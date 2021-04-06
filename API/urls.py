from django.urls import path, include
from rest_framework import routers
from . import views
from . import views

router = routers.DefaultRouter()
router.register(r'members', views.MembersViewSet)
router.register(r'users', views.UserViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

app_name = 'API'

urlpatterns = [
    path('API/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', views.index, name="index"),
    path("password_reset/", views.password_reset_request, name="password_reset"),
    path("login/", views.login_request, name="login"),
    path("register/", views.register_request, name="register"),
    path("logout/", views.logout_request, name="logout"),
]
