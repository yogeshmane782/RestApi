from api.models import Student 
from django.forms import ModelForm
from django.forms import forms
class StudentForm(ModelForm):
    class Meta:
        model=Student 
        fields="__all__"
    def clean_course(self):
        course=self.cleaned_data['course']
        if course not in ["java","python",".net"]:
            raise forms.ValidationError("Course Must be java,python or .net")
        else:
            return course 