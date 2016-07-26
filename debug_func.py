import sys
from IPython.core.debugger import Pdb
def set_trace():
    Pdb(color_scheme='Linux').set_trace(sys._getframe().f_back)

