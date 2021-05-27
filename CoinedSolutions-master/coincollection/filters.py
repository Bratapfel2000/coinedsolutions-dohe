import django_filters

from .models import *

class ProductFilter(django_filters.FilterSet):
	coin_choice_field = django_filters.ChoiceFilter(label='Buchstabe',choices=Product.LETTERS)        
	coin_sort_field = django_filters.ChoiceFilter(label='Münzart',choices=Product.COIN_SORT)       
	year = django_filters.CharFilter(label='Jahr')    
 
	class Meta:
		model = Product
		exclude = ['image']
		#fields = '__all__'
		fields =  ['coin_choice_field','coin_sort_field', 'year','category']

