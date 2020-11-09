from django.db import models
from django.utils import timezone

import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField('date published')

    def __str__(self):
        return self.question_text

    # 是否在当前发布的问卷
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    # 注意要将外键写在‘多数’的一方
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

