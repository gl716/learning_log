from django.urls import path

from . import views

app_name = 'app1'
urlpatterns = [
    # home page
    path('', views.index, name='index'),
    # page that show all topics.
    path('topics/', views.topics, name='topics'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

]
