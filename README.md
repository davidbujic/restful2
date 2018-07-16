# Rest API
Ovo je primer za Rest API koji koristi flask-restful ekstenziju i ima u sebi bazu kategorija. Radjen po tutorijalu [https://www.codementor.io/dongido/how-to-build-restful-apis-with-python-and-flask-fh5x7zjrx](https://www.codementor.io/dongido/how-to-build-restful-apis-with-python-and-flask-fh5x7zjrx) U tutorijalu je koriscen PostgreSQL, ali je prepravljeno da se koristi SQLite.

Razlike u odnosu na tutorijal su:

1. Rad u PyCharm-u
2. SQLite umesto PostgreSQL
3. Eliminacija dela sa komentarima, ovde su samo kategorije

## Getting Started

### Requirements
Za ovaj projekat potreban je PyCharm.

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
Ovaj projekat se pokreće pomoću PyCharm-a. Prvo je potrebno preuzeti sa GitHub-a ili pokrenuti komandu: `git clone https://github.com/nikilic/restful2`.
Nakon toga se otvara folder pomocu PyCharm-a. Ukoliko je potrebno treba podesiti interpreter na Python 2.7. Takodje treba instalirati sve ekstenzije iz requirements.txt

Da bi se pokrenuo server, pokrece se run.py fajl.

U slucaju promene Model.py fajla, potrebno je da se pokrenu sledece komande u terminalu u okviru virtual environment-a:
`python migrate.py db migrate`
`python migrate.py db upgrade`
Ovo su komande koje vrse migraciju baze podataka, odnosno version control za bazu.

## Running
Program se pokreće pokretanjem run.py fajla.

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

1. `GET` [http://localhost:5000/api/Category](url)
Vraca listu svih kategorija 

2. `POST` [http://localhost:5000/api/Category](url)
Dodaje novu kategoriju. Ovo je primer za slanje:
{
"name": "ime kategorije"
}

3. `PUT` [http://localhost:5000/api/Category](url)
Menja ime kategorije na datom id-u. Ovo je primer za slanje:
{
"id": "id kategorije",
"name": "ime kategorije"
}


4. `DELETE` [http://localhost:5000/api/Category](url)
Brise kategoriju. Ovo je primer za slanje:
{
"id": "id kategorije",
"name": "ime kategorije"
}

Takodje kao primer postoji i [http://localhost:5000/api/Hello](url) koji ima samo GET i vraca Hello World.

## Versions
1. Osnovni API sa kategorijama i bazom
