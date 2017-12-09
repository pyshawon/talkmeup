from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from rest_framework import permissions
from rest_framework import generics

<<<<<<< HEAD
from userprofile.forms import ContactedUserForm, SignUpForm
=======
from userprofile.forms import SignUpForm
>>>>>>> f0cfdcab2a9d074b95c0dd39f7859486b0e90596
from userprofile.models import UserProfile
from userprofile.permissions import IsOwner
from userprofile.serializers import UserProfileSerializer
from userprofile.tokens import account_activation_token


class UserProfileList(generics.ListCreateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return UserProfile.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsOwner,)


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            user.save()
            UserProfile.objects.create(owner=user)
            user.userprofile.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'userprofile/signup.html', {'form': form})
<<<<<<< HEAD


def contact(request):
    if request.method == 'POST':
        form = ContactedUserForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('home')
=======
>>>>>>> f0cfdcab2a9d074b95c0dd39f7859486b0e90596
