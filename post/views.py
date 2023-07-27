# from django.shortcuts import render
#
# # Create your views here.
# def index(request):
#     return render (request, 'index.html',{})
#
# def complaint(request):
#     submitted = False
#     return render (request, 'Complaint.html',{})

from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import PostForm
from .models import Post

# Create your views here.

class HomePageView(ListView):
    model = Post
    template_name = 'index.html'

class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'Complaint.html'
    success_url = reverse_lazy('index')
