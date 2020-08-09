
from .models import Post,Student,Course,Student
from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.http import JsonResponse
from django.core import serializers
from django.template import loader

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)
# Create your views here.
def about(request):
    return render(request,'blog/about.html',{'title':'About'})


def courseView(request):
    c = Course.objects.all()
    return render(request,"blog/courses.html",{"course":c})

def courseadd(request):
    if request.method == 'POST':
        form = CourseRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Course added!')
            return redirect('/')
    else:
        form = CourseRegisterForm()
    return render(request, 'blog/courseadd.html', {'form': form})

def stud_view(request):
    c = Student.objects.all()
    return render(request,"blog/student.html",{"stud":c})

def stud_add(request):
    if request.method == 'POST':
        form = StudentMarksForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Student added!')
            return redirect('/')
    else:
        form = StudentMarksForm()
    return render(request, 'blog/stud_add.html', {'form': form})

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


