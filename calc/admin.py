from django.contrib import admin
from .models import job, job_loc, job_qual

admin.site.register(job)
admin.site.register(job_loc)
admin.site.register(job_qual)


