from django.views import View
from django.shortcuts import render, redirect
from ..models.product import Product
from ..models.catagory import Catagory

from ..models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password


class IndexView(View):
    def get(self,request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart']={}
        template_name = 'stores/index.html'
        product_data = None
        catagories = Catagory.objects.all()
        catagoryID = request.GET.get('catagory')
        if catagoryID:
            product_data = Product.objects.filter(catagory=catagoryID)

        else:
            product_data = Product.objects.all()
        data = {}
        data['products'] = product_data
        data['catagories'] = catagories
        print('You are:',request.session.get('email'))
        context = {'product_data': product_data, 'catagories': catagories, 'data': data}
        return render(request, template_name, context)

    # cart elements addition code
    # when user press add to card button then automatically element has been added into cart
    def post(self,request):
        remove=False
        products=request.POST.get('product')
        remove=request.POST.get('remove')
        # print('remove*********-->',remove,products)
        cart = request.session.get('cart')
        if cart:
            quantity=cart.get(products)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(products)
                    else:
                        cart[products]=quantity-1
                else:
                    # print('add functionality called')
                    cart[products] = quantity + 1
            else:
                cart[products]=1
        else:
            cart={}
            cart[products]=1
        request.session['cart']=cart
        print('cart details ==========',cart)
        return redirect('home_url')


        # if cart:
        #     quantity = request.session['cart'][products]
        #     print('quantity-->',quantity)
        #     if quantity:
        #         cart[products]=int(quantity)+1
        #     else:
        #         cart[products] =  1
        #
        # else:
        #     print('cart is not available')
        #     cart={}
        #     cart[products] = products
        #
        # request.session['cart']=cart
        # print(cart)
        # return redirect('home_url')




# function based view
# def index_view(request):
#     print('index view called---------------')
#     template_name = 'stores/index.html'
#     product_data =None
#     catagories = Catagory.objects.all()
#     catagoryID = request.GET.get('catagory')
#     if catagoryID:
#         product_data=Product.objects.filter(catagory=catagoryID)
#
#     else:
#         product_data = Product.objects.all()
#     data={}
#     data['products']=product_data
#     data['catagories']=catagories
#     context={'product_data':product_data,'catagories':catagories,'data':data}
#     return render(request,template_name,context)