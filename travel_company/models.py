from django.db import models
from django.core.exceptions import ValidationError

class Person(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Horse(models.Model):
    name = models.CharField(max_length=100)
    owner = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        related_name='horse'
    )

    def __str__(self):
        return f"{self.name} --- {self.owner}"

class TourCompany(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    companies = models.ManyToManyField(TourCompany, blank=True, related_name='services')

    def __str__(self):
        companies = ", ".join(i.name for i in self.companies.all())
        return f"{self.name} --- {companies}"

class Review(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    company = models.ForeignKey(
        TourCompany,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    MARKS = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )

    marks = models.IntegerField(
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.marks < 1 or self.marks > 5:
            raise ValidationError("Оценка только от 1 до 5")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.person} --- {self.company} --- {self.marks}"