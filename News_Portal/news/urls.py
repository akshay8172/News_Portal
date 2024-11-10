from django.contrib import admin
from django.urls import path, include

from news import views

urlpatterns = [
    path('',views.home),
    path('registration',views.registration),
    path('login',views.login,name='login'),
    path('add_notificaation',views.add_notificaation),
    path('notifications',views.notification_list),
    path('AdminHome',views.AdminHome),
    path('admin_view_news',views.admin_view_news),
    path('admin_view_more_news/<id>',views.admin_view_more_news, name='admin_view_more_news'),
    path('admin_view_comments/<int:id>/', views.admin_view_comments, name='admin_view_comments'),
    path('admin_view_new_comments/<int:id>/', views.admin_view_new_comments, name='admin_view_new_comments'),
    path('admin_view_sender/<int:id>/', views.admin_view_sender, name='admin_view_sender'),
    path('admin_delete_comment/<int:id>/', views.admin_delete_comment, name='admin_delete_comment'),
    path('delete_notification/<int:id>/', views.delete_notification, name='delete_notification'),
    path('admin_view_users', views.admin_view_users, name='admin_view_users'),


    path('registration',views.registration),
    path('UserHome',views.UserHome),
    path('user_view_news',views.user_view_news,name='user_view_news'),
    path('user_view_past_news',views.user_view_past_news,name='user_view_past_news'),
    path('user_view_more_news/<id>',views.user_view_more_news,name='user_view_more_news'),
    path('user_view_comments/<id>/',views.user_view_comments,name='user_view_comments'),
    path('post_comment/<id>',views.post_comment,name='post_comment'),
    path('edit_comment/<id>',views.edit_comment,name='edit_comment'),
    path('ManageProfile',views.ManageProfile,name='ManageProfile'),
    path('edit_profile',views.edit_profile,name='edit_profile'),
    path('user_notification_list',views.user_notification_list,name='user_notification_list'),
    path('change_password',views.change_password,name='change_password'),
    path('search_news_category',views.search_news_category,name='search_news_category'),

]