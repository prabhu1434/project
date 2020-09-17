from django import forms
from .models import *

class employee(forms.ModelForm):
    class Meta:
        model=employee_details
        fields={'firstname','lastname','date','gender','phone_no','mail_id'}
        widgets={
            'firstname':forms.TextInput(attrs={'class':'form-control','placeholder':'FIRSTNAME'}),
            'lastname':forms.TextInput(attrs={'class':'form-control','placeholder':'LASTNAME'}),
            'date':forms.DateInput(format=('%d-%m-%Y'),attrs={'type':'date','class': 'form-control'}),
            'gender':forms.RadioSelect(choices=gender_choices,attrs={}),
            'phone_no':forms.TextInput(attrs={'class':'form-control','placeholder':'PHONE NUMBER'}),
            'mail_id':forms.TextInput(attrs={'class':'form-control','placeholder':'MAIL ID'}),
        }

class education(forms.ModelForm):
    class Meta:
        model=education_details
        fields={'qualification','institute','year','percent'}
        widgets={
            'qualification':forms.TextInput(attrs={'class':'form-control'}),
            'institute':forms.TextInput(attrs={'class':'form-control'}),
            'year':forms.TextInput(attrs={'class':'form-control'}),
            'percent':forms.TextInput(attrs={'class':'form-control'}),
            }

class experience(forms.ModelForm):
    class Meta:
        model=experience_details
        fields={'company','from_date','to_date','position','reason'}
        widgets={
            'company':forms.TextInput(attrs={'class':'form-control'}),
            'from_date':forms.DateInput(format=('%d-%m-%Y'),attrs={'type':'date','class': 'form-control'}),
            'to_date':forms.DateInput(format=('%d-%m-%Y'),attrs={'type':'date','class': 'form-control'}),
            'position':forms.TextInput(attrs={'class':'form-control'}),
            'reason':forms.TextInput(attrs={'class':'form-control'}),
            }

class other(forms.ModelForm):
    class Meta:
        model=other_details 
        fields={'fathername','mothername','address','city','pincode','aadhar_no','license_1','contact_name','contact_no'}
        widgets={
            'fathername':forms.TextInput(attrs={'class':'form-control','placeholder':'FATHERNAME'}),
            'mothername':forms.TextInput(attrs={'class':'form-control','placeholder':'MOTHERNAME'}),
            'address':forms.Textarea(attrs={'class':'form-control','placeholder':'ADDRESS','rows':'5'}),
            'city':forms.TextInput(attrs={'class':'form-control','placeholder':'CITY'}),
            'pincode':forms.TextInput(attrs={'class':'form-control','placeholder':'PINCODE'}),
            'aadhar_no':forms.TextInput(attrs={'class':'form-control','placeholder':'AADHAR NUMBER'}),
            'license_1':forms.TextInput(attrs={'class':'form-control','placeholder':'DRIVING LICENSE'}),
            'contact_name':forms.TextInput(attrs={'class':'form-control','placeholder':'EMERGENCY CONTACT NAME'}),
            'contact_no':forms.TextInput(attrs={'class':'form-control','placeholder':'EMERGENCY CONTACT NUMBER'}),           
        }

class salary(forms.ModelForm):
    class Meta:
        model=salary_details
        fields={'designation','date_join','salary'}
        widgets={
            'designation':forms.TextInput(attrs={'class':'form-control','placeholder':'DESIGNATION'}),
            'date_join':forms.DateInput(format=('%d-%m-%Y'),attrs={'type':'date','class': 'form-control'}),
            'salary':forms.TextInput(attrs={'class':'form-control','placeholder':'SALARY'}),                    
        }

class account(forms.ModelForm):
    class Meta:
        model=account_details
        fields={'account_no','ifsc','bankname','bankaddress'}
        widgets={
            'account_no':forms.TextInput(attrs={'class':'form-control','placeholder':'ACCOUNT NUMBER'}),
            'ifsc':forms.TextInput(attrs={'class':'form-control','placeholder':'IFSC CODE'}),
            'bankname':forms.TextInput(attrs={'class':'form-control','placeholder':'BANK NAME'}),
            'bankaddress':forms.TextInput(attrs={'class':'form-control','placeholder':'BANK ADDRESS'}),
        }





