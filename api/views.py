from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import (Product, Discount, Amount)
from . import const
from django.middleware.csrf import rotate_token
from django.views.decorators.csrf import csrf_exempt,ensure_csrf_cookie, get_token
# Create your views here.

# def index(request, slug):
#     def web_view(request):
#     return render(request,'web/home.html',{})
def index(request):
    data = {}
    products = Product.objects.all()
    
    token = get_token(request)
    data = {
        'status': 200,
        'message': 'Get data success!',
        'data': const.to_json(products),
        'discount': const.generate_discount(),
        
    }
    return JsonResponse(data)

def get_all(request):
    data = {}
    obj_products = Product.objects.all()
    # Get amount, discount of product
    # products = get_products(obj_products)
    data = {
        'status': 200,
        'message': 'Get data success!',
        'products': const.get_products(obj_products)
    }
    return JsonResponse(data)


@csrf_exempt #disable csrftoken
def detail(request):
    id = request.POST.get('id','1')
    product = Product.objects.filter(id = id)
    discount = Discount.objects.filter(product = product[0])
    data = {
        'status': 200,
        'message': "Get product sucssess!",
        'discount': const.to_json_detail(discount),
        'amount': 1
    }

    return JsonResponse(data)

    # body = request.POST.get('body', '')
    # body = libs.removed_tags(body)

# return price of amount user input on client
@csrf_exempt
def price_amount(request):
    id = request.POST.get('id', '1')
    amount = int(request.POST.get('amount',1))
    product = Product.objects.filter(id=id)[0]
    discount = Discount.objects.filter(product = product)
    data = {
        'status': 200,
        'message': "Get price with amount success!",
        'amount': amount,
        'price': product.price_num_1,
        'discount': const.to_json_detail(discount),
    }
    if(amount == 1):
        data.update({
            'price': product.price_num_1
        })
    
    elif(amount == 3):
        data.update({
            'price': product.price_num_3
        })
    
    elif(amount>3 and amount<=5):
        data.update({
            'price': product.price_num_5
        })

    elif(amount>5 and amount<=10):
        data.update({
            'price': product.price_num_10
        })
    
    elif(amount>10 and amount<=25):
        data.update({
            'price': product.price_num_25
        })
    
    elif(amount>25 and amount<=50):
        data.update({
            'price': product.price_num_50
        })
    
    elif(amount>50 and amount<=100):
        data.update({
            'price': product.price_num_100
        })
    elif(amount>100 and amount<=200):
        data.update({
            'price': product.price_num_200
        })
    elif(amount>200 and amount<=300):
        data.update({
            'price': product.price_num_300
        })
    
    elif(amount>300 and amount<=500):
        data.update({
            'price': product.price_num_500
        })
    
    elif(amount>500 and amount<=1000):
        data.update({
            'price': product.price_num_1000
        })
    
    elif(amount>1000 and amount<=2000):
        data.update({
            'price': product.price_num_2000
        })
    
    elif(amount>2000 and amount<=3500):
        data.update({
            'price': product.price_num_3500
        })
    
    elif(amount>3500 and amount<=5000):
        data.update({
            'price': product.price_num_5000
        })
    
    elif(amount>5000 and amount<=7500):
        data.update({
            'price': product.price_num_7500
        })
    
    elif(amount>7500 and amount<=10000):
        data.update({
            'price': product.price_num_10000
        })
    
    elif(amount>10000 and amount<=15000):
        data.update({
            'price': product.price_num_15000
        })
    
    elif(amount>15000 and amount<=20000):
        data.update({
            'price': product.price_num_20000
        })
    
    elif(amount>20000 and amount<=40000):
        data.update({
            'price': product.price_num_40000
        })
    
    elif(amount>40000 and amount<=60000):
        data.update({
            'price': product.price_num_60000
        })
    
    elif(amount>40000 and amount<=65000):
        data.update({
            'price': product.price_num_65000
        })
    
    elif(amount>65000 and amount<=90000):
        data.update({
            'price': product.price_num_90000
        })
    
    elif(amount>=90000):
        data.update({
            'price': product.price_num_90000
        })
    return JsonResponse(data)

@csrf_exempt
def get_amount(request):
    amount = request.POST.get('amount', '1')
    discount = request.POST.get('discount', '32000000000')
    id_product = request.POST.get('id', 1)

    return JsonResponse(data)

@csrf_exempt #disable csrftoken
def get_product(request):
    id_pro = request.POST.get('id', '1')
    amount = request.POST.get('amount', '1')
    discount_num = request.POST.get('discount', '32000000000')
    
    data = {
        'status': 200,
        'message': "Get product detail success!"
    }
    if(Product.objects.filter(id = id_pro).count()>0):
        
        product = Product.objects.filter(id = id_pro)[0]
    
        obj_discount = Discount.objects.filter(product = product)[0]
        obj_amount = Amount.objects.filter(product = product).order_by('name')[0]
        # filter_amount(product)
        data.update({
            # 'data': const.convert_amount_to_json(product)
            'retail_price': obj_amount.price_of,
            'price': filter_amount(product, amount),
            'discount': find_discount(discount_num, obj_discount),
            'discount_num': discount_num,
            'amount': amount,
        })
    else:
        data.update({
            'status': 400,
            'message': 'Error!'
        })

    
    return JsonResponse(data)

def find(arr, num):
    result = 1
    # for i in range(len(arr)):
    #     j=i
    #     if(i>1):
    #         j = i-1
    #     if(arr[i]== num):
    #         result = arr[i]
    #     elif(i>1 and num>arr[j] and num<arr[i]):
    #         result=arr[j]
    arr.sort()
    print(arr)

    for index in range(len(arr)):
        next = index +1
       
        if (num < min(arr)):
            result = min(arr)
            break
        if(next <= len(arr)):
            if(arr[index]<=num and num<arr[next]):
                result = arr[index]
                break
            
            # elif(num== arr[index]):
            #     result = arr[index]
            #     break
            elif(num >= max(arr)):
                result = max(arr)
                break
                
    return result
    

def filter_amount(product, amount):
    amounts = Amount.objects.filter(product = product)
    result = 1
    arr = []
    for item in amounts:
        arr.append(int(item.name))

    amount_range = find(arr, int(amount))
    for item in amounts:
        if(int(item.name) == amount_range):
            result = item.price_of
    return result
    # print(findElement(arr, len(arr)))
    
def find_discount(discount, obj):
    discount = int(discount)
    result = 0
    if(discount == 32000000000):
        result = obj.discount_32b
    elif(discount == 16000000000):
        result = obj.discount_16b
    elif(discount == 8000000000):
        result = obj.discount_8b
    elif(discount == 4000000000):
        result = obj.discount_4b
    elif(discount == 2000000000):
        result = obj.discount_2b
    elif(discount == 1000000000):
        result = obj.discount_1b
    elif(discount == 500000000):
        result = obj.discount_500m
    elif(discount == 300000000):
        result = obj.discount_300m
    elif(discount == 150000000):
        result = obj.discount_150m
    elif(discount == 60000000):
        result = obj.discount_60m
    elif(discount == 30000000):
        result = obj.discount_30m
    elif(discount == 10000000):
        result = obj.discount_10m
    return result