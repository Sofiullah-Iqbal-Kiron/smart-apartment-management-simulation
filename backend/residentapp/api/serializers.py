from datetime import timedelta

# django
from django.utils import timezone

# rest framework
from rest_framework import serializers

# local
from rootapp.models import Resident, Issue, TempToken
from rootapp.api.serializers import (HumanSerializer, BlockSerializer, RecordSerializer)
from ..utils import generate_a_temp_token


class IssueSerializer(serializers.ModelSerializer):
    raised_at = serializers.DateTimeField(read_only=True, format='%d %B %Y (%I:%M %p)')
    last_updated = serializers.DateTimeField(default=timezone.now(), read_only=True, format='%d %B %Y (%I:%M %p)')

    class Meta:
        model = Issue
        fields = ['id',
                  'title',
                  'details',
                  'raised_at',
                  'last_updated',
                  'emergency',
                  'checked',
                  'resolved',
                  'edited']

    def create(self, validated_data):
        return Issue.objects.create(**validated_data)


class ResidentProfileSerializer(serializers.ModelSerializer):
    human = HumanSerializer()
    accommodation = BlockSerializer()
    ID = serializers.CharField(source='resident_id', read_only=True)
    issues = IssueSerializer(many=True, read_only=True)
    records = RecordSerializer(many=True, source='his_her_entries', read_only=True)

    class Meta:
        model = Resident
        fields = ['human', 'accommodation', 'ID', 'issues', 'records']

    def validate_ID(self, value: str):
        """Validate ID, starts with RS-, length 10"""
        if not value.startswith("RS-"):
            raise serializers.ValidationError("resident_id must be start with 'RS-'")
        if len(value) != 10:
            raise serializers.ValidationError("resident_id must be of length 10")
        return value


class TempTokenSerializer(serializers.ModelSerializer):
    token_key = serializers.CharField(source='key', read_only=True)
    number_of_allowed_guests = serializers.IntegerField(min_value=1, max_value=50, source='nag')
    valid_till = serializers.DateTimeField(format="%d %B %Y (%I:%M %p)", read_only=True)

    class Meta:
        model = TempToken
        fields = ['token_key', 'number_of_allowed_guests', 'used', 'valid_till']
        read_only_fields = ['used']

    def create(self, validated_data):
        token_key = generate_a_temp_token()
        nag = validated_data.get('nag', 1)
        fond_by = validated_data['fond_by']
        return TempToken.objects.create(key=token_key, nag=nag, fond_by=fond_by, valid_till=timezone.now() + timedelta(minutes=10))
