from django.urls import path
from . import views
# from tasks.views import IndexView

urlpatterns = [
    # path('', IndexView.as_view(), name='home'),
    path('', views.index, name='home'),
    path('update_task/<str:pk>/', views.updateTask, name='update'),
    path('delete/<str:pk>/', views.delete, name='delete'),
]