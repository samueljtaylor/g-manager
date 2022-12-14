import app.config


class Device:
    hid_read_type: int = app.config.get('hid_defaults.hid_read_type')
    hid_read_request: int = app.config.get('hid_defaults.hid_read_request')
    hid_read_index: int = None
    hid_write_type: int = app.config.get('hid_defaults.hid_write_type')
    hid_write_request: int = app.config.get('hid_defaults.hid_write_request')
    hid_write_index: int = None
    hid_timeout: int = app.config.get('hid_defaults.hid_timeout')

    vendor_id: int = app.config.get('device_defaults.vendor_id')
    product_id: int = None
    control_interface: int = None

    report_ids: tuple = ()
    report_length: int = None
    report_map: tuple = None

    unknown_group_indexes: tuple = ()
    special_field_map: dict = {}

    _instantiated_report_map: tuple = None

    def __init__(self):
        self.num_unknown_groups = len(self.unknown_group_indexes)
        self.num_reports = len(self.report_ids)

        if self.hid_read_index is None:
            self.hid_read_index = self.control_interface

        if self.hid_write_index is None:
            self.hid_write_index = self.control_interface

    def get_report_map(self):
        if self._instantiated_report_map is None:
            self._build_instantiated_report_map()
        return self._instantiated_report_map

    def _build_instantiated_report_map(self):
        if self.report_map is None:
            raise NotImplementedError('report_map property must be set on device!')

        _class_relative_index = {}
        _names = []
        _map = []
        for item in self.report_map:
            item_name = item[0] if isinstance(item, tuple) else item.__name__
            item_class = item[1] if isinstance(item, tuple) else item

            if item_name in _names:
                raise KeyError('key: "' + item_name + '" found more than once in report_map!')

            _names.append(item_name)

            if item_class in _class_relative_index:
                _class_relative_index[item_class] += 1
            else:
                _class_relative_index[item_class] = 0

            _map.append((
                item_name,
                item_class(
                    self,
                    index=_class_relative_index[item_class],
                )
            ))

        self._instantiated_report_map = tuple(_map)
