import json, sys
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate

from .views import UserProfileList, UserProfileDetail
from .models import UserProfile

class UserProfileTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.leon = User.objects.create_user(
            username='leon', email='leon@…', password='top_secret')
        self.jj = User.objects.create_user(
            username='jj', email='jj@…', password='top_secret')

    def test_create_profile(self):
        response = self.create_profile(self.leon)
        self.assert_has_profile(response, 201)

    def test_profile_list_only_visible_to_owner(self):
        response = self.create_profile(self.leon)
        response = self.list_profiles(self.leon)
        self.assert_has_profile(response, 200)

        response = self.list_profiles(self.jj)
        self.assert_no_profile(response, 200)

    def test_profile_detail_only_visible_to_owner(self):
        self.create_profile(self.leon)
        request = self.factory.get('/userprofile/')
        response = self.request_detail_as_user(self.leon, request, 1)
        self.assert_has_profile(response, 200)

        request = self.factory.get('/userprofile/')
        response = self.request_detail_as_user(self.jj, request, 1)
        self.assertEqual(response.status_code, 403)

    def list_profiles(self, user):
        request = self.factory.get('/userprofile')
        return self.request_list_as_user(user, request)

    def create_profile(self, user):
        request = self.factory.post('/userprofile', {'displayName': user.username})
        return self.request_list_as_user(user, request)

    def assert_has_profile(self, response, code):
        self.assertContains(response, 'id', status_code=code)
        self.assertContains(response, 'email', status_code=code)
        self.assertContains(response, 'displayName', status_code=code)
        self.assertContains(response, 'createdOn', status_code=code)

    def assert_no_profile(self, response, code):
        self.assertNotContains(response, 'id', status_code=code)
        self.assertNotContains(response, 'email', status_code=code)
        self.assertNotContains(response, 'displayName', status_code=code)
        self.assertNotContains(response, 'createdOn', status_code=code)

    @staticmethod
    def request_list_as_user(user, request):
        force_authenticate(request, user=user)
        view = UserProfileList.as_view();
        return view(request)

    @staticmethod
    def request_detail_as_user(user, request, id):
        force_authenticate(request, user=user)
        view = UserProfileDetail.as_view();
        return view(request, pk=id)
