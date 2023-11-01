from django.contrib.auth.models import User

from rest_framework import serializers

from rootapp.models import Human, Block, Resident, Record


class DateTimeSerializer(serializers.Serializer):
    year = serializers.IntegerField(min_value=1, max_value=9999)
    month = serializers.IntegerField(min_value=1, max_value=12)
    day = serializers.IntegerField(min_value=1, max_value=31)
    hour = serializers.IntegerField(min_value=0, max_value=24)
    minute = serializers.IntegerField(min_value=0, max_value=60)
    second = serializers.IntegerField(min_value=0, max_value=60)


class UserSerializer(serializers.ModelSerializer):
    fullname = serializers.CharField(source='get_full_name')
    since = serializers.DateTimeField(source='date_joined', format='%d %B %Y (%I:%M %p)')

    class Meta:
        model = User
        fields = ['username', 'fullname', 'email', 'since']


class HumanSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    avatar = serializers.ImageField(source='photo')
    date_of_birth = serializers.DateField(format='%d %B %Y')

    class Meta:
        model = Human
        fields = ['user', 'gender', 'nid_or_br', 'contact', 'date_of_birth', 'avatar']


class BlockSerializer(serializers.ModelSerializer):
    label = serializers.CharField(source='name')

    class Meta:
        model = Block
        fields = ['label', 'floor']


class RecordSerializer(serializers.ModelSerializer):
    record_of = serializers.CharField(source='who')
    record_type = serializers.ChoiceField(source='e_type', choices=Record.TYPE)
    recorded_at = serializers.DateTimeField(source='timestamp', read_only=True, format='%d %B %Y (%I:%M %p)')
    recorded_by = serializers.StringRelatedField(source='recorder', read_only=True)

    class Meta:
        model = Record
        fields = ['record_of', 'record_type', 'recorded_at', 'recorded_by']

    def create(self, validated_data):
        validated_data['who'] = Resident.objects.get(resident_id__exact=validated_data['who'])
        return Record.objects.create(**validated_data)
