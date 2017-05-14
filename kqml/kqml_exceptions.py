from __future__ import print_function, unicode_literals
from builtins import dict, str


class KQMLException(Exception):
    pass

class KQMLBadCharacterException(KQMLException):
    pass

class KQMLBadCloseException(KQMLException):
    pass

class KQMLBadCommaException(KQMLException):
    pass

class KQMLBadHashException(KQMLException):
    pass

class KQMLBadOpenException(KQMLException):
    pass

class KQMLBadPerformativeException(KQMLException):
    pass

class KQMLBadCommandException(KQMLException):
    pass

class KQMLExpectedListException(KQMLException):
    pass

class KQMLExpectedWhitespaceException(KQMLException):
    pass

