class Utilisateur:
    id_counter = 0
    def __init__(self, nom, prenom, email, motDePasse, role ):
        Utilisateur._id_counter += 1 # gestion de l'ID peut être automatisée plus tard
        self.user_id = Utilisateur.id_counter
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.motDePasse = motDePasse
        self.role = role

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "nom": self.nom,
            "prenom": self.prenom,
            "email": self.email,
            "motDePasse": self.motDePasse,
            "role": self.role
        }