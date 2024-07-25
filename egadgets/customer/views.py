from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,DetailView
from django.views import View
from account.models import products,Cart,Orders
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.


class HomeView(TemplateView):
    template_name="home.html"


# class ProductView(TemplateView):
#     template_name="products.html"

# class ProductView(View):
#     def get(self,request,**kwargs):
#         cat=kwargs.get("cat")
#         print(cat)
#         data=products.objects.filter(category=cat)
#         print(data)
#         return render(request,"procts.html")

class ProductView(ListView):
    template_name="products.html"
    queryset=products.objects.all()
    context_object_name="data"

    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    #     context=super().get_context_data(**kwargs)
    #     print(context)
    #     return context

    def get_queryset(self) -> QuerySet[Any]:
        qs=super().get_queryset()
        qs=qs.filter(category=self.kwargs.get('cat'))
        return qs
    
class ProductDetailView(DetailView):
    template_name="details.html"
    queryset=products.objects.all()
    pk_url_kwarg="pid"
    context_object_name="products"

# def addtoCart(request,*args,**kwargs):
#     try:
#         user=request.user
#         pid=kwargs.get("pid")
#         product=products.objects.get(id=pid)
#         try:
#             cart=Cart.objects.get(user=user,products=product)
#             cart.quantity+=1
#             cart.save()
#             messages.success(request,"Product quantity updated")
#             return redirect ("clist")
#         except:
#             Cart.objects.create(user=user,products=product)
#             messages.success(request,"products added to cart")
#             return redirect ("clist")
#     except:
#         messages.error(request,"Cart entry failed")
#         return redirect("chome")


def addtoCart(request, *args, **kwargs):
    try:
        user = request.user
        pid = kwargs.get("pid")
        product = products.objects.get(id=pid)

        # Get or create cart item
        try:
            cart = Cart.objects.get(user=user, products=product)
            cart.quantity += 1
            cart.save()
            messages.success(request, "Product quantity updated")
        except Cart.DoesNotExist:
            Cart.objects.create(user=user, products=product, quantity=1)
            messages.success(request, "Product added to cart")
        return redirect("clist")
    except products.DoesNotExist:
        messages.error(request, "Product does not exist")
        return redirect("chome")
    except Exception as e:
        messages.error(request, f"Cart entry failed: {str(e)}")
        return redirect("chome")
    
class CartListView(ListView):
    template_name="cartlist.html"
    queryset=Cart.objects.all()
    context_object_name="Cart"

    def get_queryset(self):
        qs=super().get_queryset()
        qs=qs.filter(user=self.request.user)
        return qs
    

    
def CartRemoveView(request,*args,**kwargs):
    try:
        cid=kwargs.get("did") 
        cat=products.objects.get(id=cid)
        cat.delete()
        messages.success(request,"Cart item removed")
        return redirect ('clist') 
    except:
        messages.error(request,"something went wrong")                       
        return redirect ('clist') 
    
class CheckoutView(TemplateView):
    template_name="checkout.html"


    def post(self,request,*args,**kwargs):
        try:
            cid=kwargs.get("cid")
            cart=Cart.objects.get(id=cid)
            products=cart.products
            user=cart.user
            ph=request.POST.get('phone')
            addr=request.POST.get('address')
            Orders.objects.create(products=products,user=user,phone=ph,address=addr)
            cart.delete()
            messages.success(request,"order placed successfully")
            return redirect ('clist')
        except Exception as e:
            print(e)
            messages.error(request,"something went wrong, order placing cancelled")
            return redirect('clist')
        

class OrderListView(ListView):
    template_name="orderlist.html"
    queryset=Orders.objects.all()
    context_object_name="orders"

    def get_queryset(self):
        qs=super().get_queryset()
        qs=qs.filter(user=self.request.user)
        return qs
    
def cancelOrder(request,*args,**kwargs):
    try:
        cid=kwargs.get('oid')
        order=Orders.objects.get(id=cid)
        subject="Order cancelling acknowledgement"
        msg=f"your order for {order.products.title} is successfully cancelled"
        fr_om="neethukgeetha@gmail.com"
        to_ad=[request.user.email]
        send_mail(subject,msg,fr_om,to_ad)
        order.delete()
        messages.success(request,"order cancelled!!")
        return redirect ('olist')
    except Exception as e:
        messages.error(request,e)
        return redirect ('olist')


       

    
    

