from django.db import models
from django.contrib.auth.models import User

class FishProduct(models.Model):
    Picture = models.ImageField(null=True, blank=True)
    ProductStatus = models.CharField('Статус', null=True, max_length=25)
    ProductType = models.CharField('Тип продукта', null=True, max_length=25)
    ProductName = models.CharField('Название продукта', null=True, max_length=25)
    ProductDescription = models.CharField('Описание товара', null=True, max_length=35)
    ProductDescription2 = models.CharField('Описание товара', null=True, max_length=35)
    ProductRating = models.CharField('Рейтинг', null=True, max_length=50)
    ProductSize1 = models.CharField('Размер 1', null=False, default="", blank=True, max_length=25)
    ProductSize2 = models.CharField('Размер 2', null=False, default="", blank=True, max_length=25)
    ProductSize3 = models.CharField('Размер 3', null=False, default="", blank=True, max_length=25)
    ProductSize4 = models.CharField('Размер 4', null=False, default="", blank=True, max_length=25)
    ProductPrice = models.CharField('Цена', null=True, max_length=50)
    ProductID = models.CharField('ProductID', null=True, max_length=50)

    def __str__(self):
        return self.ProductName
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class AddProduct(models.Model):
    User = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    PictureURL = models.CharField("URL картинки", null=True, max_length=25)
    ProductCount = models.CharField("Колличество", null=True, max_length=25)
    ProductName = models.CharField("Название товара", null=True, max_length=25)
    ProductPrice = models.CharField("Цена за кг", null=True, max_length=25)
    ProductID = models.CharField('ProductID', null=True, max_length=50)

    def __str__(self):
        return self.ProductName
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары в корзине'

class ClientInfo(models.Model):
    User = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    orderId = models.CharField('Номер заказа', null=True, max_length=100)
    NameClient = models.CharField("Имя клиента", null=True, max_length=25)
    SurnameClient = models.CharField("Фамилия клиента", null=True, max_length=25)
    ClientPhone = models.CharField("Телефон", null=True, max_length=25)
    ClientEmail = models.CharField("Е-майл", null=True, max_length=50)
    DeliveryMethod = models.CharField("Способ доставки", null=True, max_length=25)
    ClientAddress = models.CharField("Адресс", null=True, max_length=100)
    prname = models.CharField("Название продукта", null=True, max_length=100)
    prcount = models.CharField("Вес заказа", null=True, max_length=100)
    prprice = models.CharField("Цена заказа", null=True, max_length=100)
    dateOrder = models.CharField("Дата поступления", null=True, max_length=25)
    dateDone = models.CharField('Дата выполнения', null=True, max_length=25)
    statusOrder = models.CharField('Статус заказа', default="На рассмотрении", max_length=25)
    statusColor = models.CharField('Цвет статуса заказа', default="colorfirst", max_length=25)
    def __str__(self):
        return self.NameClient
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Поступление заказов'
        

class Test(models.Model):
    Input1 = models.CharField("Сообщение 1", null=True, max_length=25)
    
    def __str__(self):
        return self.Input1