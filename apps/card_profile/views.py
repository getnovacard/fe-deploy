from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Card_profile
from .forms import EditProfile


@login_required
def profiles_list(request):
    profiles = Card_profile.objects.all()

    return render(request, 'card_profile/profiles_list.html', {'profiles': profiles})


@login_required
def view_profile(request, username):
    user_profile = get_object_or_404(Card_profile, username=username)

    return render(request, 'card_profile/view_profile.html', {'user_profile': user_profile})


@login_required
def edit_profile(request, username):
    print(1)
    user_profile = get_object_or_404(Card_profile, username=username)

    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=user_profile)
        print(2)
        x = form.is_valid()
        print(3)
        y = form.errors
        print(4)
        print(form.errors)

        print(5)
        if form.is_valid():
            print(6)
            form.save()

            print(7)
            return redirect('view_profile', username=user_profile.username)

    else:
        print(8)
        form = EditProfile()

    print(9)
    return render(request, 'card_profile/edit_profile.html', {'user_profile': user_profile, 'form': form})
