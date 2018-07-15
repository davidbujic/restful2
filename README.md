# Rest API
Ovo je primer za Rest API koji koristi flask-restful ekstenziju i ima u sebi bazu kategorija. Radjen po tutorijalu [https://www.codementor.io/dongido/how-to-build-restful-apis-with-python-and-flask-fh5x7zjrx](url) U tutorijalu je koriscen PostgreSQL, ali je prepravljeno da se koristi SQLite.

## Getting Started

### Requirements
Sadrzaj requirements.txt, odnosno neophone ekstenzije:
- `flask`
- `flask_restful`
- `flask_script`
- `flask_migrate`
- `marshmallow`
- `flask_sqlalchemy`
- `flask_marshmallow`
- `marshmallow-sqlalchemy`


### Installing
Da bi se pokrenuo server, pokrece se run.py fajl.

U slucaju promene Model.py fajla, potrebno je da se pokrenu sledece komande u terminalu u okviru virtual environment-a:
`python migrate.py db migrate`
`python migrate.py db upgrade`
Ovo su komande koje vrse migraciju baze podataka, odnosno version control za bazu.

## Running the Tests

Moguci zahtevi koji mogu da se posalju na [http://localhost:5000/api/Category](url) su:

- GET - prikazuje sve kategorije
- POST - ubacuje novu kategoriju u bazu (potrebno polje je "name")
- PUT - azurira kategoriju (potrebna polja su "id" i "name")
- DELETE - brise kategoriju (potrebna polja su "id" i "name")

Format za slanje je:
`{`
`	"id": "1"`
`	"name": "kategorija"`
`}`

Takodje kao primer postoji i [http://localhost:5000/api/Hello](url) koji ima samo GET i vraca Hello World

U tutorijalu je bio i primer za komentare, ali je to bilo kao primer za vecu funkcionalnost sa vise polja, pa je bilo dovoljno uraditi samo kategorije za ovaj slucaj.
