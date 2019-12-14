from django.shortcuts import render
from .models import job, job_qual, job_loc


def home_view(request):
    jobs = job.objects.all()
    a = job_qual.objects.all()
    b = job_loc.objects.all()

    return render(request, "home.html", {'a': a, 'b': b, 'jobs':jobs})

def res_view(request):
    jobs = job.objects.all()
    a = job_qual.objects.all()
    b = job_loc.objects.all()

    return render(request, "result.html", {'a': a, 'b': b, 'jobs': jobs})




