import re

class Format:

    def __init__(self, rawFormula):
        self.rawFormula = rawFormula
        self._reduced = []
        self._listLeft = []
        self._listRight = []

    def getLeft(self): return self._listLeft
    def getRight(self): return self._listRight
    def getFormula(self): return self._reduced

    def myAbs(self, n): return n if n >= 0 else n * -1

    ####### Reduce #######
    def _printReducedForm(self, left, name):
        print(name + " form: \x1b[97m", end=''),
        for i, e in enumerate(left):
            # signs separators
            if i > 0:
                if e[0].find("-"): # if not found then display '+'
                    print(" + ", end='')
                else:
                    print(" - ", end='')
            # Reduced raw form
            if name == "Reduced":
                if i > 0 and e[0].find("-") > -1:
                    print(e[0][1:], end='')
                else:
                    print(e[0], end='')
                print(" * " + e[1], end='')
            # Reduced natural form
            else:
                if e[1][2] == '0':
                    print(e[0], end=''),
                elif e[1][2] == '1':
                    if i > 0 and e[0].find("-") > -1 and self.myAbs(float(e[0])) != 1.0:
                        print(e[0][1:], end=''),
                    elif self.myAbs(float(e[0])) != 1.0:
                        print(e[0], end='')
                    print("X", end='')
                else:
                    if e[0].find("-") and self.myAbs(float(e[0])) != 1.0:
                        print(e[0], end='')
                    elif self.myAbs(float(e[0])) != 1.0:
                        print(e[0][1:], end='')
                    print(e[1], end='')
        print(" = 0\x1b[0m")

    def _reduceLeft(self):
        cleaned = []
        for elem in self._listLeft:
            if not cleaned:
                cleaned.append(elem)
            elif float(elem[0]) != 0:
                for e in cleaned:
                    if elem[1][2] == e[1][2]:
                        e[0] = str(float(e[0]) + float(elem[0]))
                        break
                else:
                    # convert all numbers to floats
                    elem[0] = str(float(elem[0]))
                    cleaned.append(elem)
        return cleaned

    def reduceFormula(self):
        for elem in self._listRight:
            for e in self._listLeft:
                if elem[1][2] == e[1][2]:
                    e[0] = str(float(e[0]) - float(elem[0]))
                    break
            else:
                elem[0] = str(float(elem[0]) * -1)
                self._listLeft.append(elem)
        # sort in ascending order if needed
        self._listLeft.sort(key=lambda x: x[1][2])
        # reduce left if needed + filters all values equal to zero
        self._reduced = self._reduceLeft()
        self._printReducedForm(self._reduced, "Reduced")
        self._printReducedForm(self._reduced, "Natural")

    ####### PARSER #######
    def _parseMonome(self, str, sign):
        tmp = sign + str
        if str.isdigit():
            return [tmp, "X^0"]
        elif str == "X":
            return [sign + "1", "X^1"]
        elif tmp.find("*") > -1:
            res = tmp.split("*")
            if res[1] == "X":
                res[1] = "X^1"
            return res
        elif str.find("^"):
            return [sign + "1", str]
        raise Exception("unexpected token \"%s\"" % sign)

    def _parsePolynome(self, lst):
        newList = []
        found = False
        for e in lst:
            if e.find("-") > -1:
                found = True
            elif e.find("+") == -1:
                if found == True:
                    newList.append(self._parseMonome(e, "-"))
                    found = False
                else:
                    newList.append(self._parseMonome(e, ""))
        return newList

    def parse(self):
        # remove all spaces
        tmp = self.rawFormula.replace(" ", "")
        idx = tmp.index("=")
        # creates 2 strings
        left, right = tmp[:idx], tmp[idx + 1:]
        # get final lists of lists
        try:
            # creates 2 lists splitted on either + or -
            # filter is use to remove empty strings when split happens on '-' as first element of string
            self._listLeft = self._parsePolynome(filter(None, re.split('(-+|\\++)', left)))
            self._listRight = self._parsePolynome(filter(None, re.split('(-+|\\++)', right)))
        except Exception as error:
            raise Exception(error)
