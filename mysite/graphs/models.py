from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class NamedEntity(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=1000)

    class Meta:
        abstract = True

class Case(NamedEntity):
    pass

class Village(NamedEntity):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)

class Group(NamedEntity):
    village = models.ForeignKey(Village, on_delete=models.CASCADE, null=True)

class Person(NamedEntity):
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

    age = models.CharField(max_length=2, choices=AGE_CHOICES, default=ADULT)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE)
    village = models.ForeignKey(Village, on_delete=models.CASCADE, null=True)

class Relationship(models.Model):
    status = models.IntegerField(default=0)
    strength = models.IntegerField(default=0)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    objid1 = models.PositiveIntegerField(default=0)
    objid2 = models.PositiveIntegerField(default=0)
    endpt1 = GenericForeignKey('content_type', 'objid1')
    endpt2 = GenericForeignKey('content_type', 'objid2')
    details = models.TextField(max_length=500)
