import pprint
import json
import app.config
import app.readers
import app.readers
from app.fields.composite import Report
from array import array

b = array('B', [243, 141, 64, 255, 0, 4, 0, 0, 0, 0, 0, 0, 0, 3, 16, 24, 32, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2,
     0, 0, 3, 0, 0, 0, 1, 79, 0, 1, 80, 23, 0, 0, 19, 0, 0, 0, 1, 82, 0, 0, 30, 0, 0, 31, 0, 0, 32, 0, 0, 33, 0, 0, 34,
     0, 0, 35, 0, 0, 36, 0, 0, 37, 0, 0, 38, 0, 0, 39, 0, 0, 45, 0, 0, 46, 51, 51, 255, 1, 0, 0, 2, 0, 0, 3, 0, 0, 4, 0,
     0, 5, 0, 0, 23, 0, 0, 19, 0, 0, 20, 0, 0, 0, 1, 30, 0, 1, 31, 0, 1, 32, 0, 1, 33, 0, 1, 34, 0, 1, 35, 0, 1, 36, 0,
     1, 37, 0, 1, 38, 0, 1, 39, 0, 1, 45, 0, 1, 46])

if __name__ == '__main__':
    dev = app.config.get_device()
    r = Report(dev)
    r.load_byte_value(b)
    x = Report(dev)
    x.load_readable_value(r.get_readable_value())
    assert x != r
    assert x.get_readable_value() == r.get_readable_value()
    assert x.get_byte_value() == r.get_byte_value()
    open('tmp.json', 'w').write(r.to_json())
    y = Report(dev)
    y.load_readable_value(json.loads(open('tmp.json', 'r').read()))
    assert y != r != x
    assert y.get_readable_value() == r.get_readable_value() == x.get_readable_value()
    assert y.get_byte_value() == r.get_byte_value() == x.get_byte_value()
    assert y.get_byte_value() == b

