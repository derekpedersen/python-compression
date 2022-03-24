# Python Compression API

This API is responsible for compressing binary files so that they can be more easily transmitted (size).

## Development

This program assumes you already have Python3 installed. 

Main development was done on Linux Mint 19, but the program should be compatible with MacOS. Do not personally have a Windows machine on which this could be tested.

### API

The folowing was used to initiate the API project if not already installed:

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3
pip3 install virtualenv
virtualenv -p python3 .
source bin/activate
pip3 install Flask
```

## UI

The following was used to initiate the UI project if not already installed:

```bash
brew install node
npm install -g npm 
npm install -g @angular/cli
```

## Testing

<em>Given more time I would ideally have these two apps loaded into a `Dockerfile` and thus resulting in a single command to get them up and running. Wouldn't take that much time, but I got a toddler to push on a swing.</em>

At current to test/run this application locally it requires two running bash sessions/terminals.

Both of the commands make use of a `makefile` that is located at the root of this repo.

For the UI it's one command `make ui` which will start the user interface at http://localhost:4200.

For the API it's two commands, first run `source bin/activate` and then `make api` which will start the API at http://localhost:5000.

### API

If you want to try the compression algorithm results just via the api, you can open the following link a browser:

http://127.0.0.1:5000/file-compress?filename=sample_ecg_raw.bin

## Final Thoughts

Welp, I'm not a `python` developer. I should've asked if I could've done the project in `go`. My bad. Apologies for wasting anyones time.