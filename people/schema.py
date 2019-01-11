import graphene
from graphene_django import DjangoObjectType
from django.db.models import Q

from .models import People, Post


class PeopleType(DjangoObjectType):
    fullName = graphene.String()

    class Meta:
        model = People


class PostType(DjangoObjectType):
    class Meta:
        model = Post


class Query(graphene.ObjectType):
    hello = graphene.String()
    people = graphene.List(PeopleType)
    person = graphene.Field(PeopleType, id=graphene.Int())
    post = graphene.Field(PostType, id=graphene.Int())
    posts = graphene.List(PostType, search=graphene.String())

    def resolve_hello(self, info):
        return 'Hello World!'

    def resolve_people(self, info, **kwargs):
        return People.objects.all()

    def resolve_person(self, info, id=None, **kwargs):
        if not id:
            raise Exception('Please fill the id arguments!')
        return People.objects.get(id=id)

    def resolve_post(self, info, id=None):
        if not id:
            raise Exception('Please fill the id arguments!')
        return Post.objects.get(id=id)

    def resolve_posts(self, info, search=None, **kwargs):
        qs = Post.objects.all()
        if search:
            filter = (
                Q(description__incontains=search)
            )
            qs = qs.filter(filter)
        return qs


class CreatePost(graphene.Mutation):
    id = graphene.Int()
    description = graphene.String()
    imageUrl = graphene.String()

    class Arguments:
        description = graphene.String()
        imageUrl = graphene.String()

    def mutate(self, info, description, imageUrl):
        post = Post(description=description, imageUrl=imageUrl)
        post.save()

        return CreatePost(
            id=post.id,
            description=post.description,
            imageUrl=post.imageUrl
        )


class DeletePost(graphene.Mutation):
    id = graphene.Int()
    description = graphene.String()
    imageUrl = graphene.String()

    class Arguments:
        id = graphene.Int()

    def mutate(self, info, id):
        post = Post.objects.get(id=id)
        if post:
            post.delete()

        return DeletePost(
            id=id,
            description=post.description,
            imageUrl=post.imageUrl
        )


class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
    delete_post = DeletePost.Field()
