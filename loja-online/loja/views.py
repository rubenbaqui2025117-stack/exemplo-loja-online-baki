from django.views import generic

from .models import Artigo, Categoria, Vendedor


class IndexView(generic.ListView):
    template_name = "loja/index.html"
    context_object_name = "lista_de_artigos"

    def get_queryset(self):
        """Devolva uma lista com todos os artigos"""
        return Artigo.objects.order_by("-data_de_criacao")

class ArtigoView(generic.DetailView):
    model = Artigo
    template_name = "loja/artigo.html"

class CategoriaView(generic.ListView):
    template_name = "loja/categoria.html"
    context_object_name = "contexto"

    def get_queryset(self):
        """Devolva uma lista com todos os artigos associados a esta categoria"""
        pk = self.kwargs['pk']
        categoria = Categoria.objects.get(pk=pk)
        artigos = Artigo.objects.filter(categoria=categoria)

        contexto = {}
        contexto['lista_de_artigos'] = artigos.order_by("-data_de_criacao")
        contexto['categoria'] = categoria
        return contexto

class VendedorView(generic.ListView):
    template_name = "loja/vendedor.html"
    context_object_name = "contexto"

    def get_queryset(self):
        """Devolva uma lista com todos os artigos associados a esta categoria"""
        pk = self.kwargs['pk']
        vendedor = Vendedor.objects.get(pk=pk)
        artigos = Artigo.objects.filter(vendedor=vendedor)

        contexto = {}
        contexto['lista_de_artigos'] = artigos.order_by("-data_de_criacao")
        contexto['vendedor'] = vendedor
        return contexto
