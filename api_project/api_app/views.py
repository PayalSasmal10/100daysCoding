from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test Api view"""

    def get(self, request, format=None):
        """Return a list of ApiView features"""
        an_apiview = [
            'Uses HTTP methods as function(get, post, patch, put, delete)'
            'Is similar to traditional Django view',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello Payal', 'an_apiview':an_apiview})