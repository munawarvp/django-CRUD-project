from django.urls import path
from . import views

urlpatterns = [
    path('',views.signin, name='signin'),
    path('signup',views.signup, name='signup'),
    path('home', views.home, name='home'),
    path('logout', views.logout, name='logout'),

    path('admin_panel', views.admin_panel, name='admin_panel'),
    path('add_user', views.add_user, name='add_user'),
    
    path('reg_form_submission',views.reg_form_submission, name='reg_form_submission'),
    path('add_user_form', views.add_user_form, name='add_user_form'),
    path('login_form_submit',views.login_form_submit, name='login_form_submit'),
    path('delete_user/<int:id>', views.delete_user, name='delete_user'),

    path('update_user/<int:id>', views.update_user, name='update_user'),
    path('update_user_form/<int:id>', views.update_user_form, name='update_user_form'),

    path('search_user', views.search_user, name='search_user'),
    
]