import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { RegisterService } from '../../src/app/services/register.service';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [CommonModule, FormsModule, HttpClientModule],
  templateUrl: './register.component.html',
  styleUrl: './register.component.css'
})

export class RegisterComponent {
  nom = '';
  prenom = '';
  email = '';
  motDePasse = '';
  confirmMotDePasse = '';
  role = 'patient';

  erreur = '';
  loading = false;

  constructor(
    private router: Router,
    private registerService: RegisterService
  ) {}

  onSubmit() {
    if (!this.nom || !this.prenom || !this.email || !this.motDePasse || !this.confirmMotDePasse || !this.role) {
      this.erreur = 'Tous les champs sont obligatoires.';
      return;
    }

    if (this.motDePasse !== this.confirmMotDePasse) {
      this.erreur = 'Les mots de passe ne correspondent pas.';
      return;
    }

    this.erreur = '';
    this.loading = true;

    this.registerService.register({
        nom: this.nom,
        prenom: this.prenom,
        email: this.email,
        motDePasse: this.motDePasse,
        role: this.role
      })
      .subscribe({
        next: () => {
          alert('Inscription réussie !');
          this.goToAdmin();
        },
        error: () => {
          this.erreur = 'Erreur côté serveur';
          this.loading = false;
        }
      });
}

  goToLogin() {
    this.router.navigate(['/login']);
  }

  goToAdmin() {
    this.router.navigate(['/admin']);
  }
}
