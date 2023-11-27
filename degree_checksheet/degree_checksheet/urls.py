"""
URL configuration for degree_checksheet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin, auth
from django.urls import path, include
from checksheet import views, api_views
from checksheet.views import profile
from degree_checksheet.views import course_count

urlpatterns = [
    path('admin/', admin.site.urls),
    # home page redirect
    path('', include('checksheet.urls')),
    # checklist page
    path('checklist/', views.checklist, name="checklist"),
    # accounts
    path("accounts/", include(("django.contrib.auth.urls", "auth"), namespace="accounts")),
    path("accounts/password_reset/done/",auth.views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path("accounts/reset/done/",auth.views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    path("accounts/profile/", profile, name="profile"),
    path('record_management/', include("record_management.urls")),
    # file upload
    path('upload/', views.upload),
    path('api/course_api_view/',api_views.course_api_view),
    path('graph/', course_count, name="course_count" )

]
