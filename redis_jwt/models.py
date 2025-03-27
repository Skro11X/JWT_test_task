from django.db import models


class ExampleContent(models.Model):
    content_for_both_roles = models.CharField(max_length=255)
    content_for_one_role = models.CharField(max_length=255)

