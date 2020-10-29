from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class RegisterEmployeeForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = Account
        fields=['user_id',]
    def __init__(self, *args, **kwargs):
        super(RegisterEmployeeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class EmployeeLogin(forms.Form):
    user_id = forms.IntegerField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super(EmployeeLogin, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
class DateInput(forms.DateInput):
    input_type = 'date'
class leaveApplyForm(ModelForm):
    class Meta:
        model = TLeave
        fields = ['leave_type','leave_date']
        widgets = {
            'leave_date': DateInput(attrs={'type': 'date'})
        }
    def __init__(self, *args, **kwargs):
        super(leaveApplyForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
class addressForm(ModelForm):
    class Meta:
        model = MAddress
        fields = ['building_details','road','landmark','city','state','country']
    def __init__(self, *args, **kwargs):
        super(addressForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
class paygradeForm(ModelForm):
    class Meta:
        model = MPaygrade
        fields = ['basic_amt','da_amt','pf_amt','medical_amt']
    def __init__(self, *args, **kwargs):
        super(paygradeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
class payForm(ModelForm):
    class Meta:
        model = MPay
        fields = ['fin_year','gross_salary','gross_dedn','net_salary']
    def __init__(self, *args, **kwargs):
        super(payForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
class employeeInfoForm(ModelForm):
    class Meta:
        model = MEmployee
        fields= ['employee_name', 'department', 'company', 'employee_doj', 'grade']
        widgets = {
            'employee_doj': DateInput(attrs={'type': 'date'})
        }
    def __init__(self, *args, **kwargs):
        super(employeeInfoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
class AchievementForm(ModelForm):
    class Meta:
        model =TAchievement
        fields = ['achievement_date','achievement_type']
        widgets = {
            'achievement_date': DateInput(attrs={'type': 'date'})
        }
    def __init__(self, *args, **kwargs):
        super(AchievementForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'