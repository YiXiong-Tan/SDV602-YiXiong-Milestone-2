import sys
sys.path.append("./controller")
from controller.test import test

if __name__ == "__main__":
    testClass = test(1)
    print(testClass.getVal())