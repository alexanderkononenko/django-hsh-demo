from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.ForeignKey(User)
    email = models.EmailField()
    address = models.TextField()
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return '%s [%s]' % (self.user.name, self.email)