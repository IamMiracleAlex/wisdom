from django.contrib import admin

from pages.models import Quote
from pages.forms import QuoteAdminForm


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
	form = QuoteAdminForm
	list_display = ['title', 'make_public', 'views', 'author', 'created_at'] 
