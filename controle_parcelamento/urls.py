from django.contrib import admin
from django.urls import path, include

from controle_parcelamento.views import *



urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    
    path('cliente-detail/<str:pk>/', ClienteDetailView.as_view(), name='detail_cliente'),

    path('cliente-list/', ClienteListView.as_view(), name='cliente_list'),
    path('vendas-list/', VendasListView.as_view(), name='vendas_list'),
    path('parcelas-list/', ParcelasListView.as_view(), name='parcelas_list'),
    
    path('create-cliente/', CreateClienteView.as_view(), name='create_cliente'),
    path('create-vendas/', CreateVendasView.as_view(), name='create_vendas'),
    
    path('cliente-update/<str:pk>/', UpdateClienteView.as_view(), name='update_cliente'),
    path('vendas-update/<str:pk>/', UpdateVendasView.as_view(), name='update_venda'),
    path('parcela-update/<str:pk>/', UpdateParcelasView.as_view(), name='update_parcela'),
    
    path('cliente-delete/<str:pk>/', DeleteClienteView.as_view(), name='delete_cliente'),
]