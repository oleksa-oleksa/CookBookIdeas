import { TestBed } from '@angular/core/testing';
import { ReceiptService } from './receipt.service';
import { HttpClientTestingModule } from '@angular/common/http/testing';

describe('ReceiptService', () => {
  let service: ReceiptService;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule]  
    });
    service = TestBed.inject(ReceiptService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
