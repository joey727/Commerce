from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createlisting", views.createlisting, name="createlisting"),
    path("activelisting", views.activelisting, name="activelisting"),
    path("categories", views.categories, name="categories"),
    path("viewlisting/<int:product_id>", views.viewlisting, name="viewlisting"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("addtowatchlist/<int:product_id>", views.addtowatchlist, name="addtowatchlist"),
    path("category/<str:categ>", views.category, name="category"),
    path("addcomment/<int:product_id>", views.addcomment, name="addcomment"),
    path("closebid/<int:product_id>", views.closebid, name="closebid"),
    path("closedlisting", views.closedlisting, name="closedlisting")
]
