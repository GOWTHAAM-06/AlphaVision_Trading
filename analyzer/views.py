from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import OptionChainSnapshot
from .serializers import OptionChainSerializer

@api_view(['GET'])
def get_market_data(request):
    data = OptionChainSnapshot.objects.all().order_by('-timestamp')[:10] # Get last 10 entries
    serializer = OptionChainSerializer(data, many=True)
    return Response(serializer.data)