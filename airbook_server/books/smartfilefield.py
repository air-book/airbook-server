"""
#TODO: thi has been copied from webops
MOVE TO ANOTHER REUSABLE DJANGO APP
"""

import base64
import uuid
import sys
from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from django.utils.translation import ugettext_lazy as _
import json
from rest_framework import serializers
import requests

EMPTY_VALUES = (None, '', [], (), {})
 
class SmartFileField(serializers.FileField):
    """
    
    """

    def get_file_data_from_base64(self, data):
        if data['uri'].startswith("data"):
            content = data['uri'].split(",")[1]
        else:
            content = data['uri']

        # Try to decode the file. Return validation error if it fails.
        try:
            decoded_file = base64.b64decode(content)

        except TypeError:
            raise ValidationError(_("Please upload a valid file."))
        except:
            raise

        # Generate file name:
        file_name = data['filename']

        file_data = ContentFile(decoded_file, name=file_name)
        return file_data


    def get_file_data_from_url(self, data):
        url = data['uri']
        r = requests.get(url)
        file_name = url.split("/")[-1]
        file_data = ContentFile(r.content, name=file_name)
        return file_data



    def to_internal_value(self, data):
        
        if data in EMPTY_VALUES:
            return None

        # Check if this is a base64 string
        if isinstance(data, dict):
            if 'uri' not in data:
                raise ValidationError(_("we need the uri key!"))

            if data['uri'].startswith('data:'):
                file_data = self.get_file_data_from_base64(data)

            elif data['uri'].startswith('http'):
                file_data = self.get_file_data_from_url(data)

            else:
                file_data = self.get_file_data_from_base64(data)

            
            return super(SmartFileField,self).to_internal_value(file_data)
        
        else:
            return super(SmartFileField,self).to_internal_value(data)

    
