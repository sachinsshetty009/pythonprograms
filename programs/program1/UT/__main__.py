import os
import sys

WD_DIR=os.environ["WD_DIR"]
sys.path.insert(0, WD_DIR + "/programs/program1")

from ut_program1 import *

if __name__ == '__main__':
    unittest.main()