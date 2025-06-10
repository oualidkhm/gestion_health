import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { Utilisateur } from '../../src/app/models/utilisateur.model';
import { AdminService } from '../../src/app/services/admin.service';

@Component({
  selector: 'app-admin-page',
  standalone: true,
  imports: [CommonModule, HttpClientModule],
  templateUrl: './admin-page.component.html',
  styleUrl: './admin-page.component.css'
})

export class AdminPageComponent implements OnInit {
  utilisateurs: Utilisateur[] = [];
  loading = false;

  constructor(private adminService: AdminService) {}

  ngOnInit(): void {
    this.chargerUtilisateurs();
  }

  chargerUtilisateurs() {
    this.loading = true;
    this.adminService.getUtilisateurs().subscribe({
      next: data => { this.utilisateurs = data; this.loading = false; },
      error: () => { alert('Erreur de chargement'); this.loading = false; }
    });
  }

  supprimerUtilisateur(index: number): void {
    const utilisateur = this.utilisateurs[index];
    const confirmation = confirm(`Supprimer ${utilisateur.nom} ${utilisateur.prenom} ?`);
    if (!confirmation) return;

    const id = utilisateur.user_id;
    if (!id) {
      alert("Impossible de supprimer : ID utilisateur introuvable.");
      return;
    }

    this.adminService.deleteUtilisateur(id)
      .subscribe({
        next: () => {
          alert('Utilisateur supprimé !');
          this.chargerUtilisateurs();
        },
        error: () => alert('Erreur de suppression')
      });
  }
}
