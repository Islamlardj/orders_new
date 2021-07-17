from django.contrib import admin
from.models import Commande, Products
from import_export.admin import ImportExportModelAdmin
# Register your models here.
admin.site.register(Commande)
# admin.site.register(Products)
@admin.register(Products)
class ProductsImport(ImportExportModelAdmin):
	pass
	