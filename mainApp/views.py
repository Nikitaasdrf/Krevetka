from django.shortcuts import render
from .models import *
from django.views.generic import View
from django.http import JsonResponse
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from .data import *
import json
from django.utils.timezone import datetime, timedelta

class AjaxHomePage(View):
    def get(self, request):
        Check = request.GET.get('check')
        if request.user.is_authenticated:
            user1 = request.user.id
            if Check == 'pageonload':
                ItemCount = AddProduct.objects.filter(User_id = user1).count()
                context = {'ItemCount': ItemCount}
                return JsonResponse(context, status=200)
        else:
            if Check == 'pageonload':
                x = json.loads(request.COOKIES['addProduct'])
                context = cokkiereload(x)
                return JsonResponse(context, status=200)
        hometop = FishProduct.objects.filter(ProductStatus = 'Топ')
        context = {'hometop': hometop}
        return render(request, 'mainApp/homePage.html', context)


class AjaxFish(View):
    def get(self, request):
        Check = request.GET.get('check')
        if request.user.is_authenticated:
            user1 = request.user.id
            PictureURL = request.GET.get('pictureurl')
            ProductName = request.GET.get('productname')
            ProductCount = request.GET.get('productcount')
            ProductPrice = request.GET.get('productprice')
            ProductID = request.GET.get('productid')
            if Check == 'additem':
                ProductCount = round(EnterDollarfun(ProductCount))
                ProductPrice = Pricenumbertransform(ProductPrice)
                ProductBuyModels = AddProduct.objects.filter(User_id=user1, ProductID=ProductID)
                ExistingUnits = [];
                if user1 != None:
                    if ProductBuyModels:
                        for el in ProductBuyModels:
                            ExistingUnits.append(el.ProductCount);
                        ExistingUnits = ExistingUnits[0]; ExistingUnits = EnterDollarfun(ExistingUnits)
                        NewUnits = ExistingUnits + ProductCount; NewUnits= round(NewUnits)
                        AddProduct.objects.filter(User_id=user1, ProductID=ProductID).update(ProductCount=NewUnits)
                    else:
                        AddProduct.objects.create(User_id=user1, PictureURL=PictureURL, ProductName=ProductName, ProductCount=ProductCount,  ProductPrice=ProductPrice, ProductID=ProductID)
                ItemCount = AddProduct.objects.filter(User_id = user1).count()
                context = {'ItemCount': ItemCount}
                return JsonResponse(context, status=200)
            if Check == 'pageonload':
                ItemCount = AddProduct.objects.filter(User_id = user1).count()
                context = {'ItemCount': ItemCount}
                return JsonResponse(context, status=200)
        else:
            if Check == 'pageonload':
                x = json.loads(request.COOKIES['addProduct'])
                context = cokkiereload(x)
                return JsonResponse(context, status=200)
            if Check == 'additem':
                x = json.loads(request.COOKIES['addProduct'])
                context = cokkiereload(x)
                return JsonResponse(context, status=200)
        fish = FishProduct.objects.filter(ProductType = 'Рыба')
        context = {'fish': fish}
        return render(request, 'mainApp/fish.html', context)


class AjaxShrimp(View):
    def get(self, request):
        Check = request.GET.get('check')
        if request.user.is_authenticated:
            user1 = request.user.id
            if Check == 'pageonload':
                ItemCount = AddProduct.objects.filter(User_id = user1).count()
                context = {'ItemCount': ItemCount}
                return JsonResponse(context, status=200)
        else:
            if Check == 'pageonload':
                x = json.loads(request.COOKIES['addProduct'])
                context = cokkiereload(x)
                return JsonResponse(context, status=200)
        shrimp = FishProduct.objects.filter(ProductType = 'Креветки')
        context = {'shrimp': shrimp}
        return render(request, 'mainApp/shrimp.html', context)


class AjaxSeafood(View):
    def get(self, request):
        Check = request.GET.get('check')
        if request.user.is_authenticated:
            user1 = request.user.id
            if Check == 'pageonload':
                ItemCount = AddProduct.objects.filter(User_id = user1).count()
                context = {'ItemCount': ItemCount}
                return JsonResponse(context, status=200)
        else:
            if Check == 'pageonload':
                x = json.loads(request.COOKIES['addProduct'])
                context = cokkiereload(x)
                return JsonResponse(context, status=200)
        seafood = FishProduct.objects.filter(ProductType = 'Морепродукты')
        context = {'seafood': seafood}
        return render(request, 'mainApp/seafood.html', context)


class AjaxCrab(View):
    def get(self, request):
        Check = request.GET.get('check')
        if request.user.is_authenticated:
            user1 = request.user.id
            if Check == 'pageonload':
                ItemCount = AddProduct.objects.filter(User_id = user1).count()
                context = {'ItemCount': ItemCount}
                return JsonResponse(context, status=200)
        else:
            if Check == 'pageonload':
                x = json.loads(request.COOKIES['addProduct'])
                context = cokkiereload(x)
                return JsonResponse(context, status=200)
        crab = FishProduct.objects.filter(ProductType = 'Краб')
        context = {'crab': crab}
        return render(request, 'mainApp/crab.html', context)


