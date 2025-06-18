import tkinter as tk
import requests

def get_crypto_prices():
    try:
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            "vs_currency": "usd",
            "ids": "bitcoin,solana,ethereum,dogecoin",
            "price_change_percentage": "24h"
        }
        response = requests.get(url, params=params)
        data = response.json()

        # Clear previous widgets
        for widget in frame.winfo_children():
            widget.destroy()

        for coin in data:
            name = coin["name"].ljust(10)
            price = f"${coin['current_price']:,}".rjust(12)
            change = coin["price_change_percentage_24h"]

            if change is not None:
                change_str = f"{change:+.2f}%"
                color = "#00FF00" if change >= 0 else "#FF4C4C"
                arrow = "↑" if change >= 0 else "↓"
                change_display = f"{arrow} {change_str}".rjust(8)
            else:
                change_display = "N/A"
                color = "#FFFFFF"

            full_text = f"{name:<10} {price}  {change_display}"

            label = tk.Label(
                frame,
                text=full_text,
                font=("Consolas", 11, "bold"),
                fg=color,
                bg="#1e1e1e",
                anchor="w",
                justify="left"
            )
            label.pack(anchor="w", padx=5, pady=2)

    except Exception as e:
        error_label = tk.Label(
            frame,
            text=f"⚠️ Error: {e}",
            font=("Consolas", 11),
            fg="white",
            bg="#1e1e1e"
        )
        error_label.pack()

    window.after(15000, get_crypto_prices)

# 🖥️ GUI Setup
window = tk.Tk()
window.overrideredirect(True)
window.attributes("-topmost", True)
window.geometry("360x180+100+100")
window.configure(bg="#1e1e1e")

# 🖱️ Drag Support
def drag(event):
    x, y = event.x_root, event.y_root
    window.geometry(f"+{x}+{y}")

# 📦 Frame to hold content
frame = tk.Frame(window, bg="#1e1e1e")
frame.pack(fill="both", expand=True, padx=10, pady=10)
frame.bind("<B1-Motion>", drag)
window.bind("<B1-Motion>", drag)

get_crypto_prices()
window.mainloop()