from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('', views.login_def, name = "home"),
    path('login/', views.login_def, name = "login_def"),
    path("register/", views.register, name="register"),
    path("registerstaff/", views.StaffRegistration.as_view(), name="registerstaff"),
    path('viewrecords/', views.records, name = "viewrecords"),
    path('farmrecords/delete/<int:pk>', views.farmrecords_delete, name = "farmrecordsdelete"),

]

