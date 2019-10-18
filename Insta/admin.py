from django.contrib import admin

from Insta.models import Post, MyInstaUser, Like, Comment, UserConnection

# Register your models here.

class CommentInline(admin.StackedInline):
    model = Comment

class LikeInline(admin.StackedInline):
    model = Like

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
        LikeInline,
    ]

class FollowingInline(admin.StackedInline):
    model = UserConnection
    fk_name = 'creator'

class FollowerInline(admin.StackedInline):
    model = UserConnection
    fk_name = 'following'

class UserAdmin(admin.ModelAdmin):
    inlines = [
        FollowerInline,
        FollowingInline,
    ]

admin.site.register(Post, PostAdmin)
admin.site.register(MyInstaUser, UserAdmin)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(UserConnection)