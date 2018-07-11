class Man:
    def __init__(self, name, surname, sex, growth, weight):
        self.name = name
        self.surname = surname
        self.sex = sex
        self.growth = growth
        self.weight = weight

    def __str__(self):
        return "Man: [name = {}, surname = {}, sex = {}, growth = {}, weight = {}]".format(self.name, self.surname,
                                                                                           self.sex, self.growth,
                                                                                           self.weight)


class Student(Man):
    def __init__(self, name, surname, sex, growth, weight, university, faculty, group):
        super().__init__(name, surname, sex, growth, weight)
        self.university = university
        self.faculty = faculty
        self.group = group

    def __str__(self):
        return "Student: " + super().__str__() + "university = {}, faculty = {}".format(self.university,
                                                                                        self.faculty)


class Group:
    def __init__(self):
        self.group = []

    def search(self, surname):
        for element in self.group:
            if surname in element:
                print(element)
                return element
            else:
                print("This student is not found")
                return None

    def add(self, *person):
        if len(self.group) > 10:
            print("The group is full!")
        else:
            self.group.append(person)
        return self.group

    def remove(self, surname):
        for i in range(len(self.group)):
            if surname == self.group[i][1]:
                del (self.group[i])
                return self.group[i]
            else:
                print("This student is not found")
                return 0

    def __str__(self):
        temp = ""
        for i in range(len(self.group)):
            for j in range(len(self.group[i])):
                temp += str(self.group[i][j]) + ', '
        return f"Group is: {temp}"

# Create man
man = Man("John", "Maldivian", "Male", 178, 69)
print(man)
# Create student
student_test = Student("Jason", "Winn", "Male", 174, 81, "Oxford", "Politics", "P3")
print(student_test)
# Create group
group = Group()
group.add("John", "Silver", "Male", 185, 85, "Michigan", "Economics", "E4")
group.add("Liz", "Taylor", "Female", 167, 45, "Stanford", "Article", "A2")
group.add("Kate", "Milton", "Female", 172, 55, "San-Diego", "IT", "I1")
group.add("Bob", "Norton", "Male", 180, 73, "Stanford", "Article", "A4")
group.add("Serg", "Ginzburg", "Male", 173, 65, "San-Diego", "IT", "I2")
group.add("Kent", "Baldwin", "Male", 178, 75, "Michigan", "Economics", "E5")
group.add("Jack", "Nicholson", "Male", 167, 80, "Stanford", "Article", "A5")
group.add("Paul", "Robinson", "Male", 165, 58, "San-Diego", "IT", "I2")
group.add("Christine", "Ye", "Female", 160, 40, "San-Diego", "IT", "A3")
group.add("Diana", "Kimble", "Female", 159, 45, "Stanford", "Article", "A1")
print(group)
# Search and remove functions
group.search("Winn")
group.search("Silver")
group.remove("Silver")
print(group)
