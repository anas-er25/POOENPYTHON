class Personne:
    def __init__(self, nom="Nom par défaut", prenom="Prenom par défaut", age=0):
        # Attributs privés
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age

    # Getter pour l'attribut nom
    def get_nom(self):
        return self.__nom

    # Setter pour l'attribut nom avec validation
    def set_nom(self, nom):
       self.__nom = nom

    # Getter pour l'attribut prenom
    def get_prenom(self):
        return self.__prenom

    # Setter pour l'attribut prenom avec validation
    def set_prenom(self, prenom):
        self.__prenom = prenom

    # Getter pour l'attribut age
    def get_age(self):
        return self.__age

    # Setter pour l'attribut age avec validation
    def set_age(self, age):
        self.__age = age

    # Afficher l'age
    def afficher_age(self):
        print(self.__age)

    # Méthode pour afficher les informations d'une personne
    def afficher(self):
        print(f"{self.get_nom()} {self.get_prenom()} {self.get_age()}")

# Création d'une instance de la classe Personne
P1 = Personne("ER-RAKIBI", "Anas", 21)

# Affichage des informations de la personne
P1.afficher()

# Modification des attributs de la personne
P1.set_nom("D'HIMEN")
P1.set_prenom("Hatim")
P1.set_age(19)
P1.afficher_age()
x=P1.get_age()+100

# On ne peut pas faire ça : x=P1.afficher_age()+100

# Affichage des informations modifiées de la personne
P1.afficher()
print(x)
