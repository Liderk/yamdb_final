from django.contrib import admin
from .models import User, Categories, Genres, Titles, Review


class UserAdmin(admin.ModelAdmin):
    # перечисляем поля, которые должны отображаться в админке
    list_display = ("pk", "username", "role", "is_superuser")
    # добавляем интерфейс для поиска по имени пользователя
    search_fields = ("username",)
    # добавляем возможность фильтрации по ролям
    list_filter = ("role",)
    # это свойство сработает для всех колонок: где пусто - там будет эта строка
    empty_value_display = '-пусто-'


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "slug")
    empty_value_display = '-пусто-'


class GenresAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "slug")
    search_fields = ("name",)
    list_filter = ("slug",)
    empty_value_display = '-пусто-'


class TitlesAdmin(admin.ModelAdmin):
    list_display = (
        "pk", "name",
        "year", 'description', 'rating')
    search_fields = ("name",)
    list_filter = ("rating",)
    empty_value_display = '-пусто-'


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("pk", "text", "author", 'score', 'pub_date',)
    search_fields = ("author",)
    list_filter = ("score",)
    empty_value_display = '-пусто-'


admin.site.register(User, UserAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Titles, TitlesAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Genres, GenresAdmin)
