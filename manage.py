import click
from api import create_app, db
from api.models.models import Author, Book
app = create_app()

@app.cli.command("create-db")
def create_db():
    db.create_all()

@app.cli.command("drop-db")
def drop_db():
    db.drop_all()

@app.cli.command("seed")
def seed():
    db.drop_all()
    db.create_all()

    jk = Author(name='JK Rowling')
    jr = Author(name='J. R. R. Tolkein')
    db.session.add(jk)
    db.session.add(jr)
    db.session.commit()

    book1 = Book(id=1, name='Harry Potter and the Chamber of Secrets')
    book1.author = jk
    book2 = Book(id=2, name='Harry Potter and the Prisoner of Azkaban')
    book2.author = jk
    book3 = Book(id=3, name='Harry Potter and the Gobblet of Fire')
    book3.author = jk

    book4 = Book(id=4, name='The Fellowship of the Ring')
    book4.author = jr
    book5 = Book(id=5, name='The Two Towers')
    book5.author = jr

    db.session.add(book1)
    db.session.add(book2)
    db.session.add(book3)
    db.session.add(book4)
    db.session.add(book5)

    db.session.commit()

