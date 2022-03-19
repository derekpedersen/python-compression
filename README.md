# Python Compression API

This API is responsible for compressing binary files so that they can be more easily transmitted (size).

## Development

This program assumes you already have Python3 installed. 

Main development was done on Linux Mint 19, but the program should be compatible with MacOS. Do not personally have a Windows machine on which this could be tested but assume it would work on there as well.

The folowing was used to initiate the project:

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3
pip3 install virtualenv
virtualenv -p python3 .
source bin/activate
pip3 install Flask
```

```
export FLASK_APP=run.py
export FLASK_ENV=development
```

## Testing

```
http://127.0.0.1:5000/file-compress?filename=sample_ecg_raw.bin
```