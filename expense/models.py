from django.db import models
import json, random

class Expense(models.Model):
	def random_id():
		return str(random.randint(2000, 5000))
	
	id = models.CharField( default=random_id, primary_key=True, max_length=4)
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