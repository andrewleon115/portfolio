from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),  # Example view for the home page
    path('project/<int:pk>/', project_detail, name='project_detail'),  # ✅ Add this
    path('about/', about_page, name='about'),
    path('skill/', skill_detail, name='skill'),
    path('resume/view/', resume_view, name='resume_view'),
    path('resume/download/', resume_download, name='resume_download'),
    path("blog/", blog_detail, name='blog'),
    path('contact/', contact_view, name='contact')
]
