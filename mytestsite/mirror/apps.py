from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig

class MirrorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mirror'

class MirrorAdminConfig(AdminConfig):
    default_site = 'mirror.admin.get_mirror_admin_site'
