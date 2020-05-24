from django.urls import path,include
import xadmin
from django.views.generic import TemplateView

from users import views
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('users',views.UserProfileViewSet)

urlpatterns = [
    # path('xadmin',xadmin.site.urls),
    # path('',include(router.urls)),
    # path('api-auth/',include('rest_framework.urls',namespace='rest_framework'))
    # path('',include('users.urls')),
    # path('',TemplateView.as_view(template_name='index.html'),name='index'),
    # path('login/',TemplateView.as_view(template_name='userinfo/login.html'),name='login'),
]
