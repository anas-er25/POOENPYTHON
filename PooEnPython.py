class Personne:
    # Déclaration des attributs de classe par défaut
    nom = "ER-RAKIBI"
    prenom = "Anas"
    age = 21

    # Méthode pour afficher les informations d'une personne
    def afficher(self):
        print(f"{self.nom} {self.prenom} {self.age}")  # imprimé en utilisant f-string


# Incrémentation de l'âge pour toute instance de classe Personne
Personne.age += 1

# Création de deux instances P1 et P2 de la classe Personne
P1 = Personne()
P2 = Personne()

# Affichage des informations de P1 et P2 avec les valeurs par défaut
P1.afficher()
P2.afficher()

# Modification des attributs de l'instance P1
P1.nom = "ALAMI"
P1.age = 25
P1.prenom = "Mohamed"

# Modification des attributs de l'instance P2
P2.nom = "RAMI"
P2.age = 18
P2.prenom = "Khalid"

# Affichage des informations de P1 et P2 avec les valeurs modifiées
P1.afficher()
P2.afficher()