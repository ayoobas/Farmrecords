from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone

plant_choices = (
    ('Tomatoes', 'Tomatoes'),
    ('Bell_Pepper', 'Bell_Pepper'), ('Habanero', 'Habanero'),
)
stage_choices = (
('1', 'Nursery'),
('2', 'Permanent-Space'),
)

seed_choices = (
    ('Platinum', 'Platinum'),
    ('Cobra-26-f1', 'Cobra-26-f1'),
    ('SIMBAD', 'SIMBAD'),
    ('NIKITA', 'NIKITA'),
     ('OT', 'OTHERS'),
)
fungicide_choices = (
    ('MA', 'Macozeb'),('FL','Flash-One'),('SA', 'Saaf'),('CH', 'Champ-DP'),
    ('CO', 'Controphyl'),('FS','Five-Star'), ('RG', 'Ridomil-Gold'), ('CT', 'CDN-Thunda'),
        ('JM', 'Jumper'),  ('OT', 'OTHERS'),
)
insecticide_choices = (
    ('LG', 'Laraforce-Gold'),('TI', 'Tihan'), ('VA','Vanguish'),('BE','Belt-Expert'),
    ('AM','Ampligo'),('AL', 'Allakat'),('IM','Imiforce'),('DO','Dominator'),  ('OT', 'OTHERS'),
)
micronutrient_choices = (
    ('AG','Agrovert20-20-20'),('AV','Agrovert6-13-46'),('YA','Yara-Vita15000'),
    ('SU','Super-Fruit-Setting'),('TF','Tecamin-Flower'),('AR','Agriful'),('AP', 'Agriphyt'),
    ('AM','Agric-Max'),('PN','Potassium-Nitrate-Multi-k'),('CN', 'Calcium-Nitrate'), 
    ('MS', 'Magnium-Sulphate'), ('OT', 'OTHERS'),
)

fertilizer_choices = (
     ('Manure', 'poultry'),
    ('UR', 'Urea Fertilizer'),
    ('NPK15', 'NPK15-15-15'),
    ('NPK20', 'NPK20-10-10'),
    ('NPK10', 'NPK10-20-10'),
    ('SSP','SSP' ), ('OT', 'OTHERS'),
)

herbicides_choices = (
    ('FU','Force-Up'),
    ('BF','Bara-Force'),
    ('WC','Weed-Crusher'),
    ('SL', 'Slasher'), ('OT', 'OTHERS'),

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
    ('Married','Married'),
    ('Single', 'Single'),
)

#create state choices
# STATE_CHOICES = (
# ('Lagos','Lagos'),('Ondo','Ondo'),('Ekiti','Ekiti'),('Osun', 'Osun'),('Oyo', 'Oyo'),
# ('Kwara','Kwara'),('Kano','Kano'),('Rivers','Rivers'),
# )


def validate_image_size(image):
    max_size = 0.5 * 1024 * 1024  # 1 MB
    if image.size > max_size:
        raise ValidationError("Image file too large (max 500KB allowed).")

def validate_not_future(value):
    if value > timezone.now().date():
        raise ValidationError("Date cannot be in the future.")

class Farminputs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    plant_choice =  models.CharField(choices = plant_choices  , max_length = 12, null=True, blank=True)
    plant_stage =  models.CharField(choices = stage_choices , max_length = 2, null=True, blank=True)
    plant_number = models.IntegerField(default= 0,null=True, blank=True)
    plant_age =  models.IntegerField(default= 0,null=True, blank=True)
    cocopeat_name= models.CharField(choices = cocopeat_choices , max_length = 2, null=True, blank=True)
    cocopeat_weight = models.FloatField(default= 0, null=True, blank=True)
    avg_temp = models.FloatField(default= 0, null=True, blank=True)
    avg_water = models.FloatField(default= 0, null=True, blank=True)
    seed_variety = models.CharField(choices = seed_choices, max_length = 12)
    seed_variety_other = models.CharField( max_length=30, blank=True, null=True)
    daily_observation = models.TextField( default = '')
  
    image = models.ImageField(default = 'avatar.jpg', validators=[validate_image_size],  upload_to = 'Observation_Images')
  
    created_at = models.DateField(null=True, blank=True, validators=[validate_not_future])

    class Meta:
        verbose_name = "Farminput"
        verbose_name_plural = "Farminput"  # Prevents Django from adding "s"

    def __str__(self):
        return f"{self.id}"

