from django.core.management.base import BaseCommand
from analyzer.models import OptionChainSnapshot
import yfinance as yf
from datetime import datetime

class Command(BaseCommand):
    help = 'Fetches stable market data using yfinance'

    def handle(self, *args, **kwargs):
        self.stdout.write("Switching to the stable yfinance delivery...")
        
        try:
            # Fetching NIFTY 50 Index data (^NSEI is the symbol)
            nifty = yf.Ticker("^NSEI")
            data = nifty.history(period="1d")
            
            if not data.empty:
                last_price = data['Close'].iloc[-1]
                self.stdout.write(f"NIFTY 50 Last Close: {last_price}")
                
                # Saving to our OptionChainSnapshot table
                # We'll treat this as a 'Spot Price' snapshot
                OptionChainSnapshot.objects.create(
                    symbol="NIFTY",
                    expiry_date=datetime.now().date(),
                    strike_price=0.0, # Spot doesn't have a strike, we use 0
                    option_type="SPOT",
                    last_price=last_price,
                    open_interest=0
                )
                
                self.stdout.write(self.style.SUCCESS("Successfully plucked data and saved to DB!"))
            else:
                self.stdout.write(self.style.WARNING("No data found. Market might be closed."))
                
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Delivery failed: {e}"))