import app.config
import app.lang
from app.fields.byte import ByteField, DPI
from app.fields.composite import CompositeField


class DPIGroup(CompositeField):
    _map = [
        (app.lang.get('dpi_group.dpi_shift_dpi'), DPI),
        (app.lang.get('dpi_group.default_index'), ByteField),
    ]

    def initialize(self):
        for index in range(1, app.config.get_device().num_dpi_options):
            self._map.append(
                (app.lang.replace('dpi_group.dpi_item', ('index', index)), DPI)
            )