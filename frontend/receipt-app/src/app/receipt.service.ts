import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Receipt } from './receipt.model';

@Injectable({
  providedIn: 'root'
})
export class ReceiptService {
  private apiUrl = 'http://127.0.0.1:8000/receipts_with_tag/';

  constructor(private http: HttpClient) {}

  getReceipts(): Observable<Receipt[]> {
    return this.http.get<Receipt[]>(this.apiUrl);
  }

  getReceiptsByTag(tag: string): Observable<Receipt[]> {
    const url = `${this.apiUrl}?tag=${tag}`;
    return this.http.get<Receipt[]>(url);
  }

}
