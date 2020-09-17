from django.db import models

gender_choices =(
    ("MALE","MALE"),
    ("FEMALE","FEMALE"),
    ("OTHERS","OTHERS")
)

class employee_details(models.Model):
    employee_id=models.CharField(max_length=100,null=True)
    firstname=models.CharField(max_length=100,null=True)
    lastname=models.CharField(max_length=100,null=True)
    date=models.CharField(max_length=100,null=True)
    gender=models.CharField(max_length=20,choices=gender_choices,default='FEMALE')
    phone_no=models.CharField(max_length=100,null=True)
    mail_id=models.CharField(max_length=100,null=True)

class education_details(models.Model):
    employee_id=models.CharField(max_length=100,null=True)
    qualification=models.CharField(max_length=100,null=True)
    institute=models.CharField(max_length=100,null=True)
    year=models.IntegerField(null=True)
    percent=models.IntegerField(null=True)

class experience_details(models.Model):
    employee_id=models.CharField(max_length=100,null=True)
    company=models.CharField(max_length=100,null=True)
    from_date=models.CharField(max_length=100,null=True)
    to_date=models.CharField(max_length=100,null=True)
    position=models.CharField(max_length=100,null=True)
    reason=models.CharField(max_length=100,null=True)

class other_details(models.Model):
    employee_id=models.CharField(max_length=100,null=True)    
    fathername=models.CharField(max_length=100,null=True)
    mothername=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100,null=True)
    city=models.CharField(max_length=100,null=True)
    pincode=models.CharField(max_length=100,null=True)    
    aadhar_no=models.CharField(max_length=100,null=True)
    license_1=models.CharField(max_length=100,null=True)
    contact_name=models.CharField(max_length=100,null=True)
    contact_no=models.CharField(max_length=100,null=True)

class salary_details(models.Model):
    employee_id=models.CharField(max_length=100,null=True)    
    designation=models.CharField(max_length=100,null=True)
    date_join=models.CharField(max_length=100,null=True)
    salary=models.CharField(max_length=100,null=True)

class account_details(models.Model):
    employee_id=models.CharField(max_length=100,null=True)    
    account_no=models.CharField(max_length=100,null=True)
    ifsc=models.CharField(max_length=100,null=True)
    bankname=models.CharField(max_length=100,null=True)
    bankaddress=models.CharField(max_length=100,null=True)
    


    
    



    
    
    