export interface Utilisateur {
  _id?: string;      // id Mongo renvoyé par l’API
  user_id?: number;       // (éventuel) id interne
  nom: string;
  prenom: string;
  email: string;
  motDePasse: string;
  role: string;
}
