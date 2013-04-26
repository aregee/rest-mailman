from django.forms import widgets
from rest_framework import serializers

# Serializer

class FooSerializer(serializers.Serializer):
    foo_field = serializers.CharField(max_length=200)


# Your "model"
class FooObject(object):
    def __init__(self, field):
        self.foo_field = field