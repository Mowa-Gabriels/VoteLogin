from django.urls import path
from .views import SignUpView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
      path('', views.home, name='home'),
      path('signup/', SignUpView.as_view(), name='signup'),
       path('login/', auth_views.LoginView.as_view(template_name= 'login.html'), name='login'),
       path('logout/', auth_views.LogoutView.as_view(next_page= 'login'), name='logout'),


         path('accred/', auth_views.PasswordResetView.as_view(
           template_name= 'passwordreset/password_reset.html',
           subject_template_name ='passwordreset/password_reset_subject.txt',
           email_template_name = 'passwordreset/password_reset_email.html',
           #success_url = '/login/'
           ),
           name='password_reset'),
         path('accred/done/',auth_views.PasswordResetDoneView.as_view(
           template_name= 'passwordreset/password_reset_done.html'),
           name='password_reset_done'),
         path('accred_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
           template_name= 'passwordreset/password_reset_confirm.html'),
           name='password_reset_confirm'),
         path('accred//complete/',auth_views.PasswordResetCompleteView.as_view(
           template_name= 'passwordreset/password_reset_complete.html'),
           name='password_reset_complete'),
]
