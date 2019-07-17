# Comphero  - WCAG website checker

Web Content Accessibility Guidelines (WCAG) is developed through the W3C process in cooperation with individuals and organizations around the world, with a goal of providing a single shared standard for web content accessibility that meets the needs of individuals, organizations, and governments internationally.

This tool provides you with an easy way of validating your website acording to WCAG guidelines. 

## Stack used
1) Frontend - [Vue.js](https://vuejs.org/)
2) Backend - [(Python 3) Flask](https://palletsprojects.com/p/flask/) 

## To get started
**Note**: you might be able to use "python" and "pip" instead of "python3" and "pip3" if you only have python3 installed or if "python" and "pip" reference python3 in your machine.
```
git clone https://github.com/j-000/comphero.git
cd comphero
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 startdb.py
python3 app.py
```

in another terminal window start vue.js server. Ensure you run this command in the **frontend** folder inside the repo.
```
cd frontend
npm install
npm run serve
```

Open http://localhost:8080 and voila!

## How it works

