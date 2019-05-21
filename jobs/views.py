from django.shortcuts import render,get_object_or_404
from .models import Job


def alljobs(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/home.html',{'jobs':jobs})


def pythonjobs(request):
    page_title = 'Python Projects'
    jobs = Job.objects.filter(languages__contains= 'Python')
    return render(request, 'jobs/jobfilter.html', {'page_title':page_title, 'jobs':jobs})


def phpjobs(request):
    page_title = 'PHP Projects'
    jobs = Job.objects.filter(languages__contains='PHP')
    return render(request, 'jobs/jobfilter.html', {'page_title':page_title, 'jobs':jobs})


def javajobs(request):
    page_title='Java Projects'
    jobs = Job.objects.filter(languages__contains='Java,')

    return render(request, 'jobs/jobfilter.html', {'page_title':page_title, 'jobs':jobs})


def vbjobs(request):
    page_title='VB.Net Projects'
    jobs = Job.objects.filter(languages__contains='Visual')
    return render(request, 'jobs/jobfilter.html', {'page_title':page_title, 'jobs':jobs})


def javascriptjobs(request):
    page_title = 'JavaScript Projects'
    jobs = Job.objects.filter(languages__contains='Script')
    return render(request, 'jobs/jobfilter.html', {'page_title':page_title, 'jobs':jobs})


def jobdetails(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/details.html', {'job':job})


