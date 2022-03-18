# Python Compression API

This API is responsible for compressing binary files so that they can be more easily transmitted (size).

## Development

This program was developed on a Eluktronics laptop running Linux Mint 19 and Python3

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