import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Utilisateur } from '../models/utilisateur.model';

@Injectable({ providedIn: 'root' })
export class RegisterService {
  private baseUrl = 'http://localhost:5000';          // URL Flask

  constructor(private http: HttpClient) {}

  /** POST /utilisateurs/post */
  register(user: Omit<Utilisateur, 'id'>): Observable<any> {
    return this.http.post(`${this.baseUrl}/utilisateurs/post`, user);
  }
}
