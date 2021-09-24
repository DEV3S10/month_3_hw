from rest_framework import serializers
from django import forms

from .models import Blog


class BlogForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField()
    hashtags = forms.CharField()


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = [
            'id',
            'image',
            'title',
            'description',
            'hashtags'
        ]