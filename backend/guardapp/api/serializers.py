from rest_framework import serializers

from rootapp.models import Guard
from rootapp.api.serializers import HumanSerializer, RecordSerializer


class GuardProfileSerializer(serializers.ModelSerializer):
    human = HumanSerializer()
    records = RecordSerializer(many=True, read_only=True, source='taken_records')

    class Meta:
        model = Guard
        fields = ['human', 'salary', 'guard_id', 'records']
