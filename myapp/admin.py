from django.contrib import admin

# Register your models here.

from myapp.models import Genre, Member


class GenreAdmin(admin.ModelAdmin):
    pass


admin.site.register(Genre, GenreAdmin)
admin.site.register(Member)
