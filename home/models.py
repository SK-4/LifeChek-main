from django.db import models


class Question(models.Model):
    text = models.CharField(max_length=255)
    options = models.JSONField()
    correct_option = models.CharField(max_length=255)
    selected_option = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.text
    