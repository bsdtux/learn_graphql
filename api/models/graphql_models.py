import typing as ty
from api import db
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from .models import Author, Book


# General GraphQL  Objects
class AuthorObject(SQLAlchemyObjectType):
    class Meta:
        model = Author
        interfaces = (graphene.relay.Node,) 


class BookObject(SQLAlchemyObjectType):
    class Meta:
        model = Book
        interfaces = (graphene.relay.Node,)


# Schemea Query
class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_books = SQLAlchemyConnectionField(BookObject)
    all_authors = SQLAlchemyConnectionField(AuthorObject)

schema_query = graphene.Schema(query=Query)


# Mutation
class CreateBook(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        author_name = graphene.String(required=True)

    book = graphene.Field(lambda: BookObject)

    def mutate(parent, info, name, author_name):
        user = Author.query.filter_by(name=author_name).first()
        book = Book(name=name)
        if user is not None:
            book.author = user
        db.session.add(book)
        db.session.commit()
        return CreateBook(book=book)


class CreateAuthor(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    author = graphene.Field(lambda: AuthorObject)

    def mutate(parent, info, name):
        author = Author(name=name)
        db.session.add(author)
        db.session.commit()
        return CreateAuthor(author=author)


class Mutation(graphene.ObjectType):
    save_book = CreateBook.Field()
    save_author = CreateAuthor.Field()

# noinspection PyTypeChecker
schema_mutation = graphene.Schema(query=Query, mutation=Mutation)