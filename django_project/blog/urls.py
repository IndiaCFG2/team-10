from django.urls import path
from . import views
from .views import PostListView,  PostCreateView,PostDeleteView,PostDetailView,PostUpdateView

urlpatterns = [
      path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about,name='blog-about'),
    path('course_add/',views.courseadd,name='course-add'),
    path('course_view/',views.courseView,name="course-view"),
     path('stud_view/',views.stud_view,name="stud-view"),
       path('stud_add/',views.stud_add,name="stud-add"),
]
