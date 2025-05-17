from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_login, name='admin_login'),
     path('admin_home', views.admin_home, name='admin_home'),
     path('admin_view_guide', views.admin_view_guide, name='admin_view_guide'),
     path('admin_view_user', views.admin_view_user, name='admin_view_user'),
       path('admin_view_pack', views.admin_view_pack, name='admin_view_pack'),

      path('admin_login_btn', views.admin_login_btn),
      path('admin_add_guide_btn', views.admin_add_guide),
      path('admin_delete_guide_btn/<id>', views.admin_delete_guide),
      path('admin_delete_user_btn/<id>', views.admin_delete_user),
      path('admin_delete_trip_btn/<id>', views.admin_delete_trip),
      path('admin_add_trip_btn', views.admin_add_trip),
]