from django.contrib.auth.models import User
from django.db import models

class Question(models.Model):
    question = models.TextField(max_length=500)
    asked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    asked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer = models.TextField(max_length=1000)
    answered_by = models.ForeignKey(User, on_delete = models.CASCADE)
    answered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.answer

