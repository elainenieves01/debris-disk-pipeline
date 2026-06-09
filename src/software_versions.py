"""
Print versions of important software used in the pipeline.
"""

import sys
import rebound
import numpy
import pandas
import matplotlib

print("Python:", sys.version)
print("REBOUND:", rebound.__version__)
print("NumPy:", numpy.__version__)
print("Pandas:", pandas.__version__)
print("Matplotlib:", matplotlib.__version__)
