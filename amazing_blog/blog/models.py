from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    intro = models.TextField()
    mas = models.TextField(null=True, blank=True)
    visto = models.IntegerField()
    publicado = models.BooleanField()

    def __unicode__(self):
        return u"%s - %s" % (self.id, self.titulo)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    timestamp = models.DateTimeField()
    autor = models.CharField(max_length=50)
    post = models.ForeignKey('Post', related_name="bliblablu")

    def __unicode__(self):
        return u"%s - %s" % (self.post.titulo, self.autor)
