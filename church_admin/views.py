from django.template import loader
from django.shortcuts import render 
from django.http import HttpResponse
from church_admin.models import Event
from church_admin.models import Income
from church_admin.models import Expense
from church_admin.models import Service
from church_admin.models import Ministry
from church_admin.models import Contribution
from church_admin.models import PastoralGroup
from church_admin.models import ChurchAttendance
from church_admin.models import ContributionType

# Create your views here.

def index(request):
	return render(request, 'church_admin/index.html')

def events_view_all(request):
	all_events = Event.objects.all()
	context = {'all_events': all_events}
	return render(request, 'church_admin/all_events.html', context)

def incomes_view_all(request):
	all_incomes = Income.objects.all()
	context = {'all_incomes': all_incomes}
	return render(request, 'church_admin/all_incomes.html', context)

def expenses_view_all(request):
	all_expenses = Expense.objects.all()
	context = {'all_expenses': all_expenses}
	return render(request, 'church_admin/all_expenses.html', context)

def services_view_all(request):
	all_services = Service.objects.all()
	context = {'all_services': all_services}
	return render(request, 'church_admin/all_services.html', context)

def ministries_view_all(request):
	all_ministries = Ministry.objects.all()
	context = {'all_ministries': all_ministries}
	return render(request, 'church_admin/all_ministries.html', context)

def contributions_view_all(request):
	all_contributions = Contribution.objects.all()
	context = {'all_contributions': all_contributions}
	return render(request, 'church_admin/all_contributions.html', context)

def pastoral_groups_view_all(request):
	all_pastoral_groups = PastoralGroup.objects.all()
	context = {'all_pastoral_groups': all_pastoral_groups}
	return render(request, 'church_admin/all_pastoral_groups.html', context)

def church_attendances_view_all(request):
	all_church_attendances = ChurchAttendance.objects.all()
	context = {'all_church_attendances': all_church_attendances}
	return render(request, 'church_admin/all_church_attendance.html', context)

def contribution_types_view_all(request):
	all_contribution_types = ContributionType.objects.all()
	context = {'all_contribution_types': all_contribution_types}
	return render(request, 'church_admin/all_contribution_types.html', context)