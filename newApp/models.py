from django.db import models


class Score(models.Model):
	score_value = models.FloatField()


class Worktag(models.Model):
	tag_name = models.CharField(max_length=50)

	class Meta:
		unique_together = ("tag_name", )


class Videomaker(models.Model):
	first_name = models.CharField(max_length=40)
	last_name = models.CharField(max_length=40)
	free_status = models.BooleanField(default=True)
	# work_tag = models.ManyToManyField("Worktag", blank=True)
	work_tag = models.OneToOneField(Worktag, on_delete=models.CASCADE)
	score = models.OneToOneField(Score, on_delete=models.CASCADE, primary_key=True)

	class Meta:
		verbose_name_plural = "Videomakers"
