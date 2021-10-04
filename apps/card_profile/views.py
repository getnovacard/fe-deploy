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
    user_profile = get_object_or_404(Card_profile, username=username)

    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=user_profile)

        if form.is_valid():
            form.save()

            return redirect('view_profile', username=user_profile.username)

    else:
        form = EditProfile()

    return render(request, 'card_profile/edit_profile.html', {'user_profile': user_profile, 'form': form})
