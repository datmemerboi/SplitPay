from django.db import models
import json

class Expense(models.Model):
	Name = models.CharField(max_length=30)
	Actors = models.CharField(max_length=300)

	def set_Name(self, n):
		self.Name = n

	def get_Name(self):
		return self.Name

	def set_Actors(self, s):
		self.Actors = json.dumps(s)

	def get_Actors(self):
		return json.loads( self.Actors )