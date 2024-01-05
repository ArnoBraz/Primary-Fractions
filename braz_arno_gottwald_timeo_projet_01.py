class Fraction:
    """Implémente un objet Fraction."""

    def __init__(self, n=0, d=1):
        assert isinstance(n,int) and isinstance(d,int) and d!=0, "le numérateur et le dénominateur doivent être des entiers et le dénominateur doit être positif"
        self.n=n
        self.d=d
        if self.d<0:
            self.d=-self.d
            self.n=-self.n
        self.simplifier()

    def simplifier(self):
        """
        self - Fraction
        Sortie : None, L'object Fraction est simplifié.
        """
        for div in range(self.d, 1, -1):
            if self.d/div == self.d//div and self.n/div == self.n//div:
                self.n=self.n//div
                self.d=self.d//div


    def __del__(self):
        """
        self - Fraction
        Sortie : None, L'object Fraction est détruit.
        """
        del(self)
        

    def __repr__(self):
        return f"{self.n} / {self.d}"
        

    def __str__(self):
        len_n=len(str(self.n))
        len_d=len(str(self.d))
        maxi=len_d
        if len_d<len_n:
            maxi=len_n
            num=str(self.n)
            deno=(" "*(len_n//2)) + str(self.d)
        elif len_d>=len_n:
            maxi=len_d
            num=(" "*(len_d//2-1)) + str(self.n)
            deno=str(self.d)
        separation='_'*(maxi)
        return f"""
{num}
{separation} 
  
{deno}
        """
        

    def get_numerateur(self):
        """
        self - Fraction
        Sortie : Int, Le numérateur de l'object Fraction.
        """
        return self.n
        

    def get_denominateur(self):
        """
        self - Fraction
        Sortie : Int, Le dénominateur de l'object Fraction.
        """
        return self.d
        

    def set_numerateur(self, n):
        """
        self - Fraction
        Sortie : None, attribut un nouveau numérateur à l'object Fraction.
        """
        self.n=n
        

    def set_denominateur(self, d):
        """
        self - Fraction
        Sortie : None, attribut un nouveau dénominateur à l'object Fraction.
        """
        self.d=d
        

    def __eq__(self, frac):
        return (self.n==frac.n and self.n==frac.n)
        

    def __lt__(self, frac):
        num1=self.n*frac.d
        num2=frac.n*self.d
        return num1<num2
        

    def __add__(self, frac):
        num1=self.n*frac.d
        num2=frac.n*self.d
        deno=self.d*frac.d
        NouvFrac=Fraction((num1+num2), deno)
        return NouvFrac
        

    def __sub__(self, frac):
        num1=self.n*frac.d
        num2=frac.n*self.d
        deno=self.d*frac.d
        NouvFrac=Fraction((num1-num2), deno)
        return NouvFrac
        

    def __mul__(self, frac):
        NouvFrac=Fraction((self.n*frac.n), (self.d*frac.d))
        return NouvFrac
        

    def __truediv__(self, frac):
        NouvFrac=Fraction((self.n*frac.d), (self.d*frac.n))
        return NouvFrac
        

if __name__ == "__main__":
    fract1=Fraction(80, 12)
    fract2=Fraction(123, 2)
    fract3=Fraction(10, 2)
    print(f"fract1 : {fract1}")
    print()
    print(f"fract2 : {fract2}") 
    print()
    print(f"fract3 : {fract3}")
    print()
    
    print(f"Numérateur de fract1: {fract1.get_numerateur()}")
    print(f"Dénominateur de fract1: {fract1.get_denominateur()}")
    print()

    fract2.set_numerateur(20)
    print(f"fract2 : {fract2}")
    fract2.set_denominateur(3)
    print(f"fract2 : {fract2}")
    
    print(f"fract1==fract2 : {fract1==fract2}")
    print(f"fract1==fract3 : {fract1==fract3}")
    
    print(f"fract1<fract3 : {fract1<fract3}")
    print(f"fract1>fract3 : {fract1>fract3}")
    print()
    
    fract4=fract1+fract3
    print(f"fract4 : {fract4}")
    
    fract5=fract4-fract1
    print(f"fract5==fract3 : {fract5==fract3}")
    print()
    
    fract6=fract5*fract1
    print(f"fract6 : {fract6}")
    
    fract7=fract6/fract5
    print(f"fract7==fract1 : {fract7==fract1}")
