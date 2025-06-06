import { Component, ViewChild } from '@angular/core';

import { ConsultationListComponent } from './../../components/consultation-list/consultation-list.component';
import { ConsultationDetailComponent } from './../../components/consultation-detail/consultation-detail.component';

import { RendezvousListComponent } from './../../components/rendezvous-list/rendezvous-list.component';
import { RendezvousFormComponent } from './../../components/rendezvous-form/rendezvous-form.component';
import { HttpClientModule } from '@angular/common/http';
import { ConsultationFormComponent } from '../../components/consultation-form/consultation-form.component';
import { NavbarComponent } from '../../components/navbar/navbar.component';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    HttpClientModule,
    RouterModule,  // juste RouterModule sans forRoot
    ConsultationListComponent,
    ConsultationDetailComponent,
    RendezvousListComponent,
    ConsultationFormComponent,
    RendezvousFormComponent,
    NavbarComponent
  ],
  templateUrl: './app.component.html',
})
export class AppComponent {
  @ViewChild(RendezvousListComponent) rdvList!: RendezvousListComponent;

  onRdvCreated() {
    this.rdvList.refresh();
  }
}
