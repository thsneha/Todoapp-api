from rest_framework.serializers import ModelSerializer
from api.models import Todos
from rest_framework import serializers
from django.contrib.auth.models import User

class TodoSerializer(ModelSerializer):
    id=serializers.CharField(read_only=True)#
    user=serializers.CharField(read_only=True)
    class Meta:
        model=Todos
        fields=["id","taskname","user","status"]
    def create(self, validated_data):#overriding the create
        user=self.context.get("user")#for getting the user from context dictionary.
        return Todos.objects.create(**validated_data,user=user)
class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password"]#these fields defined in usermodel
    def create(self,validated_data):#when an object is saving the create method is working.customize the user
        return User.objects.create_user(**validated_data)#for hashing the password overriding the create_user.**validated_data contains  dictionary values.


class LoginSerializer(serializers.Serializer):#inheriting normal serializer no data is saved in database.only checking
        username=serializers.CharField()#clientside application is passing username and password.
        password=serializers.CharField()