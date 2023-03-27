from django.urls import path, include

from analises.views import *



urlpatterns = [
    path('analises/', AnalisesTemplateView.as_view(), name='analises_page'),
    path('create-analise/', AnalisesCreateView.as_view(), name='create_analise'),
    path('analises-list/', AnelisesListView.as_view(), name='analises_list'),
]