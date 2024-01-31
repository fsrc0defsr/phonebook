from .models import PhoneNumber
from .serializers import PhoneNumberSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.decorators import permission_classes
import xml.etree.ElementTree as ET
import xml.dom.minidom
from django.http import HttpResponse

#@permission_classes([IsAuthenticated])
class PhoneNumberList(APIView):
    authentication_classes = [BasicAuthentication]

    def get(self, request, format=None):
        phone_numbers = PhoneNumber.objects.all()
        data = PhoneNumberSerializer(phone_numbers, many=True).data
        xml_data = generate_xml(data)
        response = HttpResponse(xml_data, content_type='application/xml', charset='utf-8')
        response['Content-Disposition'] = 'attachment; filename=phonebook.xml'
        return response

def generate_xml(data):
    root = ET.Element('YealinkIPPhoneBook')
    title = ET.SubElement(root, 'Title')
    title.text = 'Yealink'

    menu = ET.SubElement(root, 'Menu', Name='Справочник')

    for item in data:
        unit = ET.SubElement(
            menu,
            'Unit',
            Name=str(item['Name']),
            default_photo='Resource:',
            Phone3=str(item['Phone3']),
            Phone2=str(item['Phone2']),
            Phone1=str(item['Phone1'])
        )
    
    xml_string = ET.tostring(root, encoding='utf-8')
    xml_data = xml.dom.minidom.parseString(xml_string).toprettyxml(indent="    ", encoding='utf-8')
    return xml_data
