import requests
from django.shortcuts import render

# Create your views here.
from rest_framework import serializers
from rest_framework.generics import ListCreateAPIView


def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()


foodboxes = get_data('https://stepik.org/media/attachments/course/73594/foodboxes.json')
recipients = get_data('https://stepik.org/media/attachments/course/73594/recipients.json')


class ApiFoodList(ListCreateAPIView):
    queryset = foodboxes
    serializer_class = serializers.Serializer

