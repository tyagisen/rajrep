from django.contrib import admin
from .models import Post,Category,Comment,PostView
# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(PostView)
