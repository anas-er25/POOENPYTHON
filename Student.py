class Student:
    def __init__(self, nom, prenom, age, grade, is_enrolled, courses):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.grade = grade
        self.is_enrolled = is_enrolled
        self.courses = courses

    def afficher(self):
        print(f"{self.nom} {self.prenom} {self.age} {self.grade} {self.is_enrolled} {self.courses}")

S1= Student("RAHIMI", "Ahmed", 34, 10, True, ["Python", "Java"])
S1.afficher()
