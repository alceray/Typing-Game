from django.db import models
from django.contrib.auth.models import User

class Test(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    content = models.TextField()
    final_wpm = models.DecimalField(max_digits=5, decimal_places=2)
    final_accuracy = models.DecimalField(max_digits=5, decimal_places=2)
    final_consistency = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class TestSnapshot(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    wpm = models.DecimalField(max_digits=5, decimal_places=2)
    accuracy = models.DecimalField(max_digits=5, decimal_places=2)
    consistency = models.DecimalField(max_digits=5, decimal_places=2)
    total_characters_typed = models.PositiveIntegerField()

class Mistake(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    incorrect_char = models.CharField(max_length=1)
    correct_char = models.CharField(max_length=1)
    position = models.PositiveIntegerField()

class Speed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    average_wpm = models.DecimalField(max_digits=5, decimal_places=2)
