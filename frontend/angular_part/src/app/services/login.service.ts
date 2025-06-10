import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { catchError, throwError } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class LoginService {
  private apiUrl = 'http://localhost:5000';

  constructor(private http: HttpClient) {}

  verifierUtilisateur(email: string): Observable<any> {
    return this.http.get(`${this.apiUrl}/utilisateurs/email/${email}`);
  }
}
