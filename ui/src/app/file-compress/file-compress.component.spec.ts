import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FileCompressComponent } from './file-compress.component';

describe('FileCompressComponent', () => {
  let component: FileCompressComponent;
  let fixture: ComponentFixture<FileCompressComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ FileCompressComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(FileCompressComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
