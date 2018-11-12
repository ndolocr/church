from django.conf.urls import url
from church_admin import views

urlpatterns = [
	#/church_admin/
    url(r'^$', views.index, name='admin-home'),
    #/church_admin/event
    url(r'^event/$', views.events_view_all, name='all-events'),
    #/church_admin/income
    url(r'^income/$', views.incomes_view_all, name='all-incomes'),
    #/church_admin/member
    url(r'^member/$', views.members_view_all, name='all-members'),
    #/church_admin/expense
    url(r'^expense/$', views.expenses_view_all, name='all-expenses'),
    #/church_admin/service
    url(r'^service/$', views.services_view_all, name='all-services'),    
    #/church_admin/ministry
    url(r'^ministry/$', views.ministries_view_all, name='all-ministries'),   
    #/church_admin/contribution
    url(r'^contribution/$', views.contributions_view_all, name='all-contributions'), 
    #/church_admin/administrator
    url(r'^administrator/$', views.administrators_view_all, name='all-administrator'),
    #/church_admin/pastoral_group
    url(r'^pastoral_group/$', views.pastoral_groups_view_all, name='all-pastoral-groups'),    
    #/church_admin/church_attendance
    url(r'^church_attendance/$', views.church_attendances_view_all, name='all-church-attendances'),
    #/church_admin/contribution_type
    url(r'^contribution_type/$', views.contribution_types_view_all, name='all-contribution-types'),
]

'''
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''