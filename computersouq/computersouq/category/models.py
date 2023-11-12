from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
from django.urls import reverse
from django.utils.text import slugify


class Categories(models.Model):
    pass     
### Laptops Section ###
class Laptops(Categories):
    Brands = (
        ('HP', 'HP'),
        ('DELL', 'DELL'),
        ('LENOVO', 'LENOVO'),
        ('ACER', 'ACER'),
        ('ASUS', 'ASUS'),
        ('HUAWEI', 'HUAWEI'),
        ('Other', 'Other'),
    )
    HD_Types = (
        ('SSD', 'SSD'),
        ('HDD', 'HDD'),
    )
    RAM_Type = (
        ('DDR3', 'DDR3'),
        ('DDR3L', 'DDR3L'),
        ('DDR4', 'DDR4'),
        ('DDR5', 'DDR5'),
    )
    Screen_Sizes = (
        ('11.6 inch', '11.6 inch'),
        ('12.5 inch', '12.5 inch'),
        ('13.3 inch', '13.3 inch'),
        ('14 inch', '14 inch'),
        ('15.6 inch', '15.6 inch'),
        ('17.3 inch', '17.3 inch'),
    )
    Screen_Resulations = (
        ('HD', 'HD'),
        ('FHD', 'FHD'),
        ('2K', '2K'),
        ('3K', '3K'),
        ('4K', '4K'),
    )
    Condition = models.CharField(max_length= 50, choices= (('New', 'New'), ('Used', 'Used')))
    Brand = models.CharField(max_length= 50, choices= Brands)
    Model = models.CharField(max_length= 50)
    CPU = models.CharField(max_length=30)
    Ram_Memory_Type = models.CharField(max_length=30, choices= RAM_Type)
    Ram_Memory_Size = models.IntegerField()
    HD_Type = models.CharField(max_length=30, choices= HD_Types)
    HD_Storage = models.IntegerField()
    HD_Type_Other = models.CharField(max_length=30, choices= HD_Types, null= True, blank=True, default= 'HHD')
    HD_Storage_Other = models.IntegerField(null= True, blank=True)
    GPU = models.CharField(max_length=30)
    Screen_Size = models.CharField(max_length=30, choices= Screen_Sizes)
    Screen_Resulation = models.CharField(max_length=20, choices= Screen_Resulations)
    Cost = models.FloatField()
    Price = models.FloatField()
    # Image = models.ImageField(upload_to='project/new/%y/%m/%d')
    Description = models.TextField(null= True, blank= True)
    DateTime = models.DateTimeField(default= datetime.now())
    Avilable_on_stock = models.BooleanField(default= False)
    Avilable_on_store = models.BooleanField(default= False)
    Quantity = models.IntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(100)])
    Slug= models.SlugField(null= True, blank= True)
    
    def save(self, *args, **kwargs):
        self.Slug= slugify(f"{self.Brand, self.Model}")
        super(Laptops, self).save(*args, **kwargs)
        
    # def get_absolute_url(self):
    #     return reverse("appname:urlname", kwargs={"slug": self.Slug})
    
    def __str__(self):
        return f"Laptops - {self.Brand} {self.Model}"
    
    

### RAM & Hard Disk Section ###
class ram(Categories):
    RAM_Condition = (
        ('New', 'New'),
        ('Used', 'Used'),
    )
    RAM_Type = (
        ('DDR3', 'DDR3'),
        ('DDR3L', 'DDR3L'),
        ('DDR4', 'DDR4'),
        ('DDR5', 'DDR5'),
     )
    RAM_Size = (
        ('4', '4'),
        ('8', '8'),
        ('16', '16'),
        ('32', '32'),
        ('64', '64'),
    )
    Brand = models.CharField(max_length=50, default="Unknown")
    Condition = models.CharField(max_length=50,choices= RAM_Condition)
    Type = models.CharField(max_length=20, choices= RAM_Type)
    Size = models.CharField(max_length=100, choices= RAM_Size)
    Speed = models. IntegerField()
    Quantity = models.IntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(1000)])
    Cost = models.IntegerField()
    Price = models.IntegerField()
    Available = models.BooleanField(default= True)
    DateTime = models.DateTimeField(default= datetime.now())
    Description = models.TextField(null= True, blank= True)
    def __str__(self):
        return f"ram - {self.Type}-{self.Size}-{self.Speed}-{self.Condition}"
class hard(Categories):
    Hard_Condition = (
        ('New', 'New'),
        ('Used', 'Used'),
    )
    Hard_Type = (
        ('HDD', 'HDD'),
        ('SSD SATA 2.5', 'SSD SATA 2.5'),
        ('SSD M.2', 'SSD M.2'),
        ('SSD NVMe', 'SSD NVMe'),
        ('SSD PCIe', 'SSD PCIe'),
    )
    Brand = models.CharField(max_length=50, default="Unknown")
    Condition = models.CharField(max_length=50, choices= Hard_Condition)
    Type = models.CharField(max_length=20, choices= Hard_Type)
    Size = models.IntegerField()
    Quantity = models.IntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(10000)])
    Cost = models.IntegerField()
    Price = models.IntegerField()
    Available = models.BooleanField(default= True)
    DateTime = models.DateTimeField(default= datetime.now())
    Description = models.TextField(null= True, blank= True)
    def __str__(self):
        return f"hard - {self.Size}-{self.Type}-{self.Condition}"