from django.contrib import admin
from blog.models import *
from mensajeria.models import *


# Register your models here.
admin.site.register(Post)
admin.site.register(Mensaje)
