from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, View, ListView

from analises.forms import *
from analises.models import *
from core.views import *



class AnalisesTemplateView(TemplateView):
    
    template_name = 'analises/analises_page.html'
    
    def get_context_data(self, **kwargs):
        context = super(AnalisesTemplateView, self).get_context_data(**kwargs)
        context['form'] = CreateAnaliseForm()
        context['analises'] = Analises.objects.all()
        return context
    
    

class AnalisesCreateView(FormSubmissionMixin, View):
    
    form_class = CreateAnaliseForm
    success_message = 'Analise cadastrada com sucesso!'
    error_message = 'Erro ao cadastrar analise!'
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
    

class AnelisesListView(ListView):
    
    model = Analises
    template_name = 'analises/analises_list.html'
    context_object_name = 'analises'
    
    def get_context_data(self, **kwargs):
        context = super(AnelisesListView, self).get_context_data(**kwargs)
        # context['analises'] = Analises.objects.all()
        print(Analises.objects.all())
        return context