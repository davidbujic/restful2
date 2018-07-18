# Opis Projekta: restful2 -demo koriscenja Flask-restful extenzije i kreiranje Rest API funkcija
Kreiran  je primer, kao templateprojekat, za Rest API koji koristi flask-restful ekstenziju i ima u sebi bazu komentara svrstanih u kategirije. Inspirisan i radjen po tutorijalu [https://www.codementor.io/dongido/how-to-build-restful-apis-with-python-and-flask-fh5x7zjrx](https://www.codementor.io/dongido/how-to-build-restful-apis-with-python-and-flask-fh5x7zjrx) .  
U tutorijalu je koriscen PostgreSQL, ali je prepravljeno da se koristi SQLite koji je deo instalacije pythona i ne zahteva posebni db server.

Razlike u odnosu na tutorijal su:

1. IDE za rad je  PyCharm
2. SQLite umesto PostgreSQL

## Getting Started

### Requirements
Za ovaj projekat potreban je Community version PyCharm.
Github.com account

File requirements.txt sadrzi listu neophdnih ekstenzija, koje pyCharm automatski instalira u virtualni environment:
- `flask`
- `flask_restful`
- `flask_script`
- `flask_migrate`
- `marshmallow`
- `flask_sqlalchemy`
- `flask_marshmallow`
- `marshmallow-sqlalchemy`
- `requests`
- `pytest`

### Installing
Ovaj projekat se pokreće pomoću PyCharm-a. Prvo je potrebno preuzeti sa GitHub-a ili pokrenuti komandu: `git clone https://github.com/nikilic/restful2`.
Nakon toga se otvara folder pomocu PyCharm-a. Ukoliko je potrebno treba podesiti interpreter na Python 2.7. Takodje treba instalirati sve ekstenzije iz requirements.txt

Da bi se pokrenuo server, pokrece se run.py fajl.

U slucaju promene Model.py fajla, potrebno je da se pokrenu sledece komande u terminalu u okviru virtual environment-a:  
`python migrate.py db migrate`  
`python migrate.py db upgrade`  
Ovo su komande koje vrse migraciju baze podataka, odnosno version control za bazu.

## Running
Program se pokreće pokretanjem run.py fajla.

## Restful API doc
#### Category API
Moguci zahtevi koji mogu da se posalju na [http://0.0.0.0:8090/api/Category](http://0.0.0.0:8090/api/Category) su:

- GET - prikazuje sve kategorije
- POST - ubacuje novu kategoriju u bazu (potrebno polje je "name")
- PUT - azurira kategoriju (potrebna polja su "id" i "name")
- DELETE - brise kategoriju (potrebna polja su "id" i "name")

Format za slanje je:
`{`
`	"id": "1"`
`	"name": "kategorija"`
`}`

1. `GET` [http://0.0.0.0:8090/api/Category](http://0.0.0.0:8090/api/Category)
Vraca listu svih kategorija 
`curl -XGET -d '' 'http://0.0.0.0:8090/api/Category'`

2. `POST` [http://0.0.0.0:8090/api/Category](http://0.0.0.0:8090/api/Category)
Dodaje novu kategoriju. Ovo je primer za slanje:
{
"name": "ime kategorije"
}
`curl -XPOST -d '{ "name":  "ime kategorije" }' 'http://0.0.0.0:8090/api/Category'`

3. `PUT` [http://0.0.0.0:8090/api/Category](http://0.0.0.0:8090/api/Category)
Menja ime kategorije na datom id-u. Ovo je primer za slanje:
{
"id": "id kategorije",
"name": "ime kategorije"
}
`curl -XPUT -d '{ "id": "id kategorije", "name":  "ime kategorije" }' 'http://0.0.0.0:8090/api/Category'`

4. `DELETE` [http://0.0.0.0:8090/api/Category](http://0.0.0.0:8090/api/Category)
Brise kategoriju. Ovo je primer za slanje:
{
"id": "id kategorije",
"name": "ime kategorije"
}
`curl -XDELETE -d '{ "id": "id kategorije", "name":  "ime kategorije" }' 'http://0.0.0.0:8090/api/Category'`

#### Comment API
Moguci zahtevi koji mogu da se posalju na [http://0.0.0.0:8090/api/Comment](http://0.0.0.0:8090/api/Comment) su:

- GET - prikazuje sve komentare
- POST - dodaje novi komentar u bazu (potrebna polja su "category_id" i "comment")

1. `GET` [http://0.0.0.0:8090/api/Comment](http://0.0.0.0:8090/api/Comment)
Vraca sve komentare
`curl -XGET -d '' 'http://0.0.0.0:8090/api/Comment'`

2. `POST` [http://0.0.0.0:8090/api/Comment](http://0.0.0.0:8090/api/Comment)
Dodaje novi komentar. Ovo je primer za slanje:
{
"category_id": "id kategorije",
"comment": "tekst komentara"
}
`curl -XPOST -d '{ "category_id": "id kategorije", "comment": "tekst komentara" }' 'http://0.0.0.0:8090/api/Comment'`

#### Hello World API
Takodje kao primer postoji i [http://0.0.0.0:8090/api/Hello](http://0.0.0.0:8090/api/Hello) koji ima samo GET i vraca Hello World.
`curl -XPOST -d '{ "category_id": "id kategorije", "comment": "tekst komentara" }' 'http://0.0.0.0:8090/api/Comment'`

## Running the Tests
Postoji i mogucnost pokretanja automatskih testova pomocu pytest ekstenzije. Skripta Tests/test_hello.py testira Hello World API, Tests/test_comment.py testira Comment API, a Tests/test_category.py testira Category API.
Ovi testovi se pokrecu iz PyCharm-a desnim klikom na fajl, pa Run.

## Versions
1. Osnovni API sa kategorijama i bazom
2. Dodati komentari, promenjen localhost u 0.0.0.0:8090 i promenjen README.md
3. Dodati testovi u Tests folder
