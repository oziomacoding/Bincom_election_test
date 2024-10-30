# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.

# from django.db import models
# from django.contrib.auth.models import User, Group, Permission
# from django.contrib.contenttypes.models import ContentType


# class Agent(models.Model):
#     id = models.AutoField(primary_key=True)
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email = models.EmailField(blank=True, null=True)
#     phone = models.CharField(max_length=13)
#     polling_unit_id = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'agentname'


# class LgaResult(models.Model):
#     id = models.AutoField(primary_key=True)
#     lga_name = models.CharField(max_length=50)
#     party_abbreviation = models.CharField(max_length=4)
#     party_score = models.IntegerField()
#     entered_by_user = models.CharField(max_length=50)
#     date_entered = models.DateTimeField()
#     user_ip_address = models.GenericIPAddressField()

#     class Meta:
#         managed = False
#         db_table = 'announced_lga_results'


# class AnnouncedPuResults(models.Model):
#     id = models.AutoField(primary_key=True)
#     polling_unit_id = models.CharField(max_length=50)
#     party_abbreviation = models.CharField(max_length=4)
#     party_score = models.IntegerField()
#     entered_by_user = models.CharField(max_length=50)
#     date_entered = models.DateTimeField()
#     user_ip_address = models.GenericIPAddressField()

#     class Meta:
#         managed = False
#         db_table = 'announced_pu_results'


# class StateResult(models.Model):
#     id = models.AutoField(primary_key=True)
#     state_name = models.CharField(max_length=50)
#     party_abbreviation = models.CharField(max_length=4)
#     party_score = models.IntegerField()
#     entered_by_user = models.CharField(max_length=50)
#     date_entered = models.DateTimeField()
#     user_ip_address = models.GenericIPAddressField()

#     class Meta:
#         managed = False
#         db_table = 'announced_state_results'


# class WardResult(models.Model):
#     id = models.AutoField(primary_key=True)
#     ward_name = models.CharField(max_length=50)
#     party_abbreviation = models.CharField(max_length=4)
#     party_score = models.IntegerField()
#     entered_by_user = models.CharField(max_length=50)
#     date_entered = models.DateTimeField()
#     user_ip_address = models.GenericIPAddressField()

#     class Meta:
#         managed = False
#         db_table = 'announced_ward_results'


# # Remove custom models that conflict with Django's built-in models
# # class AdminLog(models.Model):
# #     action_time = models.DateTimeField()
# #     object_id = models.TextField(blank=True, null=True)
# #     object_repr = models.CharField(max_length=200)
# #     action_flag = models.PositiveSmallIntegerField()
# #     change_message = models.TextField()
# #     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
# #     user = models.ForeignKey(User, on_delete=models.CASCADE)

# #     class Meta:
# #         db_table = 'django_admin_log'


# # class ContentType(models.Model):
# #     app_label = models.CharField(max_length=100)
# #     model = models.CharField(max_length=100)

# #     class Meta:
# #         db_table = 'django_content_type'
# #         unique_together = (('app_label', 'model'),)


# # class Session(models.Model):
# #     session_key = models.CharField(primary_key=True, max_length=40)
# #     session_data = models.TextField()
# #     expire_date = models.DateTimeField()

# #     class Meta:
# #         db_table = 'django_session'


# class Lga(models.Model):
#     id = models.AutoField(primary_key=True)
#     lga_id = models.IntegerField()
#     name = models.CharField(max_length=50)
#     state_id = models.IntegerField()
#     description = models.TextField(blank=True, null=True)
#     entered_by_user = models.CharField(max_length=50)
#     date_entered = models.DateTimeField()
#     user_ip_address = models.GenericIPAddressField()

#     class Meta:
#         managed = False
#         db_table = 'lga'


# class Party(models.Model):
#     id = models.CharField(max_length=11, primary_key=True)
#     name = models.CharField(max_length=11)

#     class Meta:
#         managed = False
#         db_table = 'party'


# class PollingUnit(models.Model):
#     id = models.AutoField(primary_key=True)
#     polling_unit_id = models.IntegerField()
#     ward_id = models.IntegerField()
#     lga_id = models.IntegerField()
#     ward_unique_id = models.IntegerField(blank=True, null=True)
#     number = models.CharField(max_length=50, blank=True, null=True)
#     name = models.CharField(max_length=50, blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     latitude = models.CharField(max_length=255, blank=True, null=True)
#     longitude = models.CharField(max_length=255, blank=True, null=True)
#     entered_by_user = models.CharField(max_length=50, blank=True, null=True)
#     date_entered = models.DateTimeField(blank=True, null=True)
#     user_ip_address = models.GenericIPAddressField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'polling_unit'


# class State(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=50)

#     class Meta:
#         managed = False
#         db_table = 'states'


# class Ward(models.Model):
#     id = models.AutoField(primary_key=True)
#     ward_id = models.IntegerField()
#     name = models.CharField(max_length=50)
#     lga_id = models.IntegerField()
#     description = models.TextField(blank=True, null=True)
#     entered_by_user = models.CharField(max_length=50)
#     date_entered = models.DateTimeField()
#     user_ip_address = models.GenericIPAddressField()

#     class Meta:
#         managed = False
#         db_table = 'ward'

from django.db import models

# Create your models here.

class AnnouncedPuResults(models.Model):
    result_id = models.AutoField(primary_key=True)
    polling_unit_uniqueid = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'announced_pu_results'


class PollingUnit(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    polling_unit_id = models.IntegerField()
    ward_id = models.IntegerField()
    lga_id = models.IntegerField()
    uniquewardid = models.IntegerField(blank=True, null=True)
    polling_unit_number = models.CharField(max_length=50, blank=True, null=True)
    polling_unit_name = models.CharField(max_length=50, blank=True, null=True)
    polling_unit_description = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=255, blank=True, null=True)
    long = models.CharField(max_length=255, blank=True, null=True)
    entered_by_user = models.CharField(max_length=50, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    user_ip_address = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'polling_unit'