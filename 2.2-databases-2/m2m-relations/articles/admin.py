from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, ArticleScope, Theme


class RelationshipInline(admin.TabularInline):
    model = ArticleScope
    # formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    pass