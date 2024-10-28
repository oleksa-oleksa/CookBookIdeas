import { Component, OnInit } from '@angular/core';
import { ReceiptService } from '../receipt.service'; 
import { Receipt } from '../receipt.model';

@Component({
  selector: 'app-receipt-list',
  templateUrl: './receipt-list.component.html',
  styleUrls: ['./receipt-list.component.css'],
})
export class ReceiptListComponent implements OnInit {
  receipts: Receipt[] = [];

  constructor(private receiptService: ReceiptService) {}

  ngOnInit(): void {
    this.fetchReceipts();
  }

  fetchReceipts(): void {
    this.receiptService.getReceipts().subscribe({
      next: (data: Receipt[]) => {
        this.receipts = data;
        console.log(this.receipts);  // Debugging line
      },
      error: (error) => {
        console.error('Error fetching receipts', error);
      },
      complete: () => {
        console.log('Fetching receipts completed');
      }
    });
  }
}

