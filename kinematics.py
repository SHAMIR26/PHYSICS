v = float(input("Enter velocity(v): "))
u = float(input("Enter previous velocity(u): "))   
a = float(input("Enter acceleration(a): "))
t = float(input("Enter time: "))

class kinematics:
    def __init__(self, v, u, a, t):
        self.v = v
        self.u = u
        self.a = a
        self.t = t

    def s1(self):
        return self.v * self.t

    def s2(self):
        return self.u * self.t + 0.5 * self.a * self.t ** 2

    def s3(self):
        return (self.v ** 2 - self.u ** 2) / (2 * self.a)

    def calculate(self):
        try:
            if self.u == 0 and self.a == 0:
                return self.s1()
            elif self.v == 0:
                return self.s2()
            elif self.t == 0:
                return self.s3()
            else:
                return "Correctly input your elements"
        except:
            return "Correctly input your elements"

kinematics_obj = kinematics(v, u, a, t)
print(kinematics_obj.calculate())




