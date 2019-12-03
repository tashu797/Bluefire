from django.shortcuts import render
from .models import job


def home_view(request):
    item = job.objects.get(id=3)
    a = {
        'title': item.job_title,
        'dept': item.job_department,
        'loc': item.job_loc
        }

    return render(request, "home.html", a)





