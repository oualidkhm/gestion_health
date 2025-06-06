import { Component, inject, OnDestroy } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ConsultService } from '../../src/app/services/consultation.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-consultation-list',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './consultation-list.component.html',
  styleUrls: ['./consultation-list.component.css']
})
export class ConsultationListComponent implements OnDestroy {
  private consultService = inject(ConsultService);
  consults: any[] = [];
  private sub: Subscription;

  constructor() {
    this.loadConsults();
    this.sub = this.consultService.refresh$.subscribe(() => this.loadConsults());
  }

  loadConsults() {
    this.consultService.getAll().subscribe(data => this.consults = data);
  }

  delete(id: string) {
    this.consultService.delete(id).subscribe(() => this.loadConsults());
  }

  ngOnDestroy() {
    this.sub.unsubscribe();
  }
}