class Farminputtwo(models.Model):
    FI = models.ForeignKey(Farminputs, on_delete=models.CASCADE, related_name='chemicals') 
    fungicide_name = models.CharField(choices = fungicide_choices, max_length = 2,  null=True, blank=True)
    fungicide_other = models.CharField( max_length=30, blank=True, null=True)
    avg_fungicide = models.FloatField(default= 0, null=True, blank=True)
    
    insecticide_name = models.CharField(choices = insecticide_choices, max_length = 2)
    insecticide_other = models.CharField( max_length=30, blank=True, null=True)
    avg_insecticide = models.FloatField(default= 0, null=True, blank=True)
   

    herbicide_name = models.CharField(choices = herbicides_choices, max_length = 2)
    herbicide_other = models.CharField( max_length=30, blank=True, null=True)
    avg_herbicide = models.FloatField(default= 0, null=True, blank=True)
    
   
    
    micronutrient_name = models.CharField(choices = micronutrient_choices, max_length = 2)
    micronutrient_other = models.CharField( max_length=30, blank=True, null=True)
    avg_micronutrient = models.FloatField(default= 0, null=True, blank=True)
    
    
   
    fertilizer_name = models.CharField(choices = fertilizer_choices, max_length = 7)
    fertilizer_other = models.CharField( max_length=30, blank=True, null=True)
    avg_fertilizer = models.FloatField(default= 0, null=True, blank=True) # in kilograms per hectare(kg/ha)
    
  

    class Meta:
        verbose_name = "Farminputtwo"
        verbose_name_plural = "Farminputtwo"  # Prevents Django from adding "s"

    def __str__(self):
        return f"{self.id}"
    
class Staff(models.Model):
    staff = models.OneToOneField(User,on_delete=models.CASCADE, null = True)   
    mobile = models.CharField(max_length= 20, null=True, blank=True)
    streetno = models.IntegerField(default = 0, null=True, blank=True)
    streetname = models.CharField(max_length= 60, null=True, blank=True)
    city = models.CharField(max_length= 60, null=True, blank=True)
    state = models.CharField(max_length= 60, null=True, blank=True)
    
    emp_date = models.DateField(null=True, blank=True)
    current_salary = models.FloatField(default= 0, null=True, blank=True)
    gender = models.CharField(choices = GENDER_CHOICES, max_length = 2, null=True, blank=True)
    marital_status = models.CharField(choices = MARITAL_STATUS, max_length = 10, null=True, blank=True)
    is_active = models.BooleanField(default=False) 
    emp_role =  models.CharField(max_length= 60, null=True, blank=True)

    image = models.ImageField(default = 'avatar.jpg', validators=[validate_image_size],  upload_to = 'Profile_Images')
    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staff"  # Prevents Django from adding "s"

    def __str__(self):
        return self.staff.username

class RequestFarmrecordupdates(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # record_id = models.ForeignKey(Farminputs, on_delete=models.CASCADE)
    record_id = models.IntegerField()
    request = models.CharField(max_length= 60, null=True, blank=True)
    rectified = models.BooleanField(default=False) 
    created_at = models.DateField(auto_now_add=True)  
    class Meta:
        verbose_name = "RequestFarmrecordupdates"
        verbose_name_plural = "RequestFarmrecordupdates"  # Prevents Django from adding "s"
    def __str__(self):
        return self.user.username

