from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def profile(request):
    return render(request, "filmdiary_auth/profile.html", {"page_group": "profile"})
