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

class FooView(generics.ListCreateAPIView):

    serializer_class = FooSerializer

    def list(self, request, *args, **kwargs):
        fooObj = FooObject(field=client.domains)
        serializer = self.serializer_class(fooObj)
        return Response(serializer.data)
