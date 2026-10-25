from django.contrib.auth.models import User
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
     password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
     class Meta:
          model = User
          fields = ['username', 'email', 'password', 'password2']
          extra_kwargs = {
               'password' : {'write_only': True}
          }
          
     def save(self):
          pass1 = self.validated_data['password']
          pass2 = self.validated_data['password2']
          
          if pass1 != pass2:
               raise serializers.ValidationError({'Error':'Password not matching!'})
          
          user_email = self.validated_data['email']
          if User.objects.filter(email = user_email).exists():
               raise serializers.ValidationError({'Error': 'Email already Exists, Try Log in'})
          
          
          account = User(email = user_email,username=self.validated_data['username'])
          account.set_password(pass1)
          account.save()
          
          return account