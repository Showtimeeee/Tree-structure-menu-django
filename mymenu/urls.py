from django.urls import path
from mymenu.views import draw_menu

app_name = 'mymenu'

urlpatterns = [
    path('<str:menu_name>/', draw_menu, name='draw_menu'),
]