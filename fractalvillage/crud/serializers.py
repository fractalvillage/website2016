from rest_framework import serializers
from fractalvillage.crud.models import *

class VillageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Village
        fields = ('village_name_he', 'village_name_en', 'village_facebook_link', 'village_slack_link', 'village_email')

class VillageDocsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VillageDocs
        fields = ('doc_title', 'doc_serial_number', 'doc_link', 'doc_description')

class CampSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Camp
        fields = ('camp_name_he', 'camp_name_en', 'camp_picture_thumbnail', 'camp_picture_pageheader', 'camp_description_short_he', 'camp_description_short_en', 'camp_schedule_link', 'camp_contact', 'camp_facebook_link', 'camp_email')
