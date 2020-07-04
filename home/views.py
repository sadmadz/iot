import binascii
import os

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from home.models import Home, Thing, Type
from home.serializers import HomeSerializer, ThingSerializer, ThingPostSerializer, TypeSerializer


def home(request):
    return render(request, 'home.html')


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_home(request, pk):
    try:
        home = Home.objects.get(pk=pk)
    except Home.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single home
    if request.method == 'GET':
        if home.token == request.META['HTTP_AUTHORIZATION']:
            serializer = HomeSerializer(home, context={'request': request})
            return Response(serializer.data,
                            content_type="application/json; charset=utf-8")
        else:
            return Response({'error': 'token expired'}, status=status.HTTP_401_UNAUTHORIZED)

    elif request.method == 'DELETE':
        home.delete()
        return Response(status=status.HTTP_200_OK)
    # update details of a single home
    elif request.method == 'PUT':
        serializer = HomeSerializer(home, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK,
                            content_type="application/json; charset=utf-8")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_home(request):
    if request.method == 'GET':
        homes = Home.objects.all()
        serializer = HomeSerializer(homes, many=True, context={'request': request})
        return Response(serializer.data,
                        content_type="application/json; charset=utf-8")
    # insert a new record for a home
    elif request.method == 'POST':
        # data = {
        #     'first_name': request.data.get('first_name'),
        #     'last_name': request.data.get('last_name'),
        #     'username': request.data.get('username'),
        #     'password': request.data.get('password'),
        #     'phone_number': request.data.get('phone_number')
        # }
        serializer = HomeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED,
                            content_type="application/json; charset=utf-8")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_things(request, pk):
    try:
        home = Home.objects.get(pk=pk)
    except Home.DoesNotExist:
        return Response({'error': 'Home not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        things = Thing.objects.filter(home=home)
        serializer = ThingSerializer(things, many=True, context={'request': request})
        return Response(serializer.data,
                        content_type="application/json; charset=utf-8")
    # insert a new record for a Thing
    elif request.method == 'POST':
        print(request.data)
        data = {
            'name': request.data.get('name'),
            'status': request.data.get('status'),
            'thing_row': request.data.get('thing_row'),
            'thing_column': request.data.get('thing_column'),
            'home': pk,
            'type': request.data.get('type')
        }
        serializer = ThingPostSerializer(data=data, )
        if serializer.is_valid():
            print("sere ser")
            print(serializer.validated_data)
            serializer.save()
            print(serializer.save())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_thing(request, pk):
    try:
        try:
            thing = Thing.objects.get(pk=pk)
        except Thing.DoesNotExist:
            return Response({'error': 'Thing not found'}, status.HTTP_404_NOT_FOUND)

        # get details of a single thing
        if request.method == 'GET':
            serializer = ThingSerializer(thing, context={'request': request})
            return Response(serializer.data,
                            content_type="application/json; charset=utf-8")

        # delete a single thing
        elif request.method == 'DELETE':
            thing.delete()
            return Response(status=status.HTTP_200_OK)
        # update details of a single thing
        elif request.method == 'PUT':
            serializer = ThingSerializer(thing, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except KeyError as e:
        print(e)
        return Response({'error': 'bad request'}, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_type(request):
    if request.method == 'GET':
        types = Type.objects.all()
        serializer = TypeSerializer(types, many=True, context={'request': request})
        return Response(serializer.data,
                        content_type="application/json; charset=utf-8")
    # insert a new record for a type
    elif request.method == 'POST':
        # data = {
        #     'first_name': request.data.get('first_name'),
        #     'last_name': request.data.get('last_name'),
        #     'username': request.data.get('username'),
        #     'password': request.data.get('password'),
        #     'phone_number': request.data.get('phone_number')
        # }
        serializer = TypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED,
                            content_type="application/json; charset=utf-8")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
