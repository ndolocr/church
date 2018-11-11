from django.contrib import admin
from church_admin.models import Event
from church_admin.models import Income
from church_admin.models import Expense
from church_admin.models import Service
from church_admin.models import Ministry
from church_admin.models import Contribution
from church_admin.models import PastoralGroup
from church_admin.models import ContributionType
from church_admin.models import ChurchAttendance
# Register your models here.

admin.site.register(Event)
admin.site.register(Income)
admin.site.register(Expense)
admin.site.register(Service)
admin.site.register(Ministry)
admin.site.register(Contribution)
admin.site.register(PastoralGroup)
admin.site.register(ContributionType)
admin.site.register(ChurchAttendance)
