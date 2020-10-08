from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'posted_on', 'updated_on')
    search_fields = ('title', 'description')


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(PostComments)