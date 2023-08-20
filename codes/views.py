from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Code
from .serializers import CodeSerializer
from .custom_responses import create_zip_code_not_found_response, create_zip_code_response


class CodesView(APIView):
    def get(self, request, zip_code):
        response, success = self.create_first_part_of_response(zip_code)
        if success:
            self.append_settlements_to_response(zip_code, response)
            return Response(response, status=status.HTTP_200_OK)
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def append_settlements_to_response(self, zip_code, resp):
        settlements_lookup = Code.objects.filter(d_codigo=zip_code)
        serializer = CodeSerializer(settlements_lookup, many=True)
        
        settl_data = serializer.data
        
        for settlement in settl_data:
            settlement = self.create_settlement_obj(settlement)
            resp["settlements"].append(settlement)

    def create_first_part_of_response(self, zip_code):
        """
        It creates the first part of the response if the zip_code
        exists in the database and returns it along with True.
        
        It does not include the settlements yet.

        If the zip_code was not found return a custom message and False.
        
        """
        try:
            first = Code.objects.filter(d_codigo=zip_code).first()
        except Exception as e:
            print(e)
        
        # It means the code does not exists in the database
        if not first:
            response = create_zip_code_not_found_response(zip_code)
            return response, False
        
        serializer = CodeSerializer(first)
        data = serializer.data

        response_success = create_zip_code_response(results=data)
        
        return response_success, True

    def create_settlement_obj(self, settlement):
        """
        Creates each settlement object that will be appended to the response[settlements]
        """
        settlement = {
                "key":settlement["id_asenta_cpcons"],
                "name":settlement["d_asenta"],
                "zone_type":settlement["d_zona"],
                "settlement_type":{
                    "name": settlement["d_tipo_asenta"].upper()
                }
            }
        return settlement

    