from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Category, Contact, Index, Single, Feature, LatestNews, Biz, Sen, Lorem, Tranding, Image, Busin, Picture, Sit, Ipsum
from .forms import ContactForm, NewsletterForm

# Create your views here.
def category(request):
    category = Category.objects.all()
    tranding = Tranding.objects.all()
    image = Image.objects.all()
    busin = Busin.objects.all()
    picture = Picture.objects.all()
    sit = Sit.objects.all()
    news = NewsletterForm(request.POST or None)
    if request.method == "POST" and news.is_valid():
        news.save()
        return HttpResponse("<h1>Formangiz qabul qilindi</h1>")
    context = {
        'category': category,
        'tranding': tranding,
        'news': news,
        'image': image,
        'busin': busin,
        'picture': picture,
        'sit': sit
    }
    return render(request, 'category.html', context=context)

def contact(request):
    form = ContactForm(request.POST or None)
    print("Malumotlar -- >", form)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h1>Formangiz qabul qilindi</h1>")
    contact = Contact.objects.all()
    context = {
        'form': form
    }
    return render(request, 'contact.html', context=context)

def index(request):
    feature = Feature.objects.all()
    latestNews = LatestNews.objects.all()
    biz = Biz.objects.all()
    sen = Sen.objects.all()
    lorem = Lorem.objects.all()
    news = NewsletterForm(request.POST or None)
    if request.method == "POST" and news.is_valid():
        news.save()
        return HttpResponse("<h1>Formangiz qabul qilindi</h1>")
    context = {
        'feature': feature,
        'news': news,
        'latestNews': latestNews,
        'biz': biz,
        'sen': sen,
        'lorem': lorem
    }
    return render(request, 'index.html', context=context)

def single(request):
    single = Single.objects.all()
    ipsum = Ipsum.objects.all()
    news = NewsletterForm(request.POST or None)
    if request.method == "POST" and news.is_valid():
        news.save()
        return HttpResponse("<h1>Formangiz qabul qilindi</h1>")
    context = {
        'single': single,
        'ipsum': ipsum,
        'news': news
    }
    return render(request, 'single.html', context=context)

def featureDetail(requests, id):
    try:
        featuredetail = Feature.objects.get(id=id)
        context = {
            'featuredetail': featuredetail
        }
    except featuredetail.DoesNotExist:
        raise Http404("No product found")

    return render(requests, 'featureDetail.html', context=context)