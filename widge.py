import tkinter as tk
import requests

def get_crypto_prices():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,solana,ethereum,dogecoin",
        "vs_currencies": "usd"
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()

        price_text = ""
        for coin, info in data.items():
            name = coin.capitalize().ljust(10)
            price = f"${info['usd']:,}"
            price_text += f"{name}: {price}\n"

        label.config(text=price_text)
    except:
        label.config(text="⚠️ Error fetching prices")

    window.after(15000, get_crypto_prices)  # Refresh every 15 sec

# 🪟 Window setup
window = tk.Tk()
window.overrideredirect(True)  # No title bar
window.attributes("-topmost", True)  # Always on top
window.geometry("260x150+100+100")
window.configure(bg="#121212")

# 🖱️ Make window draggable
def drag(event):
    x = event.x_root
    y = event.y_root
    window.geometry(f"+{x}+{y}")

# 🧾 Stylish Label
label = tk.Label(
    window,
    font=("Consolas", 12, "bold"),
    fg="#00FF9F",
    bg="#121212",
    justify="left",
    anchor="nw"
)
label.pack(padx=15, pady=10, fill="both", expand=True)
label.bind("<B1-Motion>", drag)

get_crypto_prices()
window.mainloop()