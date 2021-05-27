from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.text import slugify
from PIL import Image
from django.core.validators import MaxValueValidator, MinValueValidator

class Category(MPTTModel):
	title = models.CharField(max_length=200)
	parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
	slug = models.SlugField(unique=True)

	def __str__(self):
		return self.title

	class MPTTMeta:
	    order_insertion_by = ['title']

	def __str__(self):                           
	    full_path = [self.title]            
	    k = self.parent
	    while k is not None:
	        full_path.append(k.title)
	        k = k.parent

	    return ' -> '.join(full_path[::-1])


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

class Product(models.Model):
	KP = 'KP'
	A = 'A'
	B = 'B'
	C = 'C'
	D = 'D'
	E = 'E'
	F = 'F'
	G = 'G'
	J = 'J'
	M = 'M'
	R = 'R'
	LETTERS = [
		(KP, 'KP'),		
		(A, 'A'),
		(B, 'B'),
		(C, 'C'),
		(D, 'D'),
		(E, 'E'),
		(F, 'F'),
		(G, 'G'),
		(J, 'J'),
		(M, 'M'),
		(R, 'R'),
	]
	coin_choice_field = models.CharField(
		max_length=2,
		choices=LETTERS,
		default=KP,
	)
	bundeslandcoin = 'Bundeslandmünze'
	normal = 'Normale Münze'
	sonder = 'Sondermünze'
	COIN_SORT = [
		(KP, 'KP'),
		(bundeslandcoin, 'Bundeslandmünze'),
		(normal, 'Normale Münze'),
		(sonder, 'Sondermünze'),
	]
	coin_sort_field = models.CharField(
		max_length=20,
		choices=COIN_SORT,
		default=KP,
	)
	title  = models.CharField(max_length=120)
	description = models.TextField(blank=True,null=True)
	image = models.ImageField(default='default.jpg', upload_to='coin_pics')
	year = models.PositiveIntegerField(default=2020, validators=[MinValueValidator(1984), max_value_current_year])
	date_found = models.DateTimeField(default=timezone.now)
	category = models.ForeignKey(
	    'Category',
	    related_name="products",
	    on_delete=models.CASCADE
	) 

	def save(self, *args, **kwargs):
	    self.slug = slugify(self.title)
	    super(Product,self).save(*args, **kwargs)

	def get_absolute_url(self):
	    return self.slug