import { inject, Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, BehaviorSubject, tap } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class RdvService {
  private http = inject(HttpClient);
  private baseUrl = 'http://localhost:5000/rdv';

  // Subject pour notifier les changements
  private refreshNeeded$ = new BehaviorSubject<void>(undefined);

  get refresh$() {
    return this.refreshNeeded$.asObservable();
  }

  getAll(): Observable<any[]> {
    return this.http.get<any[]>(this.baseUrl);
  }

  create(rdv: any): Observable<any> {
    return this.http.post(this.baseUrl, rdv).pipe(
      tap(() => this.refreshNeeded$.next())
    );
  }

  update(id: string, rdv: any): Observable<any> {
    return this.http.put(`${this.baseUrl}/${id}`, rdv).pipe(
      tap(() => this.refreshNeeded$.next())
    );
  }

  delete(id: string): Observable<any> {
    return this.http.delete(`${this.baseUrl}/${id}`).pipe(
      tap(() => this.refreshNeeded$.next())
    );
  }
}
