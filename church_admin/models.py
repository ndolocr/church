from django.db import models
from django.conf import settings
from accounts.models import Member
from django.utils.translation import ugettext_lazy as _

'''
	This Model creates church events.
	Events are all occurences that are 
	expected to occur in church together
	with their respective dates. In this 
	model the church advertise and lets its 
	members know the events that will occur in the church.
'''

class Event(models.Model):
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	event_name = models.CharField(_('Event Name'), max_length=255, blank=False, null=False)
	date_from = models.DateField(_('From'))
	date_to = models.DateField(_('To'))	
	event_description = models.TextField(_('Event Description'))
	updated_on = models.DateTimeField(_('Updated On'), auto_now=True)
	created_on = models.DateTimeField(_('Created On'), auto_now_add=True)
	

	class Meta:
		verbose_name = "Event"
		verbose_name_plural = "Events"

	def __str__(self):
		return self.event_name

'''
	This is the expenses App.
	This application records all 
	the expenses incured by the church.
'''

class Expense(models.Model):
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	updated_on = models.DateTimeField(_('Updated On'), auto_now=True)
	created_on = models.DateTimeField(_('Created On'), auto_now_add=True)
	voucher_no = models.CharField(_('Voucher Number'), max_length=255, blank=True, null=True)
	expense_date = models.DateField(_('Date'), blank=False, null=False)
	expense_amount = models.IntegerField(_('Amount in Ksh.'), blank=False, null=False)
	expense_description = models.TextField(_('Expense Description'), blank=False, null=False)

	class Meta:
		verbose_name = "Expense"
		verbose_name_plural = "Expenses"

	def __str__(self):
		return self.voucher_no

'''
	This is the income Model.
	In this Model, all records of
	income generated by the church 
	or income generated by the church 
	for the church are recorded right here.
'''

class Income(models.Model):
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	updated_on = models.DateTimeField(_('Updated On'), auto_now=True)
	created_on = models.DateTimeField(_('Created On'), auto_now_add=True)
	receipt_no = models.CharField(_('Receipt Number'), max_length=255, blank=True, null=True)
	income_date = models.DateField(_('Date'), blank=False, null=False)
	income_amount = models.IntegerField(_('Amount in Ksh.'), blank=False, null=False)
	income_description = models.TextField(_('Income Description'), blank=False, null=False)

	class Meta:
		verbose_name = "Income"
		verbose_name_plural = "Incomes"

	def __str__(self):
		return self.receipt_no

'''
	This Model creates the Contribution Types.
	There are many different contributions in 
	church and this app is used to classify the 
	types of contributions available. They include:
	Tithe, sunday offering during the service, Thanks Giving, Develpoment among others.
'''

class ContributionType(models.Model):
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	updated_on = models.DateTimeField(_('Updated On'), auto_now=True)
	created_on = models.DateTimeField(_('Created On'), auto_now_add=True)
	contribution_type = models.CharField(_('Contribution Type'), max_length=255, blank=False, null=False)

	class Meta:
		verbose_name = "Contribution Type"
		verbose_name_plural = "Contribution Types"

	def __str__(self):
		return self.contribution_type


'''
	This is the contribution Model.
	Members of the church contribute cash 
	and other materials to the church. The members 
	contributions are recorded here for future reference.
'''

class Contribution(models.Model):
	member = models.ForeignKey(Member, on_delete=models.CASCADE, default=1)
	contribution_type = models.ManyToManyField(ContributionType)
	amount = models.PositiveIntegerField(_('Amount in Ksh.'))
	date_of_contribution = models.DateField(_('Date'), blank=False, null=False)
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	updated_on = models.DateTimeField(_('Updated On'), auto_now=True)
	created_on = models.DateTimeField(_('Created On'), auto_now_add=True)

	class Meta:
		verbose_name = 'Contribution'
		verbose_name_plural = 'Contributions'

	def __str__(self):
		contributor = "{} - {} - {}".format(self.member, self.amount, self.date_of_contribution)
		return contributor

'''
	This creates the Ministry Model.
	Ministries are used to group christians 
	in groups accoring to one's preference in
	the church activities. Groups include the choir,
	Youth groups, Men Groups, Women groups among other groups.
'''

class Ministry(models.Model):
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	updated_on = models.DateTimeField(_('Updated On'), auto_now=True)
	created_on = models.DateTimeField(_('Created On'), auto_now_add=True)
	ministry = models.CharField(_('Ministry'), max_length=255, blank=False,null=False)

	class Meta:
		verbose_name = "Ministry"
		verbose_name_plural = "Ministries"

	def __str__(self):
		return self.ministry

'''
	This model creates the Pastoral Group.
	Pastoral Groups are used to group christian
	communities according to the places they live in.
	They help neighbours who worship in the same church 
	know each other, interact and they act as the first set 
	of friends christians can go to for help when a need arises.
'''

class PastoralGroup(models.Model):
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	pastoral_group = models.CharField(_('Pastoral Group'), max_length=255, blank=False, null=False)
	updated_on = models.DateTimeField(_('Updated On'), auto_now=True)
	created_on = models.DateTimeField(_('Created On'), auto_now_add=True)

	class Meta:
		verbose_name = "Pastoral Group"
		verbose_name_plural = "Pastoral Groups"

	def __str__(self):
		return self.pastoral_group

'''
	This creates the services Model.
	This Model creates the different
	services that occur in the church.
	Records on the service name and time are recorded.
'''

class Service(models.Model):
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	updated_on = models.DateTimeField(_('Updated On'), auto_now=True)
	created_on = models.DateTimeField(_('Created On'), auto_now_add=True)
	service_name = models.CharField(_('Service Name'), max_length=255, blank=False, null=False)
	service_time = models.TimeField(_('Service Time'), blank=False, null=False)

	class Meta:
		verbose_name = "Service"
		verbose_name_plural = "Services"

	def __str__(self):
		return self.service_name


'''
	This is the church attendance Model.
	In this Model, records about the number 
	of people attending a service is recorded.	
'''

class ChurchAttendance(models.Model):
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	attendance = models.PositiveIntegerField(_('Attendance'), blank=False, null=False)
	service = models.ForeignKey(Service, on_delete=models.CASCADE)
	attendance_date = models.DateField(_('Date'), blank=False, null=False)
	updated_on = models.DateTimeField(_('Updated On'), auto_now=True)
	created_on = models.DateTimeField(_('Created On'), auto_now_add=True)

	class Meta:
		verbose_name = "Church Attendance"
		verbose_name_plural = "Church Attendances"

	def __str__(self):
		attendance_name = "{} - {}".format(self.service, self.attendance_date)
		return attendance_name


