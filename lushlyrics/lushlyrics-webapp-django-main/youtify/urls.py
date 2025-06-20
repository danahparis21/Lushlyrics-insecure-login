from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from main import views as main_views  # make sure this import is here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # remove `next_page` for now
    path('signup/', main_views.signup_view, name='signup'),  # ✅ use your custom view here
    path('accounts/', include('allauth.urls')),
]
