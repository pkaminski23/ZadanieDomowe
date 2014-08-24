'''
Created on Aug 22, 2014

@author: pawel
'''

from django.db import models

from menu.models import Dish
from menu.models import Menu
from django.utils import timezone

class Error(models.Model):
    data = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data publikacji', null=True, default=timezone.now, editable=False, blank=True)
    email = models.EmailField()
    menu = models.ForeignKey(Menu)
    
    def save(self, *args, **kwargs):
        if not self.pub_date:
            self.pub_date = timezone.now()

        return super(Error, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return self.question

if __name__ == '__main__':
    pass