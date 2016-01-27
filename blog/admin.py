from django.contrib import admin
from .models import Post, Comment

#Coisas que no ADMIN podem ser criadas
admin.site.register(Post)
admin.site.register(Comment)
