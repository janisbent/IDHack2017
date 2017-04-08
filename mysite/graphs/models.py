from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class NamedEntity(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=1000, blank=True)

    class Meta:
        abstract = True

class Case(NamedEntity):
    pass

class Village(NamedEntity):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name="villages")

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
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class RelationshipBase(models.Model):
    POSITIVE = "PS"
    NEGATIVE = "NG"
    NEUTRAL = "NT"

    STATUS_CHOICES = (
        (POSITIVE, "Positive"),
        (NEGATIVE, "Negative"),
        (NEUTRAL, "Neutral")
    )

    status = models.CharField(choices=STATUS_CHOICES, max_length=2, default=NEUTRAL)
    strength = models.IntegerField(default=0)
    details = models.TextField(max_length=500, blank=True)

    class Meta:
        abstract = True

class GroupRelationship(RelationshipBase):
    g1 = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="rel1")
    g2 = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="rel2")

class PersonRelationship(RelationshipBase):
    p1 = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="rel1")
    p2 = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="rel2")
