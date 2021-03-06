from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify


class Post(models.Model):
	STATUS_CHOICES = (
			('draft', 'DRAFT'),
			('published', 'PUBLISHED'),
		)

	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=120)
	author = models.ForeignKey(User, related_name='blog_posts', on_delete='CASCADE')
	body = models.TextField()
	image = models.ImageField(upload_to='post', blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("blog:post_detail", args=[self.id, self.slug])

@receiver(pre_save, sender=Post)
def pre_save_slug(sender, **kwargs):
	slug = slugify(kwargs['instance'].title)
	kwargs['instance'].slug = slug


