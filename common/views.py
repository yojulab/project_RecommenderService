from django.contrib.auth import authenticate, login
from django.db import transaction
from django.shortcuts import render, redirect
from common.forms import UserForm
from common.forms import ProfileForm

@transaction.atomic
def signup(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            profile = profile_form.save(commit=False)
            user = user_form.save()
            profile.user = user
            profile.save()

            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인

            return redirect('/list_rdb/')
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'common/signup.html', {'user_form': user_form, 'profile_form':profile_form})