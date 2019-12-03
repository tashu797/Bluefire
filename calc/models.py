from django.db import models


class job(models.Model):

    job_title = models.CharField(max_length=50)
    job_department = models.CharField(max_length=100)
    job_loc = models.CharField(max_length=50, default=True)

    def __str__(self):
        return self.job_title + ' - ' + self.job_department + '-' + self.job_loc
