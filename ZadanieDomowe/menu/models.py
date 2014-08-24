'''
Created on Aug 22, 2014

@author: pawel
'''

from django.db import models
from django.utils import timezone
import ZadanieDomowe

class Dish(models.Model):
    name = models.CharField(max_length=200)
    creation_date = models.DateTimeField('Data Utworzenia', null=True, default=timezone.now, blank=True)
    price = models.FloatField()
    picture = models.ImageField(upload_to=ZadanieDomowe.settings.MEDIA_ROOT + '',
                                default=ZadanieDomowe.settings.MEDIA_ROOT + '/images/empty.jpg',
                                null = True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = timezone.now()

        self.last_modified = timezone.now()
        return super(Dish, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=200)
    creation_date = models.DateTimeField('Data Utworzenia', null=True, default=timezone.now, blank=True)
    dishes = models.ManyToManyField(Dish)
    
    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = timezone.now()

        self.last_modified = timezone.now()
        return super(Menu, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return self.name

if __name__ == '__main__':
    pass