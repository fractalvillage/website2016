from django.db import models
from django.contrib.auth.models import User

MAP_ADDRESS_LENGTH = 16
PHONENO_LENGTH = 16
NAME_LENGTH = 50
SHORT_DESCRIPTION_LENGTH = 256
URL_LENGTH = 256
EMAIL_LENGTH = 256
LONG_DESCRIPTION_LENGTH = 1000

# Create your models here.

class Village(models.Model):
    village_name_he = models.CharField(max_length=NAME_LENGTH, unique=True)
    village_name_en = models.CharField(max_length=NAME_LENGTH, unique=True)
    village_facebook_link = models.CharField(max_length=URL_LENGTH)
    village_slack_link = models.CharField(max_length=URL_LENGTH)
    village_email = models.CharField(max_length=EMAIL_LENGTH)

class VillageDocs(models.Model):
    doc_title = models.CharField(max_length=NAME_LENGTH, unique=True)
    doc_serial_number = models.FloatField()
    village = models.ForeignKey(Village, on_delete=models.PROTECT)
    doc_link = models.CharField(max_length=URL_LENGTH)
    doc_description = models.TextField(max_length=LONG_DESCRIPTION_LENGTH)

class Camp(models.Model):
    camp_name_he = models.CharField(max_length=NAME_LENGTH, unique=True)
    camp_name_en = models.CharField(max_length=NAME_LENGTH, unique=True)
    village = models.ForeignKey(Village, on_delete=models.PROTECT)
    camp_address_in_village = models.CharField(max_length=MAP_ADDRESS_LENGTH, unique=True)
    camp_picture_thumbnail = models.ImageField(upload_to="thumbnails/")
    camp_picture_map = models.ImageField(upload_to="formap/")
    camp_picture_pageheader = models.ImageField(upload_to="forpageheader/")
    camp_description_short_he = models.CharField(max_length=SHORT_DESCRIPTION_LENGTH)
    camp_description_short_en = models.CharField(max_length=SHORT_DESCRIPTION_LENGTH)
    camp_schedule_link = models.CharField(max_length=URL_LENGTH)
    camp_contact = models.ForeignKey('Staff', on_delete=models.PROTECT)
    camp_facebook_link = models.CharField(max_length=URL_LENGTH)
    camp_email = models.CharField(max_length=EMAIL_LENGTH)

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_camp = models.ForeignKey('Camp', on_delete=models.PROTECT)
    user_role = models.CharField(max_length=NAME_LENGTH)
    user_facebook_link = models.CharField(max_length=URL_LENGTH)
    user_email = models.CharField(max_length=EMAIL_LENGTH)
    user_phoneno = models.CharField(max_length=PHONENO_LENGTH)
