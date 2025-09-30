from django.db import models
from django.contrib.auth.models import User

pesticide_choices = (
    ('TI','Tihan'),
    ('TH', 'Thunder'),
)

seed_choices = (
    ('PL', 'Platinum'),
    ('CB', 'Cobra'),
)

fertilizer_choices = (
     ('Manure', 'poultry'),
    ('UR', 'Urea Fertilizer'),
    ('NPK15', 'NPK15-15-15'),
    ('NPK20', 'NPK20-10-10'),
    ('NPK10', 'NPK10-20-10'),
        )

#create state choices
STATE_CHOICES = (
('Lagos','Lagos'),
('Ondo','Ondo'),
('Ekiti','Ekiti'),
('Osun', 'Osun'),
('Oyo', 'Oyo'),
('Kwara','Kwara'),
('Kano','Kano'),
('Rivers','Rivers'),
)

class Farminputs(models.Model):
    avg_temp = models.FloatField()
    avg_water = models.FloatField()
    avg_pesticide = models.FloatField()
    pesticide_name = models.CharField(choices = pesticide_choices, max_length = 2)
    fertilizer_name = models.CharField(choices = fertilizer_choices, max_length = 7)
    avg_fertilizer = models.FloatField() # in kilograms per hectare(kg/ha)
  
    seed_variety = models.CharField(choices = seed_choices, max_length = 2)
    daily_observation = models.TextField( default = '')
    # seed_image = models.ImageField(upload_to ='seeds')
    created_at = models.DateTimeField(auto_now_add=True)  

    class Meta:
        verbose_name = "Farminputs"
        verbose_name_plural = "Farminputs"  # Prevents Django from adding "s"

    def __str__(self):
        return f"{self.seed_variety} - {self.pesticide_name} ({self.created_at})"
    
class Staff(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length = 200)
    lastname = models.CharField(max_length = 200)
    city = models.CharField(max_length= 200)
    mobile = models.IntegerField(default = 0)
    zipcode = models.IntegerField()
    state = models.CharField(choices = STATE_CHOICES, max_length = 100)
    def __str__(self):
        return self.firstname



