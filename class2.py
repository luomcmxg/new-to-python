import sys
class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tell(self):
        print("Name:\"{}\" Age:\"{}\"".format(self.name, self.age))

    def append_S(self, lst):
        lst.append(self)


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print("(Initailizing Teacher: {})".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print("Salary: \"{:d}\"".format(self.salary))


class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print("(Initailizing Student: {})".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print("Marks: \"{:d}\"".format(self.marks))
    def __getitem__(self,key):
        return self[key]

members = []
t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)
t.append_S(members)
s.append_S(members)
# members=[t,s]
print(members)
for member in members:
    member.tell()
print(t.__class__)
print(sys.builtin_module_names)