from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

UserModel = get_user_model()

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # 'username' será o email enviado pelo formulário customizado
        email = username or kwargs.get('email')
        if not email:
            return None
            
        try:
            user = UserModel.objects.get(email__iexact=email)
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
            return None
        except UserModel.MultipleObjectsReturned:
            user = UserModel.objects.filter(email__iexact=email).order_by('id').first()
            
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
