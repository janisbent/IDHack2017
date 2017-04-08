from django.db import models

class Person(models.Model):
    CHILD = "CH"
    TEENAGER = "TE"
    YOUNG_ADULT = "YA"
    ADULT = "AD"
    OLD = "OL"

    AGE_CHOICES = (
        (CHILD, "Child"),
        (TEENAGER, "Teenager"),
        (YOUNG_ADULT, "Young Adult"),
        (ADULT, "Adult"),
        (OLD, "Elderly")
    )

    MALE="M"
    FEMALE="F"

    GENDER_CHOICES = (
        (MALE, "Male"),
        (FEMALE, "Female")
    )

    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=1000)
    age = models.CharField(max_length=2, choices=AGE_CHOICES, default=ADULT)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE)

class Relationship(models.Model):
    status = models.IntegerField(default=0)
    strength = models.IntegerField(default=0)
    person1 = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="rel1")
    person2 = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="rel2")
    details = models.TextField(max_length=500)
