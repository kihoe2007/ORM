from django.db import models

# Create your models here.
from django.contrib import admin
class Loan(models.Model):
   Loan_id=models.CharField(max_length=30)
   Loan_type=models.CharField(max_length=30)
   Loan_amount=models.FloatField()
   cust_acntno=models.IntegerField()
   cust_name=models.CharField(max_length=50)

class LoanAdmin(admin.ModelAdmin):
    list_display=('Loan_id','Loan_type','Loan_amount','cust_acntno','cust_name')