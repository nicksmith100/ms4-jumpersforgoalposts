from django.db import models


class Faq(models.Model):

    question = models.CharField(max_length=254)
    answer = models.TextField()

    def __str__(self):
        return self.question