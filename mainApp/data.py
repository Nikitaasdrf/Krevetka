from .models import *

def ZeroRemovalfun(ZR):
    if ZR < 0:
        ZR = 0
    else:
        ZR = ZR
    return ZR

def Pricenumbertransform(NewID):
    try:
        NewID= str(NewID.replace(' ₽/кг',''))
    except:
        NewID = str(NewID.replace(' ₽/шт',''))
    return NewID

def EnterDollarfun(D):
    if D == "":
        D = float(0)
    else:
        try:
            D = str(D.replace('$',''))
        except:
            D = float(0)
    if D == "":
        D = float(0)
    else:
        try:
            D = float(D.replace(',',''))
        except:
            D = float(0)
    return D

def ceilround(A):
    if A%1 > 0:
        A = A - (A - A//1) + 1
    else:
        A = A
    return A

def floorround(A):
    if A%1 > 0:
        A = A - (A - A//1)
    else:
        A = A
    return A

def EfTfun(BT, T):
    if BT == 0:
        Ef_T = float(0)
    else:
        Ef_T = float(T)/float(BT)*100
        Ef_T = round(Ef_T, 2)
    return Ef_T

def updaterecord(user1, ItemCount):
    if ItemCount == 1: ItemWord = ' товар'
    elif 1 < ItemCount <= 4: ItemWord = ' товара'
    else: ItemWord = ' товаров'
    AddProductsDictLst = list(AddProduct.objects.filter(User_id=user1).values())
    TotlKgLst = []; TotlPriceLst = []
    for el in AddProductsDictLst: 
        TotlKgLst.append(int(el.get('ProductCount')))
        TotlPriceLst.append(int(el.get('ProductPrice')) * int(el.get('ProductCount')))
    TotlKg = sum(TotlKgLst)
    TotlPrice = sum(TotlPriceLst)
    context = {'AddProductsDictLst': AddProductsDictLst, 'ItemCount': ItemCount, 'ItemWord': ItemWord, 'TotlKg': TotlKg, 'TotlPrice': TotlPrice}
    return context

def changeinput(user1, ProductNewId):
    Dollarchange = AddProduct.objects.filter(User_id = user1, ProductID = ProductNewId)
    AddProductsDictLst = AddProduct.objects.filter(User_id=user1)
    DollarchangeLST = []; TotlKgLst = []; TotlPriceLst = []
    for el in Dollarchange:
        DollarchangeLST.append(int(el.ProductCount)*int(el.ProductPrice))
    for el in AddProductsDictLst: 
        TotlKgLst.append(int(el.ProductCount))
        TotlPriceLst.append(int(el.ProductPrice) * int(el.ProductCount))
    TotlKg = sum(TotlKgLst)
    TotlPrice = sum(TotlPriceLst)
    DollarchangeLST = DollarchangeLST[0]
    context  = {'productidC': ProductNewId, 'Dollarchange': DollarchangeLST, 'TotlKg': TotlKg, 'TotlPrice': TotlPrice}
    return context

def cokkiereload(x):
    LST = []; TotlKgLst = []; TotlPriceLst = []
    if x != None:
        for el in x:
            relProducts = FishProduct.objects.get(ProductID=el)
            item = {
                'PictureURL': relProducts.Picture.url,
                'ProductName': relProducts.ProductName,
                'ProductID': relProducts.ProductID,
                'ProductCount': int(x[el]['productcount']),
                'ProductPrice': relProducts.ProductPrice,}
            LST.append(item)
            TotlKgLst.append(int(x[el]['productcount']))
            TotlPriceLst.append(int(relProducts.ProductPrice) * int(x[el]['productcount']))
        TotlKg = sum(TotlKgLst)
        TotlPrice = sum(TotlPriceLst)
        ItemCount = len(LST)
        if ItemCount == 1: ItemWord = ' товар'
        elif 1 < ItemCount <= 4: ItemWord = ' товара'
        else: ItemWord = ' товаров'
        context={'AddProductsDictLst': LST, 'TotlKg': TotlKg, 'TotlPrice': TotlPrice, 'ItemCount': ItemCount, 'ItemWord': ItemWord}
    else:
        context = {}
    return context

def cokkieChange(x, ProductId):
    TotlKgLst = []; TotlPriceLst = [];
    if x != None:
        RelfishChange = FishProduct.objects.get(ProductID=ProductId)
        Dollarchange = int(RelfishChange.ProductPrice)*int(x[ProductId]['productcount'])
        for el in x:
            Relfish = FishProduct.objects.get(ProductID=el)
            TotlKgLst.append(int(x[el]['productcount']))
            TotlPriceLst.append(int(Relfish.ProductPrice) * int(x[el]['productcount']))
        TotlKg = sum(TotlKgLst)
        TotlPrice = sum(TotlPriceLst)
        context = {'TotlKg': TotlKg, 'TotlPrice': TotlPrice, 'Dollarchange': Dollarchange, 'productidC': ProductId}
    else:
        context = {}
    return context

