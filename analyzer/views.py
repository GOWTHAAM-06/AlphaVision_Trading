from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import OptionChainSnapshot
from .serializers import OptionChainSerializer
from django.http import JsonResponse

@api_view(['GET'])
def get_market_data(request):
    data = OptionChainSnapshot.objects.all().order_by('-timestamp')[:10]
    serializer = OptionChainSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_trade_signal(request):
    # Fetch the latest 5 snapshots to see the trend
    snapshots = OptionChainSnapshot.objects.all().order_by('-timestamp')[:5]
    
    if len(snapshots) < 2:
        return Response({"signal": "NEUTRAL", "reason": "Insufficient Data"})

    current_price = snapshots[0].last_price
    previous_price = snapshots[1].last_price
    
    # Simple Logic: Is the price moving up?
    if current_price > previous_price:
        signal = "BULLISH"
        color = "#00FF00" # Neon Green
        advice = "Market momentum is rising. Look for Call Option (CE) entries."
    else:
        signal = "BEARISH"
        color = "#FF0000" # Red
        advice = "Price is dipping. Watch for Put Option (PE) buildup."

    return Response({
        "symbol": "NIFTY",
        "current_price": current_price,
        "signal": signal,
        "ui_color": color,
        "advice": advice,
        "engine": "AlphaVision-v1"
    })

def api_home(request):
    return JsonResponse({
        "status": "AlphaVision Core Online",
        "version": "1.0.0",
        "endpoints": ["/api/market-data/", "/api/signal/"]
    })