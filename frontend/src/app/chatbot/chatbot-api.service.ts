import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Observable, throwError} from 'rxjs';
import {catchError, retry} from 'rxjs/operators';
import {API_URL} from '../env';
import {Chatbot} from './chatbot.model';

@Injectable()
export class ChatbotApiService {

  constructor(private http: HttpClient) {
  }

  private static _handleError(err: HttpErrorResponse | any) {
    return throwError(err.message || 'Error: Unable to complete request.');
  }

  // GET chatbot
  getChatbot(): Observable<Chatbot> {
    return this.http
      .get<Chatbot>(`${API_URL}/`).pipe(
      catchError(ChatbotApiService._handleError));
  }
}
