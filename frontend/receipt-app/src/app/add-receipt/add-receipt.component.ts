import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, FormArray, Validators, AbstractControl, ValidationErrors} from '@angular/forms';
import { Router } from '@angular/router';
import { UnitEnum } from 'src/shared/unit-enum';
import {ReceiptService } from '../receipt.service';
import { formatDate } from '@angular/common';
import { Ingredient } from '../receipt.model';

/** By creating a dedicated component, AddReceiptComponent, for adding new receipts,
 * the app modular is kept and focused on single responsibilities. 
 * This component handles all the necessary form control and validation, 
 * while the service method createReceipt abstracts the backend interaction,
 * keeping the component clean. This approach allows for easy expansion and maintenance.
 * 
 * Create a New Angular Component: 
 * This component will be responsible for the "Add New Receipt" form,
 * allowing users to enter details like title, photo URL, ingredients, 
 * preparation steps, tags, and ratings. We’ll also need a button to submit the form
 * 
 * Set Up Angular Service to Interact with Backend: 
 * You’ll need a new method in the existing ReceiptService t
 * hat sends a POST request to the backend to add a new receipt.
 * 
 * Handle Form Submission and User Feedback: Once a user submits the form,
 * the new receipt will be sent to the backend. 
 * If successful, a success message will display; otherwise,
 * an error message will guide the user on how to proceed.
 * 
 * HOW IT WORKS:
 * Backend Endpoint: The @app.post("/receipts/") endpoint in FastAPI backend
 * is defined to accept new receipt data and add it to the database. 
 * This endpoint is a POST request, which, when called, will create a new record
 * without modifying or deleting existing receipts.
 * 
 * Frontend Form: In the Angular form for adding a receipt, the UI and function are created
 * to send form data to the backend. When the form is submitted, it makes an HTTP POST request
 * to the /receipts/ endpoint. This data is packaged as a new receipt object and sent to the backend.
 * 
 * Database Behavior: When the backend endpoint receives the POST request, it:
 * Creates a new Receipt object with the provided data.
 * Adds it to the database session (db.add(db_receipt)).
 * Commits the transaction (db.commit()), which effectively saves the new receipt in the database.
*/
@Component({
  selector: 'app-add-receipt',
  templateUrl: './add-receipt.component.html',
  styleUrls: ['./add-receipt.component.css']
})
export class AddReceiptComponent implements OnInit {
  receiptForm!: FormGroup;
  formErrors: string[] = [];
  unitOptions = Object.values(UnitEnum);  // Extracts UnitEnum values

  constructor(
    private fb: FormBuilder,
    private receiptService: ReceiptService,
    private router: Router
  ) {}

  ngOnInit(): void {
    const today = formatDate(new Date(), 'yyyy-MM-dd', 'en');

    this.receiptForm = this.fb.group({
      title: ['', Validators.required],
      photo_url: ['', Validators.required],
      ingredients: this.fb.array([
        this.createIngredient()
      ]),
      preparation_steps: ['', Validators.required],
      tags: [''],
      date_added: [today],  // Default to today's date
      date_cooked: [''],
      rating: [null]
    });
  }

  // Custom numeric validator to accept only integers or floats
  private numericValidator(control: AbstractControl): ValidationErrors | null {
    const valid = /^-?\d*\.?\d*$/.test(control.value); // Regex for integers and decimals
    return valid ? null : { numeric: { value: control.value } };
  }

  createIngredient(): FormGroup {
    return this.fb.group({
      name: ['', Validators.required],
      amount: ['', [this.numericValidator]], // Use numericValidator as a synchronous validator
      unit: ['Gramm']
    });
  }

  get ingredients(): FormArray {
    return this.receiptForm.get('ingredients') as FormArray;
  }

  addIngredient(): void {
    this.ingredients.push(this.createIngredient());

  }

  removeIngredient(index: number): void {
    this.ingredients.removeAt(index);
  }

  onSubmit(): void {
    // Debug
    console.log('Form Data:', this.receiptForm.value);
  
    this.formErrors = [];
    if (this.receiptForm.valid) {
      const newReceipt = {
        title: this.receiptForm.get('title')?.value,
        photo_url: this.receiptForm.get('photo_url')?.value,
        ingredients: this.receiptForm.value.ingredients.map((ingredient: Ingredient) => ({
          name: ingredient.name,
          amount: ingredient.amount,
          unit: ingredient.unit,
      })),
        preparation_steps: this.receiptForm.value.preparation_steps.split('\n').map((step: string) => step.trim()),
        tags: this.receiptForm.value.tags.split(',').map((tag: string) => tag.trim()),
        date_added: this.receiptForm.get('date_added')?.value,
        date_cooked: this.receiptForm.value.date_cooked || null,
        rating: this.receiptForm.get('rating')?.value,
      };

      this.receiptService.createReceipt(newReceipt).subscribe({
        next: () => this.router.navigate(['/receipts']),
        error: (error) => {
          console.error('Error creating receipt', error);
        }
      });
    } else {
      Object.keys(this.receiptForm.controls).forEach(controlName => {
        const control = this.receiptForm.get(controlName);
        if (control && control.invalid) {
          Object.keys(control.errors || {}).forEach(errorKey => {
            switch (errorKey) {
              case 'required':
                this.formErrors.push(`The ${controlName} field is required.`);
                break;
              default:
                this.formErrors.push(`The ${controlName} field has an error.`);
            }
          });
        }
      });
    }
  }
}
