from django.urls import path

from mymenu import views
from mymenu.views import draw_menu, post_detail

app_name = 'mymenu'

urlpatterns = [
    path('', views.index),
    path('<str:menu_name>/', draw_menu, name='draw_menu'),
    path('mainmenu/<str:name>/', post_detail, name='post_detail')

]