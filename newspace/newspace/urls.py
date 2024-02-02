from django.contrib import admin
from django.urls import path
from end_user.views import customer_index
from content.views import serve_content, index, about
from django.contrib.auth import views as auth_views
 



urlpatterns = [
    
    path('admin/', admin.site.urls), 
    path("", index, name="index"), # literally just render the html
    path("about/", about, name="about"), # literally just render the html
    path("customer/", customer_index, name="customer_index"), # validate
    path("content/<int:id>", serve_content, name="contents"), # validate
    path(
            "login/",
            auth_views.LoginView.as_view(
                template_name = "login.html",
            ),
            name="login"
    ), 
    path(
            "logout/",
            auth_views.LogoutView.as_view(
                template_name = "logout.html",
            ),
            name="logout"), # logout 

]
