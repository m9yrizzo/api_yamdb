from django.contrib import admin

from categories.models import Category, Genre, Title, TitleGenre


@admin.register(Genre)
class GenreInline(admin.TabularInline):
    model = TitleGenre


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'category')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'
    inlines = (GenreInline,)


admin.site.register(Category)
