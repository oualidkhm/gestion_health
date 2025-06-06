import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RdvService } from '../../src/app/services/rdv.service';

@Component({
  selector: 'app-rendezvous-form',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './rendezvous-form.component.html',
  styleUrls: ['./rendezvous-form.component.css'] 
})
export class RendezvousFormComponent {
  private rdvService = inject(RdvService);
  rdv = { date: '', time: '', statut: '', patient_id: '', medecin_id: '' };

submit() {
  // Combine date et time en un seul datetime si besoin côté backend, sinon envoie séparé
  this.rdvService.create(this.rdv).subscribe(() => {
    alert('Rendez-vous créé');
    this.rdv = { date: '', time: '', statut: '', patient_id: '', medecin_id: '' };
  });
}

}
