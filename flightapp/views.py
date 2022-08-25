from uuid import uuid4

from django.db.models import Sum
from django.conf import settings
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from flightapp.models.cart import Cart
from flightapp.models.products import Brand
from flightapp.models.products import Banner
from flightapp.models.products import Products
from flightapp.models.products import BannerLefts
from flightapp.models.products import FeatureRights

from flightapp.models.category import Categories
from flightapp.models.order_history import OrderHistory

# from flightapp.utils import send_message
from flightapp.utils import searchHelper
# from flightapp.utils import categWishlistHelper
# from flightapp.libs.telegram import telebot


def homeView(request):
    day_recommends = Products.objects.filter(
        category=Categories.KUN_TAKLIFLARI)  # kunning eng yaxhi takliflari
    best_seller = Products.objects.filter(
        category=Categories.ENG_KOP_SOTILADIGAN)  # eng ko'p sotiladigan
    devices = Products.objects.filter(
        category=Categories.SIZ_UCHUN_TAVFSIYA)  # eng mashhur mahsulotlar
    _all_products = Products.objects.exclude(category__in=[
        Categories.ENG_KOP_SOTILADIGAN,
        Categories.KUN_TAKLIFLARI])

    dbctx: dict = {}
    # myctx: dict = categWishlistHelper(request)
    dbctx["best_seller"] = best_seller
    dbctx["all_products"] = _all_products
    dbctx['day_recommends'] = day_recommends
    dbctx["devices"] = devices

    banners = Banner.objects.all()
    products = Products.objects.all()
    bannerleft = BannerLefts.objects.all()
    features = FeatureRights.objects.all()
    brand = Brand.objects.all()
    context: dict = {**dbctx, 'products': products, 'banners': banners,
                     'bannerleft': bannerleft, 'features': features, 'brand': brand}

    return render(request, 'home/index.html', context)

 
def aboutView(request):
    return render(request, 'about/about.html')


def shopView(request):
    return render(request, 'shop/shop.html')


def shopdetailView(request):
    # context: dict = categWishlistHelper(request)
    # context["items"]=Products.objects.get(id=id)
    return render(request, 'shop/detail.html')




def contactView(request):
    return render(request, 'contact/contact.html')
