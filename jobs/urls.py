
from django.urls import path
from . import views


urlpatterns =[
    path('', views.alljobs, name='alljobs'),
    path('python/',views.pythonjobs, name='pythonjobs'),
    path('php/',views.phpjobs, name='phpjobs'),
    path('java/',views.javajobs, name='javajobs'),
    path('javascript/',views.javascriptjobs, name='javascriptjobs'),
    path('vb/',views.vbjobs, name='vbjobs'),
    path('<int:job_id>/',views.jobdetails, name='jobdetails'),

]