from django.db import models

# Create your models here.
class question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField("Date published")


class choice(models.Model):
    question=models.ForeignKey(question,on_delete=models.CASCADE)
    choce_test=models.CharField(max_length=100)
    voters=models.IntegerField(default=0)