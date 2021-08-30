from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('', AjaxHomePage.as_view(), name='homePage'),
    path('fish/', AjaxFish.as_view(), name='fish'),
    path('shrimp/', AjaxShrimp.as_view(), name='shrimp'),
    path('seafood/', AjaxSeafood.as_view(), name='seafood'),
    path('crab/', AjaxCrab.as_view(), name='crab'),
    path('caviar/', AjaxCaviar.as_view(), name='caviar'),
    path('about/', AjaxAbout.as_view(), name='about'),
    path('basket/', AjaxBasket.as_view(), name='basket'),
    path('makingorder/', AjaxMakingorder.as_view(), name='makingorder'),
    path('clientprofile/', AjaxClientProfile.as_view(), name='clientprofile'),
    path('profileadmin/', AjaxProfileAdmin.as_view(), name='profileadmin'),
    path('pageone/', AjaxPageOne.as_view(), name='pageone'),
    path('pagetwo/', AjaxPageTwo.as_view(), name='pagetwo'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)