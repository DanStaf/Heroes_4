from django.contrib import admin
from heroes.models import Parent, Hero, Team, Program

# Register your models here.

admin.site.register(Parent)
admin.site.register(Hero)
admin.site.register(Team)
admin.site.register(Program)
