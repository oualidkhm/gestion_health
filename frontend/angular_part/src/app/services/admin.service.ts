// src/app/admin.service.ts
import { Injectable } from '@angular/core';
import { Utilisateur } from '../models/utilisateur.model';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class AdminService {
  private baseUrl = 'http://localhost:5000';

  constructor(private http: HttpClient) {}

  /** GET /utilisateurs/get */
  getUtilisateurs(): Observable<Utilisateur[]> {
    return this.http.get<Utilisateur[]>(`${this.baseUrl}/utilisateurs/get`);
  }

  /** DELETE /utilisateurs/delete/<id> */
  deleteUtilisateur(id: number): Observable<any> {
    return this.http.delete(`${this.baseUrl}/utilisateurs/delete/${id}`);
  }
}
