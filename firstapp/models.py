from django.db import models

# Create your models here.

class Task(models.Model):
    task_id = models.IntegerField(verbose_name='任务ID')
    name = models.CharField(max_length=100,verbose_name='任务名称')

    class Meta:
        verbose_name_plural="任务"

    def __str__(self):
        return self.name

class Poem(models.Model):
    author = models.CharField(max_length=100,verbose_name='作者')
    title = models.CharField(max_length=100,verbose_name='诗名')

    class Meta:
        verbose_name_plural="诗书"

    def __str__(self):
        return self.title