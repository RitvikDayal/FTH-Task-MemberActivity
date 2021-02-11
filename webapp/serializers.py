from .models import Member, Activity
from rest_framework import serializers


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        #fields='__all__'
        # #fields =('id','member','start_time','end_time')
        fields=('start_time','end_time')

class MemberSerializer(serializers.ModelSerializer):
    activity_periods=ActivitySerializer(read_only=True,many=True)
    class Meta:
        model = Member
        fields = ('id','real_name','tz','activity_periods')