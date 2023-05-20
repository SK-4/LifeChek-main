from django.db import models
import csv

class Question(models.Model):
    text = models.CharField(max_length=255)
    options = models.JSONField()
    correct_option = models.CharField(max_length=255)
    selected_option = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.text

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    relatives_number = models.CharField(max_length=20)



# with open('mental_health.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         question_text = row[0]
#         # Create a Question object and save it to the database
#         question = Question(text=question_text, options=["NOT AT ALL", "Several Days", "MORE THAN HALF THE DAYS", "NEARLY EVERY DAY"],selected_option=None)
#         question.save()
