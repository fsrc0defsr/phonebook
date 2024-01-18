from .models import PhoneNumber
from .serializers import PhoneNumberSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from xml.etree.ElementTree import Element, SubElement, tostring

class PhoneNumberList(APIView):
    def get(self, request, format=None):
        phone_numbers = PhoneNumber.objects.all()
        data = PhoneNumberSerializer(phone_numbers, many=True).data
        xml_data = generate_xml(data)
        return Response(xml_data, content_type='application/xml')

def generate_xml(data):
    root = Element('YealinkIPPhonebook')
    title = SubElement(root, 'Title')
    title.text = 'Yealink'

    menu = SubElement(root, 'Menu', Name='Справочник')

    for item in data:
        unit = SubElement(menu, 'Unit', Name=item['Name'], default_photo='Resource:', Phone3=str(item['Phone3']), Phone2=str(item['Phone2']), Phone1=str(item['Phone1']))

    xml_string = '<?xml version="1.0" encoding="UTF-8"?>\n' + tostring(root, encoding='utf-8').decode('utf-8').replace('><', '>\n\t<').replace('><', '><')

    return xml_string
