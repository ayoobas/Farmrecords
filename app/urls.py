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
    path("profile/update/<str:username>", views.staff_profile_update, name="user_profile_update"),
    path("profile/delete/<str:username>", views.staff_profile_delete, name="user_profile_delete"),
    path("staff_list/", views.staff_list, name="staff_list"),
   # path("staff_list/edit/<str:pk>", views.Staffedit, name="staff_edit"),
    path("registerstaff/", views.StaffRegistration.as_view(), name="registerstaff"),
    path('viewrecords/', views.records, name = "viewrecords"),
    path('farmrecords/delete/<int:pk>', views.farmrecords_delete, name = "farmrecordsdelete"),
    path('farmrecords/edit/<int:pk>', views.farmrecords_edit, name = "farmrecordsedit"),
    path('requestupdate/<int:pk>', views.Requestupdate, name="requestupdate"),
    path('requestupdate/delete/<int:pk>', views.Requestfarmrecorddelete, name = "requestupdatedelete"),
    path('download/farm-records/', views.download_farm_records_csv, name='download_farm_records_csv'),

    path("updatefarmrecordlist/", views.updatefarmrecordlist, name="updatefarmrecordlist"),


]+ static( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)  # for the media files

