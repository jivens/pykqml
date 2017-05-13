import logging

class KQMLObject(object):
    """This is the parent class for KQML classes representing messages."""
    pass

from kqml.kqml_exceptions import *
from kqml.kqml_token import KQMLToken
from kqml.kqml_string import KQMLString
from kqml.kqml_list import KQMLList
from kqml.kqml_performative import KQMLPerformative
from kqml.kqml_reader import KQMLReader
from kqml.kqml_dispatcher import KQMLDispatcher
from kqml.kqml_module import KQMLModule

logging.basicConfig(format='%(levelname)s: %(modulename)s/%(name)s - %(message)s',
                    level=logging.INFO)
