# -*- coding: UTF-8 -*-
from django.db import models

class PublishedManager(models.Manager):
    def get_query_set(self):
        return super(PublishedManager, self).get_query_set().filter(is_public=True)

class Guestbook(models.Model):
	name = models.CharField(max_length=70)
	email = models.EmailField(blank=True, null=True)
	webpage = models.URLField(blank=True, null=True)
	message = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	is_public = models.BooleanField()

	objects = models.Manager()
	published = PublishedManager()

	class Meta:
		verbose_name = "Guestbook"
		verbose_name_plural = "Guestbooks"
		ordering = ['-created']

	def publish(self):
		self.is_public = True
		return self.save()

	def unpublish(self):
		self.is_public = False
		return self.save()

	@models.permalink
	def get_absolute_url(self):
		return ('list_guestbook',)