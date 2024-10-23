from django import forms

class MobileForm(forms.Form):
    brand=forms.CharField()
    
    model=forms.CharField()
    
    release_year=forms.CharField()
    
    price=forms.IntegerField()
    
    
    
    