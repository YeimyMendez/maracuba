from django.urls import path
from . import views



urlpatterns =[
    #path('contacto', views.contacto, name="Contacto"),
    path('', views.pdf_view, name='pdf_view'),
]
