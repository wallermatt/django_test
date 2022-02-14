import datetime
from django.apps import apps
from django.contrib import admin
from .models import Document, Organization, Verification


@admin.register(Verification)
class VerificationAdmin(admin.ModelAdmin):
    list_display = ("id", "organization", "client", "status_v2", "conv_created_at", "conv_updated_at", "get_document")
    list_filter = ("organization", "client")
    fieldsets = "extra_fieldsets"

    def extra_fieldsets(self):
        self.fieldsets = self.fieldsets + (
            ('Extra Fields', {'fields': ('client',)}),
        )
        return self.fieldsets
    
    @admin.display(ordering='organization__display_name', description='org_name')
    def get_org(self, obj):
        return obj.organization.display_name

    @admin.display(ordering='id', description='document')
    def get_document(self, obj):
        try:
            doc = Document.objects.get(verification_id=obj.id)
        except Document.DoesNotExist:
            doc = None
        return datetime.datetime.fromtimestamp(doc.created_at)

    @admin.display(ordering='created_at', description='created_at')
    def conv_created_at(self, obj):
        return datetime.datetime.fromtimestamp(obj.created_at)

    @admin.display(ordering='updated_at', description='updated_at')
    def conv_updated_at(self, obj):
        return datetime.datetime.fromtimestamp(obj.updated_at)

# Register your models here.
#admin.site.register(Organization)
models = apps.get_models()
for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

