from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()

class UserCreate(UserCreationForm):
   
   class Meta:
      model = User
      fields = ['primer_nombre', 'segundo_nombre','nombre_usuario', 'email', 'clave1', 'clave2',]
