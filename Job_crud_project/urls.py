"""
URL configuration for Job_crud_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('welcome/', views.WelcomeView.as_view()),

    path('company/', views.CompanyView.as_view()),

    path('job-info/', views.JobView.as_view()),

    path('applicant/', views.ApplicantView.as_view()),

    path('all-jobs/', views.AllJobsView.as_view()),

    path('employer/', views.EmployerView.as_view()),
]
