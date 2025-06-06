import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ConsultService } from '../../src/app/services/consultation.service';

@Component({
  selector: 'app-consultation-detail',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './consultation-detail.component.html',
  styleUrls: ['./consultation-detail.component.css'] 
})
export class ConsultationDetailComponent {
  private consultService = inject(ConsultService);

  consultations: any[] = [];

  ngOnInit() {
    this.consultService.getNeoConsultations().subscribe(data => {
      this.consultations = data;
    });
  }

  // Si tu veux permettre une mise à jour sur chaque consultation
  update(consult: any) {
    this.consultService.update(consult._id, consult).subscribe(() => {
      alert('Consultation mise à jour');
    });
  }
}
