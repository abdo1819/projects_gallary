from django.urls import path

from . import views

urlpatterns = [
    # path('<string:branch_name>/<int:groub_number>/', views.index, name='index'),
    path('', views.hello),
    path('<slug:branch_name>/<slug:group_name>',views.projects, name='projects_viewer')

]
