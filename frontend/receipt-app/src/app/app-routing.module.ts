import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ReceiptListComponent } from './receipt-list/receipt-list.component';
import { AddReceiptComponent } from './add-receipt/add-receipt.component';
/**
 * In Angular, the path name in the route configuration (path: 'add-receipt')
 * is the URL segment users will use to access that component
 * through the browser (like http://localhost:4200/add-receipt).
 * This does not need to match the component’s selector name in its Component decorator.
 * 
 * Selector (in the component’s .ts file):
 * This is used when embedding a component within a template,
 * like <app-add-receipt></app-add-receipt>.
 * 
 * Empty Path { path: '', redirectTo: '/receipts', pathMatch: 'full' }:
 * This defines what should happen when a user navigates 
 * to the root URL of the application (e.g., http://localhost:4200).
 * 
 * Wildcard Path { path: '**', redirectTo: '/receipts' }:
 * This is a "catch-all" or wildcard route, used to handle any undefined routes.
 */

const routes: Routes = [
  {path: 'receipts', component: ReceiptListComponent},
  {path: 'add-receipts', component: AddReceiptComponent},
  {path: '', redirectTo: '/receipts', pathMatch: 'full'},
  {path: '**', redirectTo: '/receipts'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
