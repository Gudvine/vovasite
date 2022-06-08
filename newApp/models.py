from django.db import models


class Score(models.Model):
	score_value = models.FloatField()


class Worktag(models.Model):
	tag_name = models.CharField(max_length=50)

	class Meta:
		unique_together = ("tag_name", )


#class Portfolio(models.Model):
#	description = models.CharField(max_length=256, default='')
#	video_link = models.CharField(max_length=256, default='')


class Videomaker(models.Model):
	first_name = models.CharField(max_length=40)
	last_name = models.CharField(max_length=40)
	free_status = models.BooleanField(default=True)
	experience_level = models.CharField(max_length=2)
	phone_number = models.CharField(max_length=12)
	maker_mail = models.EmailField(max_length=200)
	city = models.CharField(max_length=15)
	service_price = models.IntegerField(default=0)
	work_tag = models.OneToOneField(Worktag, on_delete=models.CASCADE)
	#portfolio = models.OneToOneField(Portfolio, on_delete=models.CASCADE, blank=True, null=True)
	score = models.OneToOneField(Score, on_delete=models.CASCADE, primary_key=True)
	telegram_link = models.CharField(max_length=256)

	class Meta:
		verbose_name_plural = "Videomakers"


class Order(models.Model):
	maker = models.OneToOneField(Videomaker, on_delete=models.CASCADE)
	time_days = models.IntegerField(default=0)
