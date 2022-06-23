from django.shortcuts import render
from rest_framework.views import APIView
from api.models import Todos
from rest_framework.response import Response
from api.serializers import  TodoSerializer

# Create your views here

#url-api/v1/todos
#method:GET-date
#return all todos

#url-api/v1/todos
#post
#data:{"taskname:"tname,"user":"akhil"}

class TodosView(APIView):
    def get(self,*args,**kwargs):
        qs=Todos.objects.all()
        serializer=TodoSerializer(qs,many=True)#for deserializing
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer=TodoSerializer(data=request.data)#deserializer
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


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










#Todo create
#Todo detail
#Todo list
#Todo update
#Todo delete
