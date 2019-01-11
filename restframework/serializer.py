from people.models import Post, People
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'description', 'imageUrl')


class PeopleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = People
        fields = ('id', 'fullName', 'firstName', 'lastName', 'email')
