import datetime
from django.apps import apps
from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

from .models import Document, Organization, Verification, Idv, AmlPassbase, DocumentData, IdvData


@admin.register(Verification)
class VerificationAdmin(admin.ModelAdmin):
    list_display = ("id", "organization", "client", "status_v2", "conv_created_at", "conv_updated_at", "get_document", "get_idv", "get_aml_passbase")
    list_display_links = ("id",)
    list_filter = ("organization", "client")
    
    @admin.display(ordering='organization__display_name', description='org_name')
    def get_org(self, obj):
        return obj.organization.display_name

    @admin.display(ordering='id', description='documents')
    def get_document(self, obj):
        try:
            doc = Document.objects.filter(verification_id=obj.id)
            url = reverse('admin:{}_{}_changelist'.format(obj._meta.app_label, "document"))
            return format_html("<a href='{}?verification__id__exact={}'>{}</a>", url, obj.id, doc.count())
        except Document.DoesNotExist:
            return None

    @admin.display(ordering='id', description='idv')
    def get_idv(self, obj):
        try:
            idv = Idv.objects.filter(verification_id=obj.id)
            url = reverse('admin:{}_{}_changelist'.format(obj._meta.app_label, "idv"))
            return format_html("<a href='{}?verification__id__exact={}'>{}</a>", url, obj.id, idv.count())
        except Idv.DoesNotExist:
            return None

    @admin.display(ordering='id', description='aml_passbase')
    def get_aml_passbase(self, obj):
        try:
            apb = AmlPassbase.objects.filter(verification_id=obj.id)
            url = reverse('admin:{}_{}_changelist'.format(obj._meta.app_label, "amlpassbase"))
            return format_html("<a href='{}?verification__id__exact={}'>{}</a>", url, obj.id, apb.count())
        except AmlPassbase.DoesNotExist:
            return None

    @admin.display(ordering='created_at', description='created_at')
    def conv_created_at(self, obj):
        return datetime.datetime.fromtimestamp(obj.created_at)

    @admin.display(ordering='updated_at', description='updated_at')
    def conv_updated_at(self, obj):
        return datetime.datetime.fromtimestamp(obj.updated_at)


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("id", "verification", "status_v2", "conv_created_at", "conv_updated_at", "get_document_data")
    list_display_links = ("id",)

    @admin.display(ordering='id', description='data')
    def get_document_data(self, obj):
        try:
            dd = DocumentData.objects.filter(document_id=obj.id)
            url = reverse('admin:{}_{}_changelist'.format(obj._meta.app_label, "documentdata"))
            return format_html("<a href='{}?document__id__exact={}'>{}</a>", url, obj.id, dd.count())
        except DocumentData.DoesNotExist:
            return None

    @admin.display(ordering='created_at', description='created_at')
    def conv_created_at(self, obj):
        return datetime.datetime.fromtimestamp(obj.created_at)

    @admin.display(ordering='updated_at', description='updated_at')
    def conv_updated_at(self, obj):
        return datetime.datetime.fromtimestamp(obj.updated_at)


@admin.register(DocumentData)
class DocumentDataAdmin(admin.ModelAdmin):
    list_display = ("get_id", "document", "conv_created_at", "conv_updated_at", "score")

    @admin.display(ordering='id', description='id')
    def get_id(self, obj):
        url = reverse('admin:{}_{}_change'.format(obj._meta.app_label, "documentdata"), args=(obj.id,))
        return format_html("<a href='{}'>{}</a>", url, obj.id)

    @admin.display(ordering='created_at', description='created_at')
    def conv_created_at(self, obj):
        return datetime.datetime.fromtimestamp(obj.created_at)

    @admin.display(ordering='updated_at', description='updated_at')
    def conv_updated_at(self, obj):
        return datetime.datetime.fromtimestamp(obj.updated_at)


@admin.register(AmlPassbase)
class AmlPassbaseAdmin(admin.ModelAdmin):
    list_display = ("id", "verification", "conv_created_at", "conv_updated_at", "status_v2")
    list_display_links = ("id",)

    @admin.display(ordering='created_at', description='created_at')
    def conv_created_at(self, obj):
        return datetime.datetime.fromtimestamp(obj.created_at)

    @admin.display(ordering='updated_at', description='updated_at')
    def conv_updated_at(self, obj):
        return datetime.datetime.fromtimestamp(obj.updated_at)


@admin.register(Idv)
class IdvAdmin(admin.ModelAdmin):
    list_display = ("id", "verification", "status_v2", "conv_created_at", "conv_updated_at", "get_idv_data")
    list_display_links = ("id",)

    @admin.display(ordering='id', description='data')
    def get_idv_data(self, obj):
        try:
            id = IdvData.objects.filter(idv_id=obj.id)
            url = reverse('admin:{}_{}_changelist'.format(obj._meta.app_label, "idvdata"))
            return format_html("<a href='{}?idv__id__exact={}'>{}</a>", url, obj.id, id.count())
        except IdvData.DoesNotExist:
            return None

    @admin.display(ordering='created_at', description='created_at')
    def conv_created_at(self, obj):
        return datetime.datetime.fromtimestamp(obj.created_at)

    @admin.display(ordering='updated_at', description='updated_at')
    def conv_updated_at(self, obj):
        return datetime.datetime.fromtimestamp(obj.updated_at)


@admin.register(IdvData)
class IdvDataAdmin(admin.ModelAdmin):
    list_display = ("id", "idv", "conv_created_at", "conv_updated_at", "score")
    list_display_links = ("id",)

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

