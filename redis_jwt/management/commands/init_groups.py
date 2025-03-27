from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission, ContentType


class Command(BaseCommand):
    help = "Создает группу у которой будет особый доступ"

    def handle(self, *args, **kwargs):
        special_group, group_created = Group.objects.get_or_create(name="special_group")
        content_types = ContentType.objects.filter(app_label="redis_jwt")
        for content_type in content_types:
            permission, permission_created = Permission.objects.get_or_create(codename="get_special_content",
                                                                              content_type=content_type,
                                                                              name="Add special field from model")
            if group_created and permission_created:
                special_group.permissions.add(permission)
