from django.contrib import admin
from heroes.models import Parent, Hero, ParentStatus, HeroStatus

# Register your models here.

admin.site.register(Parent)
admin.site.register(Hero)
admin.site.register(ParentStatus)
admin.site.register(HeroStatus)
