from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter

from test_db.views import TestDataViewSet, TestDataRelationViewSet

router = SimpleRouter()

router.register(r'book', TestDataViewSet)
router.register(r'book_relation', TestDataRelationViewSet)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('test_db.urls')),
    re_path('', include('social_django.urls', namespace='social'))

]

urlpatterns += router.urls
