from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^markers/$', views.show_markers, name='show_markers'),
    url(r'show_info/(?P<el_id>[0-9]+)/$',views.show_full_info,name='show_info'),
]

#settings for media
#copying url from settings for our media data
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
