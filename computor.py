import sys
from Format import Format
from Compute import Compute

class Handler:

    def __init__(self, argc, argv):
        self.argc = argc
        self.argv = argv

    def _readInput(self, s):
        try:
            print ("\x1b[95mFormula: \x1b[0m[%s]" % s)
            f = Format(s)
            f.parse()
            f.reduceFormula()
            c = Compute(f.getFormula())
            c.compute()
        except Exception as error:
            print("Error: invalid syntax")

    def _readFromFile(self, file):
        try:
            for e in [line.rstrip('\n') for line in open(file)]:
                if len(e):
                    self._readInput(e)
        except Exception as error:
            print("Error: No such file or directory: %s" % file)

    def start(self):
        if self.argc == 3:
            if self.argv[1] == "-f":
                self._readFromFile(self.argv[2])
            else:
                print("Error: unknown option: %s" % self.argv[1])
        elif self.argc == 2:
            self._readInput(self.argv[1])
        elif self.argc < 2:
            print("Error: argument missing.")
        else:
            print("Error: too many arguments.")

def main():
    h = Handler(len(sys.argv), sys.argv)
    h.start()

if __name__ == "__main__":
    main()
