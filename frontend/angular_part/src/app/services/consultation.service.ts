import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, BehaviorSubject, tap } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class ConsultService {
  private http = inject(HttpClient);
  private baseUrl = 'http://localhost:5000/consultations';
  private neoUrl = 'http://localhost:5000/consultations/neo';

  private refreshNeeded$ = new BehaviorSubject<void>(undefined);
  get refresh$() {
    return this.refreshNeeded$.asObservable();
  }

  getAll(): Observable<any[]> {
    return this.http.get<any[]>(this.baseUrl);
  }

  // Nouvelle méthode pour récupérer toutes les données Neo4j
  getNeoConsultations(): Observable<any[]> {
    return this.http.get<any[]>(this.neoUrl);
  }

  create(consult: any): Observable<any> {
    return this.http.post(this.baseUrl, consult).pipe(
      tap(() => this.refreshNeeded$.next())
    );
  }

  update(id: string, consult: any): Observable<any> {
    return this.http.put(`${this.baseUrl}/${id}`, consult).pipe(
      tap(() => this.refreshNeeded$.next())
    );
  }

  delete(id: string): Observable<any> {
    return this.http.delete(`${this.baseUrl}/${id}`).pipe(
      tap(() => this.refreshNeeded$.next())
    );
  }

  triggerRefresh() {
    this.refreshNeeded$.next();
  }
}
