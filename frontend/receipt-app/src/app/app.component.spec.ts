import { TestBed } from '@angular/core/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { AppComponent } from './app.component';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { ReceiptListComponent } from './receipt-list/receipt-list.component';


describe('AppComponent', () => {
  // Test values
  const appTitle = 'Make Me Tasty';

  beforeEach(() => TestBed.configureTestingModule({
    imports: [RouterTestingModule,
              HttpClientTestingModule
             ],
    declarations: [AppComponent,
                   ReceiptListComponent
    ],
    
  }));

  it('should create the app', () => {
    const fixture = TestBed.createComponent(AppComponent);
    const app = fixture.componentInstance;
    expect(app).toBeTruthy();
  });

  it(`should have as title 'Make Me Tasty'`, () => {
    const fixture = TestBed.createComponent(AppComponent);
    const app = fixture.componentInstance;
    expect(app.title).toEqual(appTitle);
  });

  it('should render title', () => {
    const fixture = TestBed.createComponent(AppComponent);
    fixture.detectChanges();
    const compiled = fixture.nativeElement as HTMLElement;
    expect(compiled.querySelector('h1')?.textContent).toContain(appTitle);
  });
});
