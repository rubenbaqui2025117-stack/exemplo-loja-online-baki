from django.urls import path

from . import views
from django.urls import path

from . import views

app_name = "loja"
urlpatterns = [
    # ex: /
    path("", views.IndexView.as_view(), name="index"),
    # ex: /artigo/5/
    path("artigo/<int:pk>/", views.ArtigoView.as_view(), name="artigo"),
    # ex: /vendedor/5/
    path("vendedor/<int:pk>/", views.VendedorView.as_view(), name="vendedor"),
    # ex: /categoria/5/
    path("categoria/<int:pk>/", views.CategoriaView.as_view(), name="categoria"),
]