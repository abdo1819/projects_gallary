from django.urls import path,include

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'branchs', views.BranchViewSet)
router.register(r'instractors', views.InstractorViewSet)
router.register(r'students', views.StudentViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'main_projects', views.MainProjectViewSet,basename="main_pro")


urlpatterns = [
    # path('<string:branch_name>/<int:groub_number>/', views.index, name='index'),
    # path('', views.hello),
    path('', include(router.urls)),

    path('<slug:branch_name>/<slug:group_name>',views.projects, name='projects_viewer')

]
