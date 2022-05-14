from django.contrib import admin

from newApp.models import Score, Videomaker, Worktag


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
	pass


@admin.register(Worktag)
class WorktagAdmin(admin.ModelAdmin):
	pass


@admin.register(Videomaker)
class VideomakerAdmin(admin.ModelAdmin):
	pass
