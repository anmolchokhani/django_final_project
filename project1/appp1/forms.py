from django import forms
from .models import BoxDetails

class BoxDetailsForm(forms.ModelForm):
    
    class Meta:
        model = BoxDetails
        fields = '__all__'
        widgets={
            'name':forms.TextInput(attrs={'placeholder':'Qbox Name*','class':"form-control"}),
            'email':forms.EmailInput(attrs={'placeholder':'Qtrack Email','class':"form-control"}),
            'password':forms.TextInput(attrs={'placeholder':"Qtrack Password",'class':"form-control"}),
            'qbox_no':forms.NumberInput(attrs={'placeholder':'Qbox No*','class':"form-control"}),
            'teleport':forms.TextInput(attrs={'placeholder':"Teleport NodeName",'class':"form-control"}),
            'sudo_password':forms.TextInput(attrs={'placeholder':"Qbox SudoPassword",'class':"form-control"}),
            'source':forms.TextInput(attrs={'placeholder':"Source Name",'class':"form-control"}),
            'apihub':forms.TextInput(attrs={'placeholder':"Apihub Version",'class':"form-control"}),
            'web_frontend':forms.TextInput(attrs={'placeholder':"WebFrontend Version",'class':"form-control"}),
            'checkpoints':forms.TextInput(attrs={'placeholder':"Checkpoints Version",'class':"form-control"}),
            'cxr_api':forms.TextInput(attrs={'placeholder':"CxrApi Version",'class':"form-control"}),
            'additional':forms.TextInput(attrs={'placeholder':"Any Extra Information To Put",'class':"form-control"}),
            'dcmio':forms.TextInput(attrs={'placeholder':"Dcmio Version",'class':"form-control"}),
            
        }
        labels= {'name':'QBox Name', 'email': 'Qtrack Email', 'password':'Qtrack Password', 'qbox_no': 'QBox No',
        'sudo_password':"Sudo Password",'cxr_api':"CxrApi",'web_frontend':"WebFrontend",'additional':'Additional','dcmio':'Dcmio'}
