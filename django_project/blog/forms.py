from django import forms
from .models import Course,Student
from django.forms import ModelForm;


class CourseRegisterForm(forms.ModelForm):
    

    class Meta:
        model = Course
        fields = '__all__'
class StudentMarksForm(forms.ModelForm):
    

    class Meta:
        model = Student
        fields = '__all__'