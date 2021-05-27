from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Product
from .filters import ProductFilter

#def coinhome(request):
#    return render(request, 'coincollection/home.html', {'title': 'coinhome'})


def coinhome(request):
    category = Category.objects.all()
    all_products = Product.objects.all().order_by('?')
    page = "somu-overview"
    order = Product.objects.all()
    myFilter = ProductFilter(request.GET, queryset=order)
    order = myFilter.qs
    context={'category':category, 'all_products':all_products, 'order':order, 'myFilter':myFilter}
    return render(request, 'coincollection/home.html',context)


def coinbase(request):
    category = Category.objects.all()
    all_products = Product.objects.all()
    page = "somu-overview"
    order = Product.objects.all()
    myFilter = ProductFilter(request.GET, queryset=order)
    order = myFilter.qs
    context={'category':category, 'all_products':all_products, 'order':order, 'myFilter':myFilter}
    return render(request, 'coincollection/base.html',context)

def country(request,id,slug):
    products = Product.objects.filter(category_id=id) 
    all_products = Product.objects.all()
    catdata = Category.objects.get(pk=id)
    category = Category.objects.all()
    context={'products': products,
             'all_products':all_products, 
             'category':category,
             'catdata':catdata,
             'slug': slug}
    return render(request,'coincollection/country.html',context)

def coin_detail(request,id,slug):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    context = {'product': product,'category': category,
               }
    return render(request,'coincollection/coin_detail.html',context)

def coin_filter(request):
    category = Category.objects.all()
    all_products = Product.objects.all()
    order = Product.objects.all()
    myFilter = ProductFilter(request.GET, queryset=order)
    order = myFilter.qs
    context={'category':category, 'all_products':all_products, 'order':order, 'myFilter':myFilter}
    return render(request,'coincollection/coinfilter.html',context)

def coin_table(request):
    category = Category.objects.all()
    all_products = Product.objects.all()
    order = Product.objects.all()
    myFilter = ProductFilter(request.GET, queryset=order)
    order = myFilter.qs
    context={'category':category, 'all_products':all_products, 'order':order, 'myFilter':myFilter}
    return render(request,'coincollection/listed.html',context)
    
def coin_filtertable(request):
    category = Category.objects.all()
    all_products = Product.objects.all()
    order = Product.objects.all()
    myFilter = ProductFilter(request.GET, queryset=order)
    order = myFilter.qs
    context={'category':category, 'all_products':all_products, 'order':order, 'myFilter':myFilter}
    return render(request,'coincollection/filtertable.html',context)

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def unification_histogram(s):
    d = dict()
    for c in s:
        if c.parent == None:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        else:
            if c.parent not in d:
                d[c.parent] = 1
            else:
                d[c.parent] += 1
    return d

def coin_charts(request):
    all_products = Product.objects.all()
    category = Category.objects.all()
    labels = []
    data = []
    product_listed = []
    #adds hist with number of countries in list for charts
    for prod in all_products:
        product_listed.append(prod.category)
    product_hist = histogram(product_listed)
    for i in product_hist:
        data.append(product_hist[i])
        labels.append(i.title)

    #unified subcountries
    product_listed_unified = []
    labels_unified = []
    data_unified = []
    for prod in all_products:
        product_listed_unified.append(prod.category)
    product_hist_unfied = unification_histogram(product_listed_unified)
    for j in product_hist_unfied:
        data_unified.append(product_hist_unfied[j])
        labels_unified.append(j.title)

    context={'category':category, 'all_products':all_products,'labels': labels, 'data': data, 'labels_unified':labels_unified, 'data_unified':data_unified}
    return render(request, 'coincollection/coin_charts.html', context)