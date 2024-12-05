####inheritance##
# class collage():
#     def classroom(self):
#         print("bench")
# class student(collage):
#     def manavan(self):
#         print("test")
# vikki=student()
# vikki.classroom()

###Multiple inheritance##
# class collage():
#     def classroom(self):
#         print("bench")
# class professor():
#     def master(self):
#         print("paper")
# class student(professor,collage):
#     def manavan(self):
#         print("test")
# vikki=student()
# vikki.classroom()
# vikki.master()

##multilevel inheritance###
# class collage():
#     def classroom(self):
#         print("bench")
# class professor(collage):
#     def master(self):
#         print("paper")
# class student(professor):
#     def manavan(self):
#         print("test")
# vikki=student()
# vikki.master()
# p1=professor()
# p1.classroom()

## Hierarchial inheritance##
# class college():
#     def classroom(self):
#         print("bench")
# class student(college):
#     def manavan(self):
#         print("test")
# class student1(college):
#     def manavan(self):
#         print("test")
# class student2(college):
#     def manavan(self):
#         print("test")
# buddy2=student1()
# buddy2.classroom()

##Hybrid inheritance
# class college():
#     def classroom(self):
#         print("bench")
# class principal():
#     def HOD(self):
#         print("permission")
# class student(college):
#     def manavan(self):
#         print("test")
# class student1(college,principal):
#     def manavan(self):
#         print("test")
# class student2(college,principal):
#     def manavan(self):
#         print("test")
# buddy2=student2()
# buddy2.HOD()
# buddy2.manavan()

###super keyword##
# class a():
#     def __init__(self):
#         print("phy")
#     def subject(self):
#         print("physics")
# class b():
#     def __init__(self):
#         # super().__init__()
#         print("chem")
#     def subject(self):
#         print("chemistry")
# class c(b,a):
#     def __init__(self):
#         super().__init__()
#         print("mat")
#     def subject(self):
#         print("maths")
# master=c()

##polymorphism
# class animal():
#     def sound(self):
#         print("animal makes sound")
# class dog():
#     def sound(self):
#         print("dog barks")
# class bird(animal):
#     def sound(self):
#         print("bird sing")
# b=bird()
# b.sound()

# class shape():
#     def area(self):
#         return "0"
# class rectangle(shape):
#     def area(self):
#         l=5
#         b=2
#         print(l*b)
# A=rectangle()
# A.area()

# class person():
#     def __init__(self,name):
#         self.name=name
# class student(person):
#     def __init__(self,name,grade):
#         super().__init__(name)
#         self.grade=grade
#     def display(self):
#         print(self.name,self.grade)
# d1=student("ram","A")
# d1.display()

# class vehicle():
#     def start(self):
#         print("vehicle started")
# class car(vehicle):
#     def display(self):
#         print("car started")
# v=car()
# v.display()

# class employee():
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
# class manager(employee):
#     def __init__(self,name,salary,department):
#         super().__init__(name,salary)
#         self.department=department
#     def display(self):
#         print(self.name,self.salary,self.department)
# m1=manager("Raju","15000","Mechanical")
# m1.display()

#######Encapsulation(private)
# class company():
#     def __init__(self):
#         self.__companyName="google"
#     def companyName(self):
#         print(self.__companyName)
# c1=company()
# c1.companyName()













