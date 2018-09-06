# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Books(models.Model):
	name = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	author = models.CharField(max_length=200)
	image = models.CharField(max_length=400, 
		blank=True,
		null=True
	)

	def __str__(self):
		return self.name + " | " + self.author

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)