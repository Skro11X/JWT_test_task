from django.contrib import admin
from redis_jwt.models import ExampleContent

@admin.register(ExampleContent)
class ExampleContentAdmin(admin.ModelAdmin):
    pass


