from django.db import models
from django.core.urlresolvers import reverse

class TempData(models.Model):
    temp = models.FloatField()
    date_time = models.DateTimeField()
    
    def get_absolute_url(self):
        return reverse('Temperature:input')
    
    def __str__(self):
        return "The Temperature on " + str(self.date_time) + " was: " + str(self.temp)
    