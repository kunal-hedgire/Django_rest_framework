from django import forms
GENDER_CHOICES = (
    ('Male',  'Male'),
    ('Female','Female'),
    ('Other', 'Other')
)

class StudentForm(forms.Form):
    First_Name = forms.CharField(max_length=20,label='First Name',help_text="First Name")
    Last_Name = forms.CharField(max_length=20,label='Last Name',help_text='Last Name')
    Email = forms.EmailField()
    Age = forms.IntegerField(label='Age',help_text='Age')
    Mobile = forms.IntegerField(label='Mobile Number',help_text='Mobile Numnber')
    Gender  = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    Remarks = forms.CharField(widget=forms.Textarea(attrs={'cols':40,'rows': 10}))
    # skills - - checkbox
    # country - - dropdown
    #widgets = { 'Remarks': forms.Textarea(attrs={'cols': 80, 'rows': 20})}

    #created_at = forms.DateTimeField(auto_now_add=True)
    #updated_at = forms.DateTimeField(auto_now=True)

class IDForm(forms.Form):
    id=forms.IntegerField()