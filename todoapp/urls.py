from django.urls import path
from . import views


urlpatterns= [
    path('',views.Todoapp,name='todoview'),
    path('delete/<todo_id>', views.deleteview,name ='delete'),
    path('cross_off/<todo_id>', views.cross_off, name='cross_off'),
    path('uncross/<todo_id>', views.uncross, name='uncross'),

]