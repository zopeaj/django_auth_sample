from django.urls import path
from account.views import RegistrationApiView, LoginApiView

urlpatterns = [
    path('registration/', RegistrationApiView.as_view(), name='registration'),
    path('login/', LoginApiView.as_view(), name='login')

]

# http://127.0.0.1:5050/auth/api/registration/
# http://127.0.0.1:5050/auth/api/login/

