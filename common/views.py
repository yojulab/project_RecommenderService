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
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            # try:
            #     connect = sqlite3.connect('./db.sqlite3')
            #     cursor = connect.cursor()
            #     cursor.execute("INSERT INTO common_profile (birth_date,location,user_id) values (?, ?, ?)",
            #                    (request.POST['birth_date'], request.POST['location'], user.id))
            # finally:
            #     connect.commit()
            #     connect.close()

            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인

            return redirect('/list_rdb/')
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'common/signup.html', {'user_form': user_form, 'profile_form':profile_form})