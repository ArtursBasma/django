from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'joined_date')  # Nomaina 'date' uz 'joined_date'
    search_fields = ['title', 'author']  # Paliek tas pats


# Reģistrē Post modeli ar definēto admin klasi
admin.site.register(Post, PostAdmin)

