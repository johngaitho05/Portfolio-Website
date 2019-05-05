
from django.urls import path
from . import views


urlpatterns =[
    path('', views.contactpage, name='contactpage'),
    path('sendmessage/', views.savemessage, name='savemessage'),
]