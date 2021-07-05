from django.db import models

class url_strings (models.Model):

    url = models.CharField(max_length=1000)
    url_short = models.CharField(max_length = 100)
    url_title = models.CharField(max_length=20, default = 'random')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.url_title
