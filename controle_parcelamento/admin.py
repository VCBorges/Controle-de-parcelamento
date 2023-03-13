from django.contrib import admin
from .models import Cliente, Vendas, Parcelas

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Vendas)
admin.site.register(Parcelas)