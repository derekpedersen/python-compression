api:
	nohup flask run > log.txt 2>&1 &

ui: 
	cd ui && npm run start

serve: api ui

# brew install node
# npm install -g npm 
# npm install -g @angular/cli
# npm install><P: