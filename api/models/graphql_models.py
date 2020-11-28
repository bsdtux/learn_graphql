import typing as ty
import graphene as gh


# Mock DB objects
class Author(gh.ObjectType):
    id = gh.Int()
    name = gh.String()
    books = gh.Field(gh.List(lambda: Book))

    def resolve_books(parent, info):
        return [book for book in books if book.authorId == parent.id]

authors = [
    Author(id=1, name='J. K. Rowling'),
    Author(id=2, name='J. R. R. Tolkien'),
    Author(id=3, name='Brent Weeks'),
]

class Book(gh.ObjectType):
    id = gh.Int() 
    name = gh.String()
    authorId = gh.Int()
    author = gh.Field(lambda : Author)

    def resolve_author(parent, info):
        return get_author_by_id(parent.authorId, authors)

books = [
    Book(id=1, name='Harry Potter and the Chamber of Secrets', authorId=1),
    Book(id=2, name='Harry Potter and the Prisoner of Azkaban', authorId=1),
    Book(id=3, name='Harry Potter and the Gobblet of Fire', authorId=1),
    Book(id=4, name='The Fellowship of the Ring', authorId= 2),
    Book(id=5, name='The Two Towers', authorId=2),
    Book(id=6, name='The Return of the King', authorId=2),
    Book(id=7, name='The Way of Shadows', authorId=3),
    Book(id=8, name='Beyond the Shadows', authorId=3),
]

def get_author_by_id(author_id: int, authors: ty.List) -> Author:
    author = list(filter(lambda x: x.id == author_id, authors))
    return author[-1] if author else Author()


def get_author_books(author_id: int, books: ty.List) -> ty.List:
    return list(map(lambda x: x.authorId == author_id, books)) or []


# Schemea
class Query(gh.ObjectType):
    books = gh.Field(gh.List(Book))
    book = gh.Field(Book, id=gh.Int())
    authors = gh.Field(gh.List(Author))
    author = gh.Field(Author, id=gh.Int())

    def resolve_books(parent, info):
        return books

    def resolve_book(parent, info, id):
        book = list(filter(lambda x: x.id == id, books))
        return book[0] if book else Book()

    def resolve_authors(parent, info):
        return authors

    def resolve_author(parent, info, id):
        author = get_author_by_id(id, authors)
        return author

schema = gh.Schema(query=Query)
