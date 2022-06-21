from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Post


class Postforms(forms):

    class meta:
        model = Post
        fields = "__all__"


