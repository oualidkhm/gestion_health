import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { LoginService } from '../../src/app/services/login.service';
import { HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, FormsModule, HttpClientModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
  email = '';
  motDePasse = '';

  erreur = '';
  submitted = false;

  constructor(
    private router: Router,
    private loginService: LoginService
  ) {}

  onSubmit() {
    this.submitted = true;
    this.erreur = '';

    if (!this.email || !this.motDePasse) {
      this.erreur = 'Tous les champs sont obligatoires.';
      return;
    }
    
    this.loginService.verifierUtilisateur(this.email).subscribe({
      next: (utilisateur) => {
        if (utilisateur.motDePasse === this.motDePasse) {
          alert('Connexion réussie ! Vous êtes connecté en tant que ' + utilisateur.role + '.');
          switch (utilisateur.role) {
            case 'admin':
            this.router.navigate(['/admin']);
            break;
          case 'médecin':
          case 'medecin':  // pour être tolérant aux deux orthographes
            this.router.navigate(['/list-rdv']);
            break;
          case 'patient':
            this.router.navigate(['/form-rdv']);
            break;
          default:
            this.erreur = 'Rôle inconnu. Veuillez contacter l’administrateur.';
          }
        } else {
          this.erreur = 'Email et/ou mot de passe incorrect';
        }
      },
      error: (err) => {
        console.error(err);
        this.erreur = 'Email et/ou mot de passe incorrect';
      }
    });
  }

  goToRegister() {
    this.router.navigate(['/register']);
  }
}