class AjaxCaviar(View):
    def get(self, request):
        Check = request.GET.get('check')
        if request.user.is_authenticated:
            user1 = request.user.id
            if Check == 'pageonload':
                ItemCount = AddProduct.objects.filter(User_id = user1).count()
                context = {'ItemCount': ItemCount}
                return JsonResponse(context, status=200)
        else:
            if Check == 'pageonload':
                x = json.loads(request.COOKIES['addProduct'])
                context = cokkiereload(x)
                return JsonResponse(context, status=200)
        caviar = FishProduct.objects.filter(ProductType = 'Икра')
        context = {'caviar': caviar}
        return render(request, 'mainApp/caviar.html', context)


class AjaxAbout(View):
    def get(self, request):
        Check = request.GET.get('check')
        if request.user.is_authenticated:
            user1 = request.user.id
            if Check == 'pageonload':
                ItemCount = AddProduct.objects.filter(User_id = user1).count()
                context = {'ItemCount': ItemCount}
                return JsonResponse(context, status=200)
        else:
            if Check == 'pageonload':
                x = json.loads(request.COOKIES['addProduct'])
                context = cokkiereload(x)
                return JsonResponse(context, status=200)
        return render(request, 'mainApp/about.html',)


class AjaxBasket(View):
    def get(self, request):
        Check = request.GET.get('check')
        ProductId = request.GET.get('productidb')
        if request.user.is_authenticated:
            user1 = request.user.id
            ProductCount = request.GET.get('productcountb')
            RemoveItemID = request.GET.get('itemid')
            if Check == 'pageonload':
                ItemCount = AddProduct.objects.filter(User_id = user1).count()
                context = updaterecord(user1, ItemCount)
                return JsonResponse(context, status=200)
            if Check == 'removeitem':
                AddProduct.objects.filter(User_id = user1, ProductID = RemoveItemID).delete()
                ItemCount = AddProduct.objects.filter(User_id = user1).count()
                context = updaterecord(user1, ItemCount)
                return JsonResponse(context, status=200)
            if Check == 'changebasket':
                AddProduct.objects.filter(User_id = user1, ProductID = ProductId).update(ProductCount=int(ProductCount))
                context = changeinput(user1, ProductId)
                return JsonResponse(context, status=200)
        else:
            if Check == 'pageonload':
                x = json.loads(request.COOKIES['addProduct'])
                context = cokkiereload(x)
                return JsonResponse(context, status=200)
            if Check == 'removeitem':
                x = json.loads(request.COOKIES['addProduct'])
                context = cokkiereload(x)
                return JsonResponse(context, status=200)
            if Check == 'changebasket':
                x = json.loads(request.COOKIES['addProduct'])
                context = cokkieChange(x, ProductId)
                return JsonResponse(context, status=200)
        return render(request, 'mainApp/basket.html',)


class AjaxMakingorder(View):
    def get(self, request):
        Check = request.GET.get('check')
        if request.user.is_authenticated:
            user1 = request.user.id
            user_first_name = request.user.first_name
            user_last_name = request.user.last_name
            user_email = request.user.email
            context = {'user_first_name': user_first_name, 'user_last_name': user_last_name, 'user_email': user_email}
            if Check == 'pageonload':
                ItemCount = AddProduct.objects.filter(User_id = user1).count()
                context = updaterecord(user1, ItemCount)
                return JsonResponse(context, status=200)
            if Check == 'clientinfo':
                clientName = request.GET.get('clientname')
                clientsurName = request.GET.get('clientsurname')
                clientPhone = request.GET.get('clientphone')
                clientEmail = request.GET.get('clientemail')
                DeliveryMethod = request.GET.get('deliverymethod')
                clientAddress = request.GET.get('clientaddress')
                addProducts = AddProduct.objects.filter(User_id = user1).all()
                productsName = []
                prcount = []
                prprice = []
                for el in addProducts:
                    prname = str(el.ProductName) + ' - ' + str(el.ProductCount)
                    productsName.append(prname)
                    prcount.append(float(el.ProductCount))
                    prprice.append(float(el.ProductCount) * float(el.ProductPrice))
                prprice = sum(prprice)
                prcount = sum(prcount)
                n = ClientInfo.objects.filter(User_id = user1).count()
                n = n+1
                orderId = datetime.now().strftime("%y%m%d"+str(n))
                dateOrder = datetime.now().strftime("%d-%m-%Y %H:%M")
                dateDone = (datetime.now() + timedelta(days = 3)).strftime("%d-%m-%Y")
                productsName = (', '.join(productsName))
                ClientInfo.objects.create(User_id = user1, NameClient = clientName, SurnameClient = clientsurName, 
                ClientPhone = clientPhone, ClientEmail = clientEmail, DeliveryMethod = DeliveryMethod, ClientAddress = clientAddress, 
                prname = productsName, prcount = prcount, prprice = prprice, dateOrder = dateOrder, orderId = orderId, dateDone = dateDone)
                AddProduct.objects.filter(User_id = user1).delete() 
                context = {'clientName': clientName, 'orderId': orderId,}
                return JsonResponse(context, status=200)
        else:
            if Check == 'pageonload':
                x = json.loads(request.COOKIES['addProduct'])
                context = cokkiereload(x)
                return JsonResponse(context, status=200)
        return render(request, 'mainApp/makingorder.html', context)


