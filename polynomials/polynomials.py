from numbers import Number, Integral


class Polynomial:

    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and\
             self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other
    
    def __sub__(self,other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a - b for a, b in zip(self.coefficients,
                                                other.coefficients))
            if self.coefficients >= other.coefficients:
                coefs = coefs + self.coefficients[common:]
                return Polynomial(coefs)
            else:
                coefs += tuple(-i for i in other.coefficients[common:])
                return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] - other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented
        
    def __rsub__(self, other):
        return Polynomial((other - self.coefficients[0],) + tuple(-i for i in self.coefficients[1:]))
    
    def __mul__(self, other):
        
        if isinstance(other, Number):
            coefs_1 = tuple(other*i for i in self.coefficients)
            return Polynomial(coefs_1)
        
        if isinstance(other, Polynomial):
            # initialize storage polynomial
            Poly = Polynomial(())
            
            for i ,j in tuple(enumerate((other.coefficients))):
                coefs_2 = tuple(0 for l in range(i)) + tuple(j*m for m in self.coefficients) # give mutiplication of each coefficient of other
                Poly += Polynomial(coefs_2) # add each one to the storage polynomial
                
            return Poly
        
    def __rmul__(self,other):
        return self * other
    
    def __pow__(self,power):
    
        if isinstance(power, Integral) and power > 0:
            Poly = self
            for i in range(power-1):
                Poly = Poly * self # just make power times mutiplication
            return Poly
        
        else:
            return NotImplemented
    
    def __call__(self,value):
        a = self.coefficients[0]
        for i,j in tuple(enumerate(self.coefficients[1:],start = 1)):
            a += j * (value ** i)
        return a
    
    def dx(self):
        
        
        if len(self.coefficients) > 1:
            return Polynomial(tuple(i*j for i,j in tuple(enumerate(self.coefficients[1:],start = 1))))
        
        # exclude 0-power case
        else:
            return Polynomial((0,))
        

def derivative(Poly):
    """"Import a polynomial, return the derivative of polynomial."""
    if isinstance(Poly,Polynomial):
        return Poly.dx()
    else:
        return NotImplemented