import { ComponentFixture, TestBed } from '@angular/core/testing';
import { ReceiptListComponent } from './receipt-list.component';
import { HttpClientTestingModule } from '@angular/common/http/testing'; 


describe('ReceiptListComponent', () => {
  let component: ReceiptListComponent;
  let fixture: ComponentFixture<ReceiptListComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ReceiptListComponent],
      imports: [HttpClientTestingModule] 
    });
    fixture = TestBed.createComponent(ReceiptListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
