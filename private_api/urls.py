
from django.conf.urls import url
from django.contrib import admin
from rest_framework.authtoken import views


from app.views import BeagleFarmListAPIView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^beagle_farms/$', BeagleFarmListAPIView.as_view(), name='beagle_farm_list_api_view'),  # pluralize and underscore the model name
    url('^api-token-auth/', views.obtain_auth_token),

]
