def NOD(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


class Fractions:
    def __init__(self, numerator, denominator):
        self.numerator = int(numerator)
        self.denominator = int(denominator)

    def __add__(self, other):
        new_chisl = self.numerator * other.denominator + other.numerator * self.denominator
        new_znam = self.denominator * other.denominator
        nod = NOD(new_chisl, new_znam)
        return Fractions(new_chisl / nod, new_znam / nod)

    def __eq__(self, other):
        return other.numerator / self.numerator == other.denominator/self.denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

data = input().split(',')
first_fraction = data[0].split()
second_fracton = data[1][1:].split()
first_numerator, first_denominator = int(first_fraction[0]), int(first_fraction[1])
second_numerator, second_denominator = int(second_fracton[0]), int(second_fracton[1])
Fraction1 = Fractions(first_numerator, first_denominator)
Fraction2 = Fractions(second_numerator,second_denominator)
print(Fraction1+Fraction2)
print(Fraction1 == Fraction2)