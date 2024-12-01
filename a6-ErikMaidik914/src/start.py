#
# This module is used to invoke the program's UI and start it. It should not contain a lot of code.
#
from tests import *
from ui import run_console

def run():
    run_tests()
    run_console()

if __name__ == '__main__':
    run()




