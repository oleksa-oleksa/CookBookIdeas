import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Receipt, Ingredient } from './receipt.model';

@Injectable({
  providedIn: 'root'
})
export class ReceiptService {
  private apiUrl = 'http://127.0.0.1:8000/receipts/';

  constructor(private http: HttpClient) {}

  getReceipts(): Observable<Receipt[]> {
    /** uses Angular’s HttpClient service to make an HTTP GET request 
     * to this.apiUrl, which is the endpoint of the backend server 
     * (e.g., http://127.0.0.1:8000/receipts).
     * 
     * The <Receipt[]> part is a TypeScript generic that tells HttpClient
     * to expect an array of Receipt objects in the response.
     * 
     * The getReceipts() method doesn’t return the data immediately;
     * instead, it returns an Observable<Receipt[]>.
     * Any component that subscribes to this observable will receive the Receipt[]
     * data once the HTTP request completes and data is available.
     * Observable is a stream of data that you can observe and react to over time. 
     * In Angular, observables are provided by the RxJS library
     * Handling asynchronous events like HTTP requests, WebSocket connection:
     * Instead of waiting for data (like with promises), observables let
     * subscribe to data when it arrives and respond to it.
*/ 
    return this.http.get<Receipt[]>(this.apiUrl);
  }

  getReceiptsByTag(tag: string): Observable<Receipt[]> {
    /**
     * Using template literals (${}), a query string is appended to this.apiUrl to add a filter parameter:
     * ?tag=${tag}: This syntax creates a query string where tag is the key,
     * and the value is the value of the tag parameter passed to the function.
     * For example, if tag = "dessert", the resulting URL would be http://127.0.0.1:8000/receipts?tag=dessert.
     * 
     * $ symbol is commonly used in template literals to embed expressions within strings,
     * making it easy to create dynamic strings
     */
    const url = `${this.apiUrl}?tag=${tag}`;
    return this.http.get<Receipt[]>(url);
  }

  createReceipt(newReceipt: any): Observable<any> {
    return this.http.post<any>(this.apiUrl, newReceipt);
  }

}
