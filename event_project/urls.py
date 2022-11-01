"""event_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from users import views as user_views
from shared import views as shared_views
from event import views as event_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", user_views.user_register, name="register"),
     path("logout/", user_views.logout_user, name="logout"),
     path("login/", user_views.login_user, name="login"),
     path("home/", event_views.home, name="home"),
     path("profile-org/<int:user_id>/", user_views.get_organizer_profile, name="profile_org"),
     path("profile/edit/<int:user_id>/", user_views.update_profile, name="edit_profile"),
     path("event/add/", event_views.create_event, name="create_event" ),
     path("book/<int:event_id>/", event_views.book_event, name="book_event"),
     path("success/", event_views.booking_success, name="booking_success"),
      path("profile-user/<int:user_id>/", user_views.get_user_profile, name="profile_user"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)