from kqml import KQMLObject
from kqml.kqml_reader import KQMLReader

try:
    from BytesIO import BytesIO
except ImportError:
    from io import BytesIO

def test_read_list():
    s = b'(FAILURE :reason INVALID_DESCRIPTION)'
    sreader = BytesIO(s)
    kr = KQMLReader(sreader)
    lst = kr.read_list()
    for obj in lst:
        assert(isinstance(obj, KQMLObject))

def test_read_performative():
    s = b'(REQUEST :CONTENT (REQUEST_TYPE :CONTENT "<ekb>ONT::PROTEIN</ekb>"))'
    sreader = BytesIO(s)
    kr = KQMLReader(sreader)
    kp = kr.read_performative()
