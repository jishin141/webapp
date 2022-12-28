from django.urls import path
from products import views
urlpatterns = [

    path('',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('checkout/',views.checkout),
    path('faqs/',views.faqs),
    path('help/',views.help),
    # path('payment/',views.payment),
    path('privacy',views.privacy),
    path('product/',views.product),
    path('product2/',views.product2),
    path('single/',views.single),
    path('single2/',views.single2),
    path('terms/',views.terms),
    path('register/',views.register),
    path('login/',views.login),
    path('logout/',views.logout),
    path('adminlogin/',views.adminlogin),
    path('adlogout/',views.adlogout),
    path('adminindex/',views.adminindex),
    path('blocks/',views.blocks),
    path('cards/',views.cards),
    path('carousels/',views.carousels),
    path('people/',views.people),
    path('forms/',views.forms),
    path('pricing/',views.pricing),
    path('viewdata/',views.viewdata),
    path('addproduct/',views.addproduct),
    path('productupdate/',views.productupdate),
    path('addcart/',views.addcart),
    path('cart/',views.cart),
    path('deleteitem/',views.deleteitem),
    path('cartupdate/',views.cartupdate),
    path('payindex/',views.payindex),
    # path('details/',views.details),
    # path('view/',views.view),
    # path('sample/',views.sample),
    
    
    







]    