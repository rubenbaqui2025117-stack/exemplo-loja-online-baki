from django.contrib import admin

from .models import Categoria, Artigo, Vendedor


class ArtigoAdmin(admin.ModelAdmin):
    list_display = ["nome", "categoria", "data_de_criacao"]
    search_fields = ["nome"]

class ArtigoInline(admin.StackedInline):
    model = Artigo
    extra = 3

class CategoriaAdmin(admin.ModelAdmin):
    inlines = [ArtigoInline]
    list_display = ["nome"]
    search_fields = ["nome"]

class VendedorAdmin(admin.ModelAdmin):
    inlines = [ArtigoInline]
    list_display = ["nome", "data_de_criacao"]
    search_fields = ["nome"]

admin.site.register(Artigo, ArtigoAdmin)
admin.site.register(Vendedor, VendedorAdmin)
admin.site.register(Categoria, CategoriaAdmin)