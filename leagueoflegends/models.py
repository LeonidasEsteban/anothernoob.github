from django.db import models
from athumb.fields import ImageWithThumbsField
from athumb.backends.s3boto import S3BotoStorage_AllPublic
from django.contrib.auth.models import User

# Create your models here.

class Roles(models.Model):
    label = models.CharField(max_length = 140, verbose_name = 'rol')
    
    class Meta:
        verbose_name = 'rol'
        verbose_name_plural = 'roles'
        
    def __unicode__(self):
        return self.label

class Champions(models.Model):
    name = models.CharField(max_length = 140, verbose_name = 'nombre')
    rol = models.ManyToManyField(Roles, verbose_name = 'roles')
    portrait = ImageWithThumbsField(
        upload_to="champions/portrait",
        thumbs=(
            ('32x32', {'size': (32, 32)}),
        ),
        blank=True, null=True)
    splashscreen = models.ImageField(upload_to = 'champions/splash', verbose_name = 'portada')
    
    class Meta:
        verbose_name = 'campeon'
        verbose_name_plural = 'campeones'
        
    def __unicode__(self):
        return self.name
    
class Players(models.Model):
    nickname = models.CharField(max_length = 140, verbose_name = 'nombre de invocador')
    user = models.ForeignKey(User, verbose_name = 'usuario')
    
    class Meta:
        verbose_name = 'invocador'
        verbose_name_plural = 'invocadores'
        
    def __unicode__(self):
        return self.nickname
    
# Admin site
from django.contrib import admin

admin.site.register(Champions)
admin.site.register(Players)
admin.site.register(Roles)