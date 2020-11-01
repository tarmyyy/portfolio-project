from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length=50)
	pub_date = models.DateTimeField(auto_now=False,auto_now_add=False)
	image = models.ImageField(upload_to='images/')
	body = models.TextField()

	def __str__(self):
		return self.title

	def summary(self):
		return self.body[:100]

	def pub_date_short(self):
		return self.pub_date.strftime("%b %e %Y")