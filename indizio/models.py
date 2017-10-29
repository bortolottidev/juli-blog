from django.db import models

class Indizio(models.Model):
	title = models.CharField(max_length=30)
	text = models.TextField()
	# Scelte che puntano a questo indizio
	#puntato_da = models.OneToOneField(Scelta, null=True) 
		#null=True, default=NULL, through='Scelta')

	def __str__(self):
		return self.title+" "+self.text[:20]

class Scelta(models.Model):
	# Molte scelta portano allo stesso indizio
	# Indizio che mostra questa scelta
	indizio_from = models.ForeignKey(Indizio, 
		related_name='fromz',null=True)
	# Indizio successivo
	indizio_next = models.ForeignKey(Indizio, 
		related_name='toz', null=True)
	text = models.CharField(max_length=200)

	def __str__(self):
		return self.text