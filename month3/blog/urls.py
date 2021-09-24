from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogView.as_view(), name='blogs'),
    path('<int:pk>/', views.BlogDetailView.as_view()),
    path('create-post/', views.create_post),
    path('now/', views.date_view),
    path('random_number/', views.random_number),
    path('image/', views.image_view),
    path('students/', views.student_view),
    path('data/', views.BlogListApiView.as_view()),
]
