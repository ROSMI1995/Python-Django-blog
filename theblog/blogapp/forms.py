from django import forms
from  .models import Post, Category, Comment


#choices = [( 'Diet', 'Diet'), ('Excercise', 'Excercise'),('Food', 'Food'), ('Nutrients', 'Nutrients')]

choices = Category.objects.all().values_list('name', 'name')

choices_list = []
for item in choices:
	choices_list.append(item)

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title',  'author', 'category', 'body', 'status', 'image')

		widgets = {
			'title' : forms.TextInput(attrs={'class': 'form-control'}),
			#'slug' : forms.TextInput(attrs={'class': 'form-control'}),
			'author' : forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id': 'user', 'type': 'hidden'}),
			#'author' : forms.Select(attrs={'class': 'form-control'}),
			'category' : forms.Select(choices=choices_list, attrs={'class': 'form-control'}),
			'body' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Minimum 300 characters required'}),
			'status' : forms.Select(attrs={'class': 'form-control'}),

		}
		#exclude auther name

class EditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'category', 'body', 'status')
		widgets = {
			'title' : forms.TextInput(attrs={'class': 'form-control'}),
			#'slug' : forms.TextInput(attrs={'class': 'form-control'}),
			#'author' : forms.Select(attrs={'class': 'form-control'}),
			'category' : forms.Select(choices=choices_list,attrs={'class': 'form-control'}),
			'body' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Minimum 300 characters required'}),
			'status' : forms.Select(attrs={'class': 'form-control'}),

		}

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields =('name', 'body')
		widgets = {
			'name' : forms.TextInput(attrs={'class': 'form-control'}),
			'body' : forms.Textarea(attrs={'class': 'form-control'})
			
		}

	