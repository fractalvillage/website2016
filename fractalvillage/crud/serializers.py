from rest_framework import serializers
from fractalvillage.crud.models import *

class VillageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Village
        fields = ('url', 'village_name_he', 'village_name_en', 'village_facebook_link', 'village_slack_link', 'village_email')

class VillageDocsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VillageDocs
        fields = ('url', 'doc_title', 'doc_serial_number', 'doc_link', 'doc_description')

class CampSerializer(serializers.HyperlinkedModelSerializer):
    camp_picture_thumbnail_url = serializers.SerializerMethodField()
    camp_picture_map_url = serializers.SerializerMethodField()
    camp_picture_pageheader_url = serializers.SerializerMethodField()
    class Meta:
        model = Camp
        fields = ('url', 'camp_name_he', 'camp_name_en', 'camp_address_in_village', 'village', 'camp_picture_thumbnail_url', 'camp_picture_map_url', 'camp_picture_pageheader_url', 'camp_description_short_he', 'camp_description_short_en', 'camp_schedule_link', 'camp_contact', 'camp_facebook_link', 'camp_email')
    def get_camp_picture_thumbnail_url(self, obj):
        return obj.camp_picture_thumbnail.url if obj.camp_picture_thumbnail else None
    def get_camp_picture_map_url(self, obj):
        return obj.camp_picture_map.url if obj.camp_picture_map else None
    def get_camp_picture_pageheader_url(self, obj):
        return obj.camp_picture_pageheader.url if obj.camp_picture_pageheader else None
