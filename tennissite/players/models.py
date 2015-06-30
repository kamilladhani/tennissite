from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    dob = models.CharField(max_length=200)
    age = models.IntegerField()
    desc = models.CharField(max_length=200)
    grandslams_won = models.IntegerField(default=0)
    
    def __unicode__(self):
    	return self.name
    
class GrandSlam(models.Model):
	AUSTRALIAN = 'Australian Open'
	FRENCH = 'French Open'
	WIMBLEDON = 'Wimbledon'
	US = 'US Open'
	YEAR_IN_SCHOOL_CHOICES = (
		(AUSTRALIAN, AUSTRALIAN),
		(FRENCH, FRENCH),
		(WIMBLEDON, WIMBLEDON),
    	(US, US),
	)
	grandslam = models.CharField(max_length=50,
                        		choices=YEAR_IN_SCHOOL_CHOICES,
                            	default=AUSTRALIAN)
	player = models.ForeignKey(Player)
	year = models.IntegerField()

    