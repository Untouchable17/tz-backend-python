from django.contrib import admin

from src.menu import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ("id", "name", "parent", "url")