from django.contrib import admin

from Insta.models import Post, MyInstaUser, Like, Comment, UserConnection

# Register your models here.
admin.site.register(Post)
admin.site.register(MyInstaUser)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(UserConnection)