from django.urls import path
from . import views


urlpatterns = [

    path('',views.login_r ,name="login_r"),
    path('login_v',views.login_v ,name="login_v"),
    path('p_logout',views.p_logout ,name="p_logout"),
    path('emp/',views.emp ,name="emp"),
    path('show',views.show,name = "show"),
    path('delete/<int:id>',views.delete),


]
