from django import forms
from .models import Commande, Products



class CmdForm(forms.ModelForm):
	class Meta:
		model = Commande
		fields = ['product','productype','tags']
		CTR_CHOICES = (
			('', ''),
			('Médicament','Médicament'),
			('Article','Article'),
			('Autres','Autres'))

		TAG_CHOICES = (
			('',''),
			('Rupture','Zéro Stock'),
			('Faible','Faible Stock'),
			('Ord','Ord')
			)
		labels = {
			'product':('Nom de produit'),
			'productype' : ('Le type de produit'),
			'tags' : ('Tager le produit'),
			'username' : ('Le Nom d\'utilisateur')
		}
		widgets = {
			'product': forms.TextInput(attrs={
			'id' : 'product',
			'class' : 'form-control ',
			'placeholder': 'Nom de Produit',
			'autofocus': 'True',
			'list' : 'products'

			}),
			'productype' : forms.Select(choices= CTR_CHOICES, attrs = {
				'id' : 'type',
				'class' : 'form-control ',
				'placeholder': 'Type De Produit'
				}),
			'tags' : forms.Select(choices= TAG_CHOICES, attrs={
				'id' : 'tag',
				'class' : 'form-control ',
				'placeholder': 'Tag de Produit'
				})

		}

class addForm(forms.ModelForm):
	class Meta:
		model = Products
		fields = ['product', 'tag', 'ppa','marge','pu']
		CTR_CHOICES = (
			('', ''),
			('Médicament','Médicament'),
			('Article','Article'),
			('Autres','Autres'))

		widgets ={
			'product' : forms.TextInput(attrs={
				'id' : 'prd',
				'class' : 'input'
				}),
			'tag' : forms.Select(choices=CTR_CHOICES, attrs={
				'id' : 'slctag',
				'class' : 'input',
				})
		}