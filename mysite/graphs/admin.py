from django.contrib import admin

from .models import Person
from .models import Village
from .models import Case
from .models import Group
from .models import GroupRelationship
from .models import PersonRelationship

admin.site.register(Person)
admin.site.register(Village)
admin.site.register(Case)
admin.site.register(Group)
admin.site.register(GroupRelationship)
admin.site.register(PersonRelationship)
