from django.urls import path
from . import views

urlpatterns = [
    # REST API URLs
    path('api/students/', views.student_list_api),
    path('api/students/<int:id>/', views.student_detail_api),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    path('', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
    path('edit/<int:id>/', views.edit_student, name='edit_student'),

]
