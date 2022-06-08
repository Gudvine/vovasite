from ast import Or
from django.contrib import admin

from newApp.models import Score, Videomaker, Worktag, Order


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
	pass


@admin.register(Worktag)
class WorktagAdmin(admin.ModelAdmin):
	pass


@admin.register(Videomaker)
class VideomakerAdmin(admin.ModelAdmin):
	pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	pass
