from django.db import models


class Book(models.Model):
    book_id = models.IntegerField()
    title = models.TextField()
    sentence_count = models.IntegerField()
    text = models.TextField()
