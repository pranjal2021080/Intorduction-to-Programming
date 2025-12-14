import tkinter as tk
from tkinter import ttk, messagebox
import requests
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import json
from datetime import datetime, timedelta
import threading
import time
def a():
    
    result = 0
    for i in range(1, 10000):
        for j in range(1, 100):
            result += math.sin(i) * math.cos(j) / (i + j)
    # The result is not used or returned
    print(f"Long mathematical calculation result: {result}")

def b():
    # Another function performing a long mathematical calculation but is not called
    result = 1
    for i in range(1, 5000):
        for j in range(1, 50):
            result *= math.sin(i) * math.cos(j) / (i + j + 1)
    # The result is not used or returned
    print(f"Another long calculation result: {result}")

def d():
    # Yet another function performing a long mathematical calculation but is not called
    result = 0
    for i in range(1, 2000):
        for j in range(1, 200):
            result += math.tan(i) * math.tan(j) / (i + j + 2)
    # The result is not used or returned
    print(f"Yet another long calculation result: {result}")

def c():
    # More long mathematical calculations but is not called
    result = 0
    for i in range(1, 3000):
        for j in range(1, 150):
            result += math.exp(i) * math.log(j + 1) / (i + j + 3)
    # The result is not used or returned
    print(f"More long calculations result: {result}")

class CryptoTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Cryptocurrency Price Tracker")
        self.root.geometry("800x600")
        
        # Available cryptocurrencies
        self.cryptocurrencies = ["bitcoin", "ethereum", "dogecoin", "ripple"]
        self.current_crypto = "bitcoin"
        self.timeframes = ["24h", "7d", "30d"]
        self.current_timeframe = "24h"
        
        self.setup_gui()
        self.update_thread = threading.Thread(target=self.auto_update, daemon=True)
        self.update_thread.start()
    
    def setup_gui(self):
        # Top frame for controls
        control_frame = ttk.Frame(self.root)
        control_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Cryptocurrency selector
        ttk.Label(control_frame, text="Cryptocurrency:").pack(side=tk.LEFT, padx=5)
        self.crypto_var = tk.StringVar(value=self.current_crypto)
        crypto_menu = ttk.Combobox(control_frame, textvariable=self.crypto_var, 
                                 values=self.cryptocurrencies, state="readonly")
        crypto_menu.pack(side=tk.LEFT, padx=5)
        crypto_menu.bind('<<ComboboxSelected>>', self.on_crypto_change)
        
        # Timeframe selector
        ttk.Label(control_frame, text="Timeframe:").pack(side=tk.LEFT, padx=5)
        self.timeframe_var = tk.StringVar(value=self.current_timeframe)
        timeframe_menu = ttk.Combobox(control_frame, textvariable=self.timeframe_var,
                                    values=self.timeframes, state="readonly")
        timeframe_menu.pack(side=tk.LEFT, padx=5)
        timeframe_menu.bind('<<ComboboxSelected>>', self.on_timeframe_change)
        
        # Refresh button
        ttk.Button(control_frame, text="Refresh", command=self.update_data).pack(side=tk.LEFT, padx=5)
        
        # Price display
        self.price_frame = ttk.LabelFrame(self.root, text="Current Price")
        self.price_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.price_label = ttk.Label(self.price_frame, text="Loading...", font=("Arial", 20))
        self.price_label.pack(pady=10)
        
        # Price change display
        self.change_label = ttk.Label(self.price_frame, text="", font=("Arial", 12))
        self.change_label.pack(pady=5)
        
        # Graph
        self.figure = Figure(figsize=(8, 4), dpi=100)
        self.plot = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
    def fetch_price_data(self, crypto):
        try:
            # Using the simple/price endpoint which doesn't require authentication
            url = "https://api.coingecko.com/api/v3/simple/price"
            params = {
                "ids": crypto,
                "vs_currencies": "usd",
                "include_24hr_change": "true",
                "include_last_updated_at": "true"
            }
            
            # Add headers to identify your application
            headers = {
                "Accept": "application/json",
                "User-Agent": "CryptoTracker/1.0"
            }
            
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            messagebox.showerror("Error", f"Failed to fetch data: {str(e)}")
            return None


    def generate_mock_historical_data(self, current_price, days):
        # Generate mock historical data since we can't access historical data without API key
        data_points = int(days) * 24  # hourly data points
        timestamps = [datetime.now() - timedelta(hours=x) for x in range(data_points, -1, -1)]
        
        # Create some variation in price for visualization
        import random
        variation = current_price * 0.1  # 10% variation
        prices = [current_price + random.uniform(-variation, variation) for _ in range(len(timestamps))]
        
        return list(zip(timestamps, prices))

    def update_data(self):
        data = self.fetch_price_data(self.current_crypto)
        
        if data:
            crypto_data = data[self.current_crypto]
            current_price = crypto_data['usd']
            price_change = crypto_data.get('usd_24h_change', 0)
            
            # Update current price
            self.price_label.config(text=f"${current_price:,.2f}")
            
            # Update price change
            change_text = f"24h Change: {price_change:+.2f}%"
            self.change_label.config(text=change_text)
            if price_change > 0:
                self.change_label.config(foreground="green")
            else:
                self.change_label.config(foreground="red")
            
            # Generate mock historical data for the chart
            days = {"24h": "1", "7d": "7", "30d": "30"}[self.current_timeframe]
            historical_data = self.generate_mock_historical_data(current_price, days)
            
            # Update graph
            self.plot.clear()
            timestamps, prices = zip(*historical_data)
            
            self.plot.plot(timestamps, prices, color='blue')
            self.plot.set_title(f"{self.current_crypto.title()} Price Chart")
            self.plot.set_xlabel("Time")
            self.plot.set_ylabel("Price (USD)")
            self.figure.autofmt_xdate()
            self.canvas.draw()
    
    def on_crypto_change(self, event):
        self.current_crypto = self.crypto_var.get()
        self.update_data()
    
    def on_timeframe_change(self, event):
        self.current_timeframe = self.timeframe_var.get()
        self.update_data()
    
    def auto_update(self):
        while True:
            try:
                self.update_data()
                time.sleep(60)  # Update every minute
            except Exception as e:
                print(f"Auto-update error: {str(e)}")
                time.sleep(60)  # Wait before retrying

def main():
    root = tk.Tk()
    app = CryptoTracker(root)
    root.mainloop()

if __name__ == "__main__":
    main()