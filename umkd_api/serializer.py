from rest_framework import serializers
from umkd_api.models import Competence, Indicator


class DesktopIndicatorSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Indicator
        fields = "code", "description", "type"
        extra_kwargs = {'code': {'read_only': True}, 'description': {'read_only': True}}


class DesktopCompetenceSerializer(serializers.ModelSerializer):
    indicator_set = DesktopIndicatorSerializer(many=True, required=True)

    class Meta(object):
        model = Competence
        fields = "code", "description", "indicator_set",
        extra_kwargs = {'code': {'read_only': True}, 'description': {'read_only': True}}
