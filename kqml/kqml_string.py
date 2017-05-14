from __future__ import print_function, unicode_literals
from builtins import dict, str

try:
    from BytesIO import BytesIO
except ImportError:
    from io import BytesIO
from kqml import KQMLObject

class KQMLString(object):
    def __init__(self, data=None):
        if data is None:
            self.data = ''
        else:
            self.data = data

    def __len__(self):
        return len(self.data)

    def char_at(self, n):
        return self.data[n]

    def equals(self, obj):
        if not isinstance(obj, KQMLString):
            return False
        else:
            return obj.data == self.data

    def write(self, out):
        out.write('"'.encode('utf-8'))
        for ch in self.data:
            if ch == '"':
                out.write('\\'.encode('utf-8'))
            out.write(ch.encode('utf-8'))
        out.write('"'.encode('utf-8'))

    def to_string(self):
        out = BytesIO()
        self.write(out)
        return out.getvalue().decode()

    def string_value(self):
        return self.data

    def __str__(self):
        return self.to_string()

    def __repr__(self):
        s = self.__str__()
        s = s.replace('\n', '\\n')
        return s

    def __getitem__(self, *args):
        return self.data.__getitem__(*args)

