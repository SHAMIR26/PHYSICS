class Force:
    def __init__(self, F=0.0, m=0.0, a=0.0, g=9.8):
        self.F = F
        self.m = m
        self.a = a
        self.g = g

    def calculate(self):
        if self.F == 0 and self.a == 0 and self.m != 0:
            print("force = ", self.m * self.g)
        elif self.F == 0:
            print("force = ", self.m * self.a)
        elif self.m == 0:
            print("mass = ", self.F / self.a)
        elif self.a == 0:
            print("acceleration = ", self.F / self.m)
        else:
            print("input error")

if __name__ == "__main__":
    print("Input '0' for any unknown value")
    F = float(input("Enter the force in Newtons: "))
    m = float(input("Enter the mass in kg: "))
    a = float(input("Enter the acceleration in m/s^2: "))
    Force = Force(F, m, a)
    Force.calculate()