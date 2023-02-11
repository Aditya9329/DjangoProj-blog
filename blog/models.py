from django.db import models

class BlogContent(models.Model):
    # blog number as b_no
    b_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    author  = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    timestamp =  models.DateTimeField(blank=True)
    
    def __str__(self):
        return self.title + ' by ' +self.author