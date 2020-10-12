from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length=50)
	pub_date = models.DateTimeField(auto_now=False,auto_now_add=False)
	image = models.ImageField(upload_to='images/')
	body = models.TextField()
# Create a Blog model
#   Blog fields
#     title
#     pub_date
#     body
#     image
# add a Blog app to the settings
# create a migration
# run migrations
# add to the Admin
