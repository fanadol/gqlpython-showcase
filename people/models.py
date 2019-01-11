from django.db import models


# Create your models here.
class Post(models.Model):
    description = models.TextField()
    imageUrl = models.URLField()


class People(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=150)
    email = models.EmailField()
    likedPosts = models.ManyToManyField(Post)

    @property
    def fullName(self):
        return '{} {}'.format(self.firstName, self.lastName)

# class LikedPost(models.Model):
#     people = models.ForeignKey('people.People', related_name='people', on_delete=models.CASCADE)
#     post = models.ForeignKey('people.Post', related_name='post', on_delete=models.CASCADE)
