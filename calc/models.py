from django.db import models


class job_loc(models.Model):
    job_loc_title = models.CharField(max_length=50, default=True)
    job_loc_id = models.IntegerField(null=True)
    def __str__(self):
        return self.job_loc_title

class job_qual(models.Model):
    job_qual_title = models.CharField(max_length=50, default=True)
    job_loc_id=models.IntegerField(null=True)
    def __str__(self):
        return self.job_qual_title

class job(models.Model):
    job_title = models.CharField(max_length=50)
    job_department = models.CharField(max_length=100)
    job_loc = models.ForeignKey('job_loc', on_delete='')
    job_qual = models.ForeignKey('job_qual', on_delete='')
    job_id=models.IntegerField
    def __str__(self):
        return self.job_title + ' - ' + self.job_department
