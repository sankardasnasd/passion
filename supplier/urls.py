from . import views
from django.urls import path

app_name="supplier"
urlpatterns = [
    # path('supplier/',include('supplier.urls')),
    path('addproduct',views.supplierAddProduct,name="supplierAddproduct"),
    path('viewproduct',views.supplierViewProduct,name="supplier_view_product"),
    path('orders',views.supplierOrders,name="supplier_orders"),
    path('pass',views.supplierPass,name="supplier_pass"),
    path('profile',views.supplierProfile,name="supplier_profile"),
]