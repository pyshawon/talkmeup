from rest_framework import serializers

from userprofile.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    email = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'displayName', 'createdOn')
