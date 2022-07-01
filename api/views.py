from django.shortcuts import render
from rest_framework.views import APIView
from api.models import Todos
from rest_framework.response import Response
from api.serializers import  TodoSerializer,UserSerializer,LoginSerializer
from rest_framework import status
from rest_framework import authentication,permissions
from django.contrib.auth import authenticate,login

# Create your views here
#authenticate-request and credentials are correct return user.


#url-api/v1/todos
#method:GET-date
#return all todos

#url-api/v1/todos
#post
#data:{"taskname:"tname,"user":"akhil"}

class TodosView(APIView):
    authentication_classes = [authentication.BasicAuthentication,authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request,*args,**kwargs):
        qs=Todos.objects.filter(user=request.user)
        serializer=TodoSerializer(qs,many=True)#for deserializing
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer = TodoSerializer(data=request.data,context={'user':request.user})#serializing
        print(request.user)
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


#details of specific todo with given id
class TodoDetails(APIView):
    def get(self,request,*args,**kwargs):
           id=kwargs.get("todo_id")
           todo=Todos.objects.get(id=id)
           serializer=TodoSerializer(todo)
           return Response(serializer.data)
    def put(self,request,*args,**kwargs):
         id =kwargs.get("todo_id")
         todo=Todos.objects.get(id=id)
         serializer=TodoSerializer(instance=todo,data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("todo_id")
        todo=Todos.objects.get(id=id)
        todo.delete()
        return Response({"msg":"deleted"})

# user created from UserSerializer and fields

class UserCreationView(APIView):#(signup view)
    def post(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class SignInView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            uname=serializer.validated_data.get("username")
            password=serializer.validated_data.get("password")
            user=authenticate(request,username=uname,password=password)
            if user:
                login(request,user)#to stop the function of reauthenticate every request, we are calling login then user session store there.
                return Response({"msg":"success"})
            else:
                return Response({"msg":"invalid credentials"})










#Todo create
#Todo detail
#Todo list
#Todo update
#Todo delete
