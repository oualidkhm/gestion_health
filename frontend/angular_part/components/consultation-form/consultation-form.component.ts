import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ConsultService } from '../../src/app/services/consultation.service';

@Component({
  selector: 'app-consultation-form',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './consultation-form.component.html',
  styleUrls: ['./consultation-form.component.css']
})
export class ConsultationFormComponent {
  private consultService = inject(ConsultService);
consult = { date: '', description: '', patient_id: '', patient_name: '', medecin_id: '', medecin_name: '' };

  submit() {
    this.consultService.create(this.consult).subscribe(() => {
      alert('Consultation créée');
      this.consult = { date: '', description: '', patient_id: '', patient_name: '', medecin_id: '', medecin_name: '' };

      this.consultService.triggerRefresh();
    });
  }
}
