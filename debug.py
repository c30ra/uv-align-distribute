PYDEV_SOURCE_DIR = "C:\\Users\\Luca\\.p2\\pool\\plugins\\org.python.pydev_4.4.0.201510052309\\pysrc"
 
import sys
 
if PYDEV_SOURCE_DIR not in sys.path:
    sys.path.append(PYDEV_SOURCE_DIR)
 
import pydevd
#uncomment this line to start debugging with ecplise 
#pydevd.settrace()
 
bling = "start debugging"
print(bling)
