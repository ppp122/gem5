from m5.params import *
from m5.SimObject import SimObject


class JiajiaObject(SimObject):
    type = "JiajiaObject"
    cxx_header = "learning_gem5/jiajiapart2/jiajia_object.hh"
    cxx_class = "gem5::JiajiaObject"
