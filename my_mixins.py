class A:
    total = 27


class B(A):
    age = 45


class C(A):
    name = "bright"


class M:
    def print_total(self):
        print(self.total)

    def print_age(self):
        print(self.age)

    def print_name(self):
        print(self.name)


class D(B, M):
    pass


class E(C, M):
    pass


e = E()
e.print_total()
e.print_name()
# e.print_age()

d = D()
d.print_age()
d.print_total()