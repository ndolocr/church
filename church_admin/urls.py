from django.conf.urls import url
from church_admin import views

urlpatterns = [
	#/church_admin/
    url(r'^$', views.home, name='admin-home')
]

'''
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''