from django.shortcuts import render
from rest_framework import permissions

from userprofile.models import UserProfile
from userprofile.permissions import IsOwner
from userprofile.serializers import UserProfileSerializer
from rest_framework import generics


class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAdminUser,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsOwner,)
