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

Each checkpoint uses a specific regular expression to validate the html page. For example, the checkpoint "All pages should contain a title tag" uses the following regex: `(?s)(?i)<title\b[^>]*>[^<>]+?<\/title>`.

New checkpoints can be added, but not without having to re-wire the Scanner class. Removing some hard coded defaults is something for a next iteration of this project.

## Future ideas

[ ] Use [Flask RESTful](https://flask-restful.readthedocs.io/en) to build the API
[ ] Remove hard-coded defaults from Scanner class
[ ] Add authentication logic
...
