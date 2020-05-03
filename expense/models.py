from django.db import models
import json

class Expense(models.Model):
	name = models.CharField(max_length=30)
	actors = models.CharField(max_length=300)
	dateTime = models.DateTimeField(auto_now=True)

	def set_name(self, n):
		self.name = n
	def get_name(self):
		return self.name

	def set_actors(self, s):
		self.actors = json.dumps(s)
	def get_actors(self):
		return json.loads( self.actors )
	
	def get_dateTime(self):
		return self.dateTime

class Payment(models. Model):
	whichExpense = models.ForeignKey( Expense, on_delete=models.CASCADE )
	amount = models.IntegerField()
	paymentBy = models.CharField(max_length=300)

	def set_amount(self, a):
		self.amount = a

	def set_paymentBy(self, p):
		self.paymentBy = json.dumps( p )
