from django.urls import reverse_lazy
from django.views.generic import CreateView
from violations.forms import RegisterUserForm
from violations.models import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')

def validate_username(request):
    username = request.GET.get('username', None)
    response = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(response)

@login_required
def profile(request):
    current_user = request.user
    print(current_user.username)

    if request.method == "POST":
        post = Post()
        post.title = request.POST.get("title")
        post.body = request.POST.get("body")
        post.user = request.user
        post.save()
    return render(request, 'violations/profile.html')

@login_required
def allPost(request):
    posts = Post.objects.filter(user=request.user)
    return render(request, 'violations/allPost.html', {"posts": posts})