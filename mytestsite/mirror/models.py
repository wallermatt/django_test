# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Account(models.Model):
    id = models.CharField(primary_key=True, max_length=99)
    created_at = models.BigIntegerField()
    first_time = models.BooleanField(blank=True, null=True)
    last_login_at = models.BigIntegerField()
    password = models.CharField(max_length=99)
    updated_at = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'account'


class AccountClientOrganization(models.Model):
    account = models.OneToOneField(Account, models.DO_NOTHING, primary_key=True)
    client = models.ForeignKey('Client', models.DO_NOTHING)
    organization = models.ForeignKey('Organization', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_client_organization'
        unique_together = (('account', 'client', 'organization'),)


class AccountEmail(models.Model):
    id = models.CharField(primary_key=True, max_length=99)
    account = models.ForeignKey(Account, models.DO_NOTHING)
    created_at = models.BigIntegerField()
    email = models.CharField(unique=True, max_length=99)
    status = models.SmallIntegerField()
    updated_at = models.BigIntegerField()
    verified = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_email'


class AccountOrganizationRole(models.Model):
    account = models.OneToOneField(Account, models.DO_NOTHING, primary_key=True)
    organization = models.ForeignKey('Organization', models.DO_NOTHING)
    role = models.ForeignKey('Role', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_organization_role'
        unique_together = (('account', 'organization', 'role'),)


class AccountProfile(models.Model):
    id = models.CharField(primary_key=True, max_length=99)
    account = models.ForeignKey(Account, models.DO_NOTHING)
    avatar = models.TextField(blank=True, null=True)
    full_name = models.CharField(max_length=99)
    phones = models.CharField(max_length=99, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_profile'


class AmlPassbase(models.Model):
    id = models.CharField(primary_key=True, max_length=99)
    verification = models.ForeignKey('Verification', models.DO_NOTHING)
    aml_response = models.TextField(blank=True, null=True)
    created_at = models.BigIntegerField()
    status = models.SmallIntegerField()
    status_by = models.CharField(max_length=99, blank=True, null=True)
    updated_at = models.BigIntegerField()
    manually_approved = models.BooleanField(blank=True, null=True)
    deleted_at = models.BigIntegerField(blank=True, null=True)
    status_v2 = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'aml_passbase'


class AmlSmartsearch(models.Model):
    id = models.CharField(primary_key=True, max_length=99)
    verification = models.ForeignKey('Verification', models.DO_NOTHING)
    aml_error_response = models.TextField(blank=True, null=True)
    aml_individual_uk_response = models.TextField(blank=True, null=True)
    completed = models.SmallIntegerField()
    created_at = models.BigIntegerField()
    status = models.SmallIntegerField()
    status_by = models.CharField(max_length=99, blank=True, null=True)
    updated_at = models.BigIntegerField()
    manually_approved = models.BooleanField(blank=True, null=True)
    deleted_at = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aml_smartsearch'


class AuditLog(models.Model):
    created_at = models.BigIntegerField()
    new_data = models.JSONField(blank=True, null=True)
    old_data = models.JSONField(blank=True, null=True)
    statement = models.CharField(max_length=99)
    table_name = models.CharField(max_length=99)

    class Meta:
        managed = False
        db_table = 'audit_log'


class Client(models.Model):
    id = models.CharField(primary_key=True, max_length=99)
    created_at = models.BigIntegerField()
    email = models.CharField(unique=True, max_length=99)
    last_login_at = models.BigIntegerField()
    password = models.CharField(max_length=99, blank=True, null=True)
    registration_code = models.CharField(max_length=99, blank=True, null=True)
    self_verified = models.BooleanField(blank=True, null=True)
    updated_at = models.BigIntegerField()

    def __str__(self):
        return "{}".format(self.email)

    class Meta:
        managed = False
        db_table = 'client'


class ClientCompany(models.Model):
    client = models.OneToOneField(Client, models.DO_NOTHING, primary_key=True)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    position = models.CharField(max_length=99)

    class Meta:
        managed = False
        db_table = 'client_company'
        unique_together = (('client', 'company'),)


class ClientProfile(models.Model):
    id = models.CharField(primary_key=True, max_length=99)
    client = models.OneToOneField(Client, models.DO_NOTHING)
    full_name = models.CharField(max_length=99)
    phones = models.CharField(max_length=99, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client_profile'


class Company(models.Model):
    id = models.CharField(primary_key=True, max_length=99)
    created_at = models.BigIntegerField()
    display_name = models.CharField(max_length=99)
    registration_number = models.CharField(max_length=99, blank=True, null=True)
    updated_at = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'company'


class CompanyOrganization(models.Model):
    company = models.OneToOneField(Company, models.DO_NOTHING, primary_key=True)
    organization = models.ForeignKey('Organization', models.DO_NOTHING)
    position = models.CharField(max_length=99)

    class Meta:
        managed = False
        db_table = 'company_organization'
        unique_together = (('company', 'organization'),)


class Customer(models.Model):
    id = models.CharField(primary_key=True, max_length=99)
    organization = models.ForeignKey('Organization', models.DO_NOTHING)
    card_brand = models.CharField(max_length=99, blank=True, null=True)
    client_secret = models.CharField(max_length=99, blank=True, null=True)
    created_at = models.BigIntegerField()
    email = models.CharField(max_length=99)
    extended_aml_billing_period = models.BigIntegerField()
    last4 = models.CharField(max_length=99, blank=True, null=True)
    latest_invoice_id = models.CharField(max_length=99, blank=True, null=True)
    payment_method_id = models.CharField(max_length=99, blank=True, null=True)
    payment_status = models.CharField(max_length=99, blank=True, null=True)
    plan = models.CharField(max_length=99, blank=True, null=True)
    status = models.CharField(max_length=99, blank=True, null=True)
    subscription_extended_aml_item_id = models.CharField(max_length=99, blank=True, null=True)
    subscription_id = models.CharField(max_length=99, blank=True, null=True)
    subscription_item_id = models.CharField(max_length=99, blank=True, null=True)
    subscription_period_ends = models.BigIntegerField()
    updated_at = models.BigIntegerField()
    verifications_billing_period = models.BigIntegerField()
    invoice_billing = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class CustomerDiscounts(models.Model):
    customer = models.OneToOneField(Customer, models.DO_NOTHING)
    date_from = models.DateField()
    date_to = models.DateField()
    discount = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_discounts'


class Document(models.Model):
    id = models.CharField(primary_key=True, max_length=99)
    verification = models.ForeignKey('Verification', models.DO_NOTHING)
    completed = models.BooleanField(blank=True, null=True)
    created_at = models.BigIntegerField()
    document_type = models.CharField(max_length=99)
    status = models.SmallIntegerField()
    status_by = models.CharField(max_length=99, blank=True, null=True)
    type_explanation = models.CharField(max_length=99, blank=True, null=True)
    updated_at = models.BigIntegerField()
    manually_approved = models.BooleanField(blank=True, null=True)
    deleted_at = models.BigIntegerField(blank=True, null=True)
    status_v2 = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'document'


class DocumentData(models.Model):
    id = models.CharField(primary_key=True, max_length=99)
    document = models.ForeignKey(Document, models.DO_NOTHING)
    chain = models.TextField(blank=True, null=True)
    content_length = models.BigIntegerField(blank=True, null=True)
    content_type = models.CharField(max_length=99, blank=True, null=True)
    cookies = models.TextField(blank=True, null=True)
    created_at = models.BigIntegerField()
    file_category = models.CharField(max_length=99, blank=True, null=True)
    key = models.CharField(max_length=99, blank=True, null=True)
    name = models.CharField(max_length=99, blank=True, null=True)
    score = models.SmallIntegerField()
    screenshot = models.CharField(max_length=99, blank=True, null=True)
    updated_at = models.BigIntegerField()
    url = models.TextField(blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'document_data'


class Idv(models.Model):
    id = models.CharField(primary_key=True, max_length=99)
    verification = models.ForeignKey('Verification', models.DO_NOTHING)
    completed = models.BooleanField(blank=True, null=True)
    created_at = models.BigIntegerField()
    status = models.SmallIntegerField()
    status_by = models.CharField(max_length=99, blank=True, null=True)
    updated_at = models.BigIntegerField()
    manually_approved = models.BooleanField(blank=True, null=True)
    deleted_at = models.BigIntegerField(blank=True, null=True)
    status_v2 = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'idv'


class IdvData(models.Model):
    id = models.CharField(primary_key=True, max_length=99)
    idv = models.ForeignKey(Idv, models.DO_NOTHING)
    created_at = models.BigIntegerField()
    idv_key = models.TextField(blank=True, null=True)
    idv_response = models.TextField(blank=True, null=True)
    nfc_data = models.TextField(blank=True, null=True)
    score = models.SmallIntegerField()
    updated_at = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'idv_data'


class Invitation(models.Model):
    id = models.CharField(primary_key=True, max_length=99)
    organization = models.ForeignKey('Organization', models.DO_NOTHING)
    created_at = models.BigIntegerField()
    email = models.CharField(max_length=99)
    updated_at = models.BigIntegerField()
    status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'invitation'
        unique_together = (('organization', 'email'),)


class InvitationLink(models.Model):
    id = models.CharField(primary_key=True, max_length=99)
    organization = models.OneToOneField('Organization', models.DO_NOTHING)
    created_at = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'invitation_link'


class Organization(models.Model):
    id = models.CharField(primary_key=True, max_length=99)
    created_at = models.BigIntegerField()
    display_name = models.CharField(max_length=99)
    logo = models.TextField(blank=True, null=True)
    updated_at = models.BigIntegerField()

    def __str__(self):
        return "{}".format(self.display_name)

    class Meta:
        managed = False
        db_table = 'organization'


class Role(models.Model):
    name = models.CharField(max_length=99)

    class Meta:
        managed = False
        db_table = 'role'


class SchemaMigrations(models.Model):
    version = models.BigIntegerField(primary_key=True)
    dirty = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'schema_migrations'


class Verification(models.Model):
    id = models.CharField(primary_key=True, max_length=99)
    account = models.ForeignKey(Account, models.DO_NOTHING)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    organization = models.ForeignKey(Organization, models.DO_NOTHING)
    created_at = models.BigIntegerField()
    organization_notified = models.BooleanField(blank=True, null=True)
    status = models.SmallIntegerField()
    updated_at = models.BigIntegerField()
    status_v2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    deleted_at = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'verification'


class VerificationReminder(models.Model):
    id = models.CharField(primary_key=True, max_length=99)
    verification = models.ForeignKey(Verification, models.DO_NOTHING)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    created_at = models.BigIntegerField()
    sent_by = models.ForeignKey(Account, models.DO_NOTHING, db_column='sent_by')

    class Meta:
        managed = False
        db_table = 'verification_reminder'
