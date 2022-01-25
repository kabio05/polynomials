from numbers import Number 

class Polynomial:
    
    def __init__(self, coefs):
        self.coefficients = coefs
        
    def degree(self):
        return len(self.coefficients)-1

    def __str__(self):
        
        coefs = self.coefficients
        terms = []
        
        if coefs[0]: 
            terms.append(str(coefs[0]))
        if self.degree() > 0 and coefs[1]:
            terms.append(f"{'' if coefs[1]==1 else coefs[1]}x")
        
        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d,c in enumerate(coefs[2:],start =2) if c]
        
        return "+".join(reversed(terms)) or "0" # python will only evaluate second operands if the first one is false, blank string is false
    
    def __eq__(self,other):
        
        return self.coefficients == other.coefficients
    
    def __add__(self,other):
        
        if isinstance(other,Polynomial):
            common = min(self.degree(),other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common: ] + other.coefficients[common:]
            
            return Polynomial(coefs)
        
        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])
        
        else:
            return NotImplemented
            
    def __radd__(self,other):
        return self + other 
        
        