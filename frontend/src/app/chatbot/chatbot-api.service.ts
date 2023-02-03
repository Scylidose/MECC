import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Observable, throwError} from 'rxjs';
import {catchError, retry} from 'rxjs/operators';
import {API_URL} from '../env';
import {Chatbot} from './chatbot.model';

@Injectable()
export class ChatbotApiService {
  private url: string;
  
  constructor(private http: HttpClient) {
    this.url = `${API_URL}/message`;
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

  public send(chatbot: Chatbot): Observable<any> {
    return this.http.post(this.url, chatbot);
  }

  saveChatbot(chatbot: Chatbot): Observable<any> {
    return this.http
      .post(this.url, chatbot);
  }
}