class AjaxClientProfile(View):
    def get(self, request):
        Check = request.GET.get('check')
        if request.user.is_authenticated:
            user1 = request.user.id
            user_first_name = request.user.first_name
            user_last_name = request.user.last_name
            ClientInfoNikita = ClientInfo.objects.exclude(statusOrder = "Выполнено").filter(User_id = user1).all()
            ClientInfoNikitaDone = ClientInfo.objects.filter(statusOrder = "Выполнено", User_id = user1).all()
            context = {'ClientInfoNikita': ClientInfoNikita, 'ClientInfoNikitaDone': ClientInfoNikitaDone, 'user_first_name': user_first_name, 'user_last_name': user_last_name,}
            if Check == 'pageonload':
                ItemCount = AddProduct.objects.filter(User_id = user1).count()
                context = updaterecord(user1, ItemCount)
                return JsonResponse(context, status=200)
        else:
            if Check == 'pageonload':
                x = json.loads(request.COOKIES['addProduct'])
                context = cokkiereload(x)
                return JsonResponse(context, status=200)
        return render(request, 'mainApp/clientprofile.html', context)

class AjaxProfileAdmin(View):
    def get(self, request):
        Check = request.GET.get('check')
        if request.user.is_authenticated:
            user1 = request.user.id
            if Check == 'pageonload':
                ItemCount = AddProduct.objects.filter(User_id = user1).count()
                context = updaterecord(user1, ItemCount)
                return JsonResponse(context, status=200)
            if Check == 'pageonloadfinalorder':
                ClientInfoNikita = list(ClientInfo.objects.exclude(statusOrder = "Выполнено").values())
                ClientInfoNikitaDone = list(ClientInfo.objects.filter(statusOrder = "Выполнено").values())
                context = {'ClientInfoNikita': ClientInfoNikita, 'ClientInfoNikitaDone': ClientInfoNikitaDone}
                return JsonResponse(context, status=200)
            if Check == 'removefinalorder':
                delbtnId = request.GET.get('delbtnid')
                ClientInfo.objects.filter(User_id = user1, orderId = delbtnId).delete()
                ClientInfoNikita = list(ClientInfo.objects.exclude(statusOrder = "Выполнено").values())
                context = {'ClientInfoNikita': ClientInfoNikita}
                return JsonResponse(context, status=200)
            if Check == 'newdate':
                dateId = request.GET.get('dateid')
                valDate = request.GET.get('valdate')
                ClientInfo.objects.filter(orderId = dateId).update(dateDone = valDate)
                context = {'valDate': valDate}
                return JsonResponse(context, status=200)
            if Check == 'newstatus':
                statusVal = request.GET.get('statusval')
                statusId = request.GET.get('statusid')
                colorStatus = request.GET.get('colorstatus')
                ClientInfo.objects.filter(orderId = statusId).update(statusOrder = statusVal,statusColor = colorStatus)
                ClientInfoNikita = list(ClientInfo.objects.exclude(statusOrder = "Выполнено").values())
                ClientInfoNikitaDone = list(ClientInfo.objects.filter(statusOrder = "Выполнено").values())
                context = {'ClientInfoNikita': ClientInfoNikita, 'ClientInfoNikitaDone': ClientInfoNikitaDone}
                return JsonResponse(context, status=200)
        else:
            if Check == 'pageonload':
                x = json.loads(request.COOKIES['addProduct'])
                context = cokkiereload(x)
                return JsonResponse(context, status=200)
        return render(request, 'mainApp/profileadmin.html',)

class AjaxPageOne(View):
    def get(self, request):
        Check = request.GET.get('check')
        if Check == 'nikita':
             inputNikita1 = request.GET.get('inputnikita1')
             Test.objects.create(Input1 = inputNikita1)
             test = list(Test.objects.values())
             context = {'test': test}
             return JsonResponse(context, status=200)
        if Check == 'pageonloadnikita':
             test = list(Test.objects.values())
             context = {'test': test}
             return JsonResponse(context, status=200)
        return render(request, 'mainApp/pageone.html',)

class AjaxPageTwo(View):
    def get(self, request):
        return render(request, 'mainApp/pagetwo.html',)