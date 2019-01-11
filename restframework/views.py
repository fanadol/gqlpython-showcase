from people.models import Post, People
from rest_framework import viewsets
from .serializer import PostSerializer, PeopleSerializer


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    """
    API Endpoint that allows posts to be viewed or edited
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PeopleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows people to be viewed or edited
    """
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
