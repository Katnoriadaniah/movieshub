from django import forms
from .models import Post

choices = [('Hollywood', 'Hollywood'), ('Bollywood', 'Bollywood'), ('South', 'South')]


class postform(forms.ModelForm):
	class Meta:
		model = Post
		fields =('title', 'image', 'link', 'category')


		widget ={
			'title':forms.TextInput(attrs={'class': 'form-control'}),
			'category':forms.Select(choices=choices, attrs={'class': 'form-control'}),



		}