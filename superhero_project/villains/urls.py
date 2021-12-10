from django.urls import path
from . import views

app_name = 'villains'
urlpatterns = [
    path('new_villain/', views.create, name='create'),
    path('<int:villain_id>/details', views.detail, name='detail'),
    path('<int:villain_id>/update', views.update, name='update'),

]