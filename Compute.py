class Compute:

    def __init__(self, formula):
        self._formula = formula
        self._deg = 0
        self._a = 0
        self._b = 0
        self._c = 0

    def _displayDegree(self):
        print("Polynomial degree:\x1b[92m " + str(self._deg) + "\x1b[0m")

    def _displayA(self):
        print ("\x1b[90ma = " + str(self._a) + "\x1b[0m")

    def _displayB(self):
        print ("\x1b[90mb = " + str(self._b) + "\x1b[0m")

    def _displayC(self):
        print ("\x1b[90mc = " + str(self._c) + "\x1b[0m")

    def _getPolynomialDegree(self):
        for e in self._formula:
            if int(e[1][2:]) > self._deg:
                self._deg = int(e[1][2:])

    def _power(self, b, p):
        if p == 1:
            return b
        return self._power(b * b, p - 1)

    def _computeDegreeTwo(self):
        for e in self._formula:
            if e[1][2:] == '0':
                self._c = float(e[0])
            elif e[1][2:] == '1':
                self._b = float(e[0])
            elif e[1][2:] == '2':
                self._a = float(e[0])
        # discriminant = b^2 - 4ac
        disc = self._power(self._b, 2) - (4 * self._a * self._c)
        print ("\x1b[90mD = " + str(disc) + "\x1b[0m")
        self._displayA()
        self._displayB()
        self._displayC()
        if self._a == 0:
            print ("\x1b[93mEvery real are solution\x1b[0m")
            return
        # Determine number of solutions
        if disc > 0:
            print ("Discriminant is strictly \x1b[93mpositive\x1b[0m, the \x1b[93mtwo solutions\x1b[0m are:")
            print ("\x1b[94mx1 = \x1b[97m" + str ((-self._b - (disc ** 0.5)) / (2 * self._a)))
            print ("\x1b[94mx2 = \x1b[97m" + str((-self._b + (disc ** 0.5)) / (2 * self._a)) + "\x1b[0m")
        elif disc == 0:
            print ("Discriminant is \x1b[93mequal to zero\x1b[0m, the \x1b[93msolution\x1b[0m is:")
            print ("\x1b[94mx = \x1b[97m" + str(-self._b / (2 * self._a)) + "\x1b[0m")
        else:
            real = -self._b / (2 * self._a)
            complx = ((-disc) ** 0.5) / (2 * self._a)
            print ("Discriminant is strictly \x1b[93mnegative\x1b[0m, the \x1b[93mtwo complex solutions\x1b[0m are:")
            print ("\x1b[94mx1 = \x1b[97m" + str(real) + '{0:+}i\x1b[0m'.format(complx))
            print ("\x1b[94mx2 = \x1b[97m" + str(real) + '{0:+}i\x1b[0m'.format(complx * -1))

    def _computeDegreeOne(self):
        if len(self._formula) > 1:
            for e in self._formula:
                if e[1][2:] == '0':
                    self._b = float(e[0])
                elif e[1][2:] == '1':
                    self._a = float(e[0])
        else:
            self._a = float(self._formula[0][0])
        # check if equals is 0 = 0
        if self._a == 0:
            print ("\x1b[93mEvery real are solution\x1b[0m")
        # check if equals n = 0
        elif self._formula[0][1][2] == '0' and self._b == 0:
            print ("\x1b[93mNo solution\x1b[0m")
        # else is valid as n * x = 0
        else:
            self._displayA()
            self._displayB()
            print ("\x1b[93mThe solution is:\x1b[0m\x1b[97m " + str(-self._b / self._a) + "\x1b[0m")

    def compute(self):
        self._getPolynomialDegree()
        self._displayDegree()
        if self._deg > 2:
            print("The polynomial degree is strictly greater than 2, I cannot solve it.")
        elif self._deg == 2:
            self._computeDegreeTwo()
        else:
            self._computeDegreeOne()
        print("")
