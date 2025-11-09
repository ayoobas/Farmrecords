from django.db import models
from django.contrib.auth.models import User


stage_choices = (
('1', 'Nursery'),
('2', 'Permanent-Space')
)

seed_choices = (
    ('PL', 'Platinum'),
    ('CB', 'Cobra-26-f1'),
)
fungicide_choices = (
    ('MA', 'Macozeb'),('FL','Flash-One'),('SA', 'Saaf'),('CH', 'Champ-DP'),
    ('CO', 'Controphyl'),('FS','Five-Star'), ('RG', 'Ridomil-Gold'), ('CT', 'CDN-Thunda'),
        ('JM', 'Jumper'),
)
insecticide_choices = (
    ('LG', 'Laraforce-Gold'),('TI', 'Tihan'), ('VA','Vanguish'),('BE','Belt-Expert'),
    ('AM','Ampligo'),('AL', 'Allakat'),('IM','Imiforce'),('DO','Dominator'),
)
micronutrient_choices = (
    ('AG','Agrovert20-20-20'),('AV','Agrovert6-13-46'),('YA','Yara-Vita15000'),
    ('SU','Super-Fruit-Setting'),('TF','Tecamin-Flower'),('AR','Agriful'),('AP', 'Agriphyt'),
    ('AM','Agric-Max'),('PN','Potassium-Nitrate-Multi-k'),('CN', 'Calcium-Nitrate'),
    ('MS', 'Magnium-Sulphate'),
)

fertilizer_choices = (
     ('Manure', 'poultry'),
    ('UR', 'Urea Fertilizer'),
    ('NPK15', 'NPK15-15-15'),
    ('NPK20', 'NPK20-10-10'),
    ('NPK10', 'NPK10-20-10'),
    ('SSP','SSP' ),
)

cocopeat_choices = (
    ('CO', 'Coco-Coir'),('CB', 'Coco-Bliss'),
    ('GP', 'Golden-Peat'),
)

#gender choices 
GENDER_CHOICES = (
    ('M','Male'),
    ('F', 'Female'),
)
MARITAL_STATUS = (
    ('M','Married'),
    ('S', 'Single'),
)

#create state choices
STATE_CHOICES = (
('Lagos','Lagos'),('Ondo','Ondo'),('Ekiti','Ekiti'),('Osun', 'Osun'),('Oyo', 'Oyo'),
('Kwara','Kwara'),('Kano','Kano'),('Rivers','Rivers'),
)

class Farminputs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    plant_stage =  models.CharField(choices = stage_choices , max_length = 2, null=True, blank=True)
    plant_number = models.IntegerField(default= 0,null=True, blank=True)
    plant_age =  models.IntegerField(default= 0,null=True, blank=True)
    cocopeat_name= models.CharField(choices = cocopeat_choices , max_length = 2, null=True, blank=True)
    cocopeat_weight = models.FloatField(default= 0, null=True, blank=True)
    avg_temp = models.FloatField(default= 0, null=True, blank=True)
    avg_water = models.FloatField(default= 0, null=True, blank=True)
    seed_variety = models.CharField(choices = seed_choices, max_length = 2)
    daily_observation = models.TextField( default = '')
    # seed_image = models.ImageField(upload_to ='seeds')
    created_at = models.DateTimeField(auto_now_add=True)  

    class Meta:
        verbose_name = "Farminput"
        verbose_name_plural = "Farminput"  # Prevents Django from adding "s"

    def __str__(self):
        return f"{self.id}"

class Farminputtwo(models.Model):
    FI = models.ForeignKey(Farminputs, on_delete=models.CASCADE, related_name='chemicals') 
    fungicide_name = models.CharField(choices = fungicide_choices, max_length = 2,  null=True, blank=True)
    avg_fungicide = models.FloatField(default= 0, null=True, blank=True)
    insecticide_name = models.CharField(choices = insecticide_choices, max_length = 2)
    avg_insecticide = models.FloatField(default= 0, null=True, blank=True)
    micronutrient_name = models.CharField(choices = micronutrient_choices, max_length = 2)
    avg_micronutrient = models.FloatField(default= 0, null=True, blank=True)
    fertilizer_name = models.CharField(choices = fertilizer_choices, max_length = 7)
    avg_fertilizer = models.FloatField(default= 0, null=True, blank=True) # in kilograms per hectare(kg/ha)
    class Meta:
        verbose_name = "Farminputtwo"
        verbose_name_plural = "Farminputtwo"  # Prevents Django from adding "s"

    def __str__(self):
        return f"{self.id}"
    
class Staff(models.Model):
    staff = models.OneToOneField(User,on_delete=models.CASCADE, null = True)   
    mobile = models.IntegerField(default = 0, null=True, blank=True)
    streetno = models.IntegerField(default = 0, null=True, blank=True)
    streetname = models.CharField(max_length= 60, null=True, blank=True)
    city = models.CharField(max_length= 60, null=True, blank=True)
    state = models.CharField(choices = STATE_CHOICES, max_length = 20)
    emp_date = models.DateField(null=True, blank=True)
    current_salary = models.FloatField(default= 0, null=True, blank=True)
    gender = models.CharField(choices = GENDER_CHOICES, max_length = 2, null=True, blank=True)
    marital_status = models.CharField(choices = MARITAL_STATUS, max_length = 2, null=True, blank=True)
    children_no = models.IntegerField(default= 0, null=True, blank=True)
    spouse_no = models.IntegerField( default= 0, null=True, blank=True)
    image = models.ImageField(default = 'avatar.jpg', upload_to = 'Profile_Images')
    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staff"  # Prevents Django from adding "s"

    def __str__(self):
        return self.staff.username



