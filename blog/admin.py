from django.contrib import admin
from blog.models import BlogContent
# Register your models here.
# we registor our model toadmin so that we can manage the modelsfrom admin section
admin.site.register(BlogContent)
