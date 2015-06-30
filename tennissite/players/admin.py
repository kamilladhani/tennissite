from django.contrib import admin
from .models import Player, GrandSlam

# Register your models here.

class GrandSlamInline(admin.StackedInline):
	model = GrandSlam
	

class PlayerAdmin(admin.ModelAdmin):
	inlines = [GrandSlamInline]
	
	

admin.site.register(Player, PlayerAdmin)