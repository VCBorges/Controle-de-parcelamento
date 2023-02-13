from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView
from django.contrib import messages

from controle_parcelamento.forms import *
from controle_parcelamento.models import *



class HomeTemplateView(TemplateView):
    
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super(HomeTemplateView, self).get_context_data(**kwargs)
        context['form'] = CreateClienteForm()
        context['form2'] = CreateVendasForm()
        # context['cliente'] = Cliente.objects.all()
        return context
    
class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente_list.html'
    context_object_name = 'clientes'
    
    def get_context_data(self, **kwargs):
        context = super(ClienteListView, self).get_context_data(**kwargs)
        context['cliente'] = Cliente.objects.all()
        return context
    

class VendasListView(ListView):
    model = Vendas
    template_name = 'vendas_list.html'
    context_object_name = 'vendas'
    
    def get_context_data(self, **kwargs):
        context = super(VendasListView, self).get_context_data(**kwargs)
        context['vendas'] = Vendas.objects.all()
        return context
    

class ParcelasListView(ListView):
    model = Parcelas
    template_name = 'parcela_list.html'
    context_object_name = 'parcelas'
    
    def get_context_data(self, **kwargs):
        context = super(ParcelasListView, self).get_context_data(**kwargs)
        context['parcelas'] = Parcelas.objects.all()
        return context
    
    
class CreateClienteView(CreateView):
    model = Cliente
    form_class = CreateClienteForm
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        messages.success(self.request, 'Cliente cadastrado com sucesso!', extra_tags='cliente')
        return super().form_valid(form)
    
    def form_invalid(self, form: CreateClienteForm):
        messages.error(self.request, 'Houve um erro ao cadastrar o cliente!', extra_tags='cliente')
        return redirect('home')

    
class CreateVendasView(CreateView):
    model = Vendas
    form_class = CreateVendasForm
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        print(form)
        messages.success(self.request, 'Venda cadastrado com sucesso!', extra_tags='venda')
        return super().form_valid(form)
    
    def form_invalid(self, form: CreateVendasForm):
        print(form)
        print('EXECUTANDO FORM INVALID')
        messages.error(self.request, 'Houve um erro ao cadastrar a venda!', extra_tags='venda')
        return redirect('home')



class UpdateClienteView(UpdateView):
    model = Cliente
    form_class = UpdateClienteForm
    template_name = 'cliente_update.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        messages.success(self.request, 'Cliente atualizado com sucesso!', extra_tags='cliente')
        return super().form_valid(form)
    
    def form_invalid(self, form: CreateClienteForm):
        messages.error(self.request, 'Houve um erro ao atualizar o cliente!', extra_tags='cliente')
        return redirect('home')
    
    

class UpdateVendasView(UpdateView):
    model = Vendas
    form_class = UpdateVendasForm
    template_name = 'vendas_update.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        messages.success(self.request, 'Venda atualizada com sucesso!', extra_tags='venda')
        return super().form_valid(form)
    
    def form_invalid(self, form: CreateVendasForm):
        messages.error(self.request, 'Houve um erro ao atualizar a venda!', extra_tags='venda')
        return redirect('home')
    

class UpdateParcelasView(UpdateView):
    model = Parcelas
    form_class = UpdateParcelasForm
    template_name = 'parcela_update.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        messages.success(self.request, 'Parcela atualizada com sucesso!', extra_tags='parcela')
        return super().form_valid(form)
    
    def form_invalid(self, form: UpdateParcelasForm):
        messages.error(self.request, 'Houve um erro ao atualizar a parcela!', extra_tags='parcela')
        return redirect('home')
