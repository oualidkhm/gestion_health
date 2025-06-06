import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RdvService } from '../../src/app/services/rdv.service';

@Component({
  selector: 'app-rendezvous-list',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './rendezvous-list.component.html',
  styleUrls: ['./rendezvous-list.component.css']
})
export class RendezvousListComponent {
  private rdvService = inject(RdvService);
  rdvs: any[] = [];

  ngOnInit() {
    this.loadRdvs();
  }

  loadRdvs() {
    this.rdvService.getAll().subscribe(data => this.rdvs = data);
  }

  refresh() {
    this.loadRdvs();
  }

  delete(id: string) {
    this.rdvService.delete(id).subscribe(() => {
      this.rdvs = this.rdvs.filter(r => r._id !== id);
    });
        this.loadRdvs();  // recharge la liste automatiquement après suppression

  }
}
