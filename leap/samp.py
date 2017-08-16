
import sys
sys.path.insert(0, "./lib")

import Leap

def main():
     controller = Leap.Controller()

     # Keep this process running until Enter is pressed
     print ("Press Enter to quit...")
     try:
         sys.stdin.readline()
     except KeyboardInterrupt:
         pass