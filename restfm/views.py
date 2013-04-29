# Create your views here.
from restfm.models import *
from restfm.serializers import *
from rest_framework import generics 
from rest_framework.response import Response
import os

import time

import subprocess

from mocker import Mocker

mocker = Mocker()

from mailmanclient import Client


client = Client('http://localhost:8001/3.0', 'restadmin', 'restpass')

class ApiView(generics.ListCreateAPIView):

    serializer_class = MailmanSerializer

    def list(self, request, *args, **kwargs):
        listObj = MailmanObject(field=client.system)
        serializer = self.serializer_class(listObj)
        return Response(serializer.data)
