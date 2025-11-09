from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.login_def, name = "home"),
    path('login/', views.login_def, name = "user_login"),
    path('logout/', views.logout_user, name = "user_logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.staff_profile, name="user_profile"),
    path("staff_list/", views.staff_list, name="staff_list"),
    path("registerstaff/", views.StaffRegistration.as_view(), name="registerstaff"),
    path('viewrecords/', views.records, name = "viewrecords"),
    path('farmrecords/delete/<int:pk>', views.farmrecords_delete, name = "farmrecordsdelete"),
    path('farmrecords/edit/<int:pk>', views.farmrecords_edit, name = "farmrecordsedit"),


]+ static( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)  # for the media files

