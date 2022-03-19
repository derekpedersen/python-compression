import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { FileCompressComponent } from './file-compress/file-compress.component';

const routes: Routes = [
  { path: 'compress', component: FileCompressComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
