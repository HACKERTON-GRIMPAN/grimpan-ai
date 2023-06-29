from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('create_image/', include('create_image.urls')), # create_image API url을 이용할 수 있도록 include
    path('admin/', admin.site.urls), # admin 페이지 url
]