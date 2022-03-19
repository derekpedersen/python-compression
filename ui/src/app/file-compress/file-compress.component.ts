import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FileCompress } from './file-compress.model';

@Component({
  selector: 'app-file-compress',
  templateUrl: './file-compress.component.html',
  styleUrls: ['./file-compress.component.css'],
})
export class FileCompressComponent implements OnInit {
  public file!: File;
  public uploaded!: string;
  public compressed!: FileCompress;

  constructor(private http: HttpClient) {}

  ngOnInit(): void {}

  onChange(event: any) {
    this.file = event.target.files[0];
  }

  public isReadyToUpload() {
    if (this.file === undefined || this.file === null || this.file.size === 0) {
      return false;
    }
    return true;
  }

  public uploadFile() {
    const formData = new FormData();
    formData.append('file', this.file, this.file.name);
    this.http
      .post<string>('/api/file/upload', formData)
      .subscribe((filename: any) => {
        this.uploaded = filename;
      });
  }

  public isReadyToCompress() {
    if (
      this.uploaded === undefined ||
      this.uploaded === null ||
      this.uploaded === ''
    ) {
      return false;
    }
    return true;
  }

  public compressFile(filename: string) {
    this.http
      .get<FileCompress>('/api/file/compress?filename=' + filename)
      .subscribe((data: FileCompress) => {
        this.compressed = data;
      });
  }

  public isReadyToDownload() {
    if (
      this.compressed === undefined ||
      this.compressed === null ||
      this.compressed.compressedFileName === ''
    ) {
      return false;
    }
    return true;
  }

  public downloadFile(filename: string) {
    window.open('/api/file/download?filename=' + filename, "_blank");
  }
}
