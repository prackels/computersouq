from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify
from datetime import datetime
from django.core.validators import MinLengthValidator, RegexValidator
from category.models import Categories

class invoice(models.Model):
    Payments= (('Cash' ,'كاش'),
               ('Visa' ,'ڤيزا'),
               )
    id = models.AutoField(primary_key=True)
    Name= models.CharField(max_length= 100)
    Phone_Number = models.CharField('Phone', max_length=11, validators=[RegexValidator(r'^\d{1,11}$'), MinLengthValidator(11)])
    Products = models.ManyToManyField(Categories)
    Quantity= models.IntegerField(default= 1)
    Ram= models.IntegerField(validators=[MaxValueValidator(128)])
    DateTime = models.DateTimeField(default= datetime.now())
    Slug= models.SlugField
    Payment= models.CharField(max_length=50,choices= Payments)
    def __str__(self):
        return f"{self.Name}"
    def save(self, *args, **kwargs):
        self.Slug= slugify(f"{self.Name} - {self.id}")
        super(invoice, self).save(*args, **kwargs)



class Creditor_debtor_accounts(models.Model):
    id = models.AutoField(primary_key=True)
    Name= models.CharField(max_length=100)
    Phone_Number= models.CharField('Phone', max_length=11, validators=[RegexValidator(r'^\d{1,11}$'), MinLengthValidator(11)])
    address= models.CharField(max_length=500, verbose_name= "العنوان و اسم المكان")
    def __str__(self):
        return self.Name
class transaction(Creditor_debtor_accounts):
    account= models.ForeignKey(Creditor_debtor_accounts, on_delete= models.CASCADE)
    Products = models.ManyToManyField(Categories)
    creditor = models.FloatField(verbose_name= "دائن")
    debitor = models.FloatField(verbose_name= "مدين")
    amount= models.FloatField(verbose_name= "السعر الكلي")
    def __str__(self):
        return self.account.Name