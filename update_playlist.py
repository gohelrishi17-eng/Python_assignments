playlist_prices = {
    "workout": 999,
    "chill": 499,
    "party": 1299,
    "focus": 799,
    "sleep": 599,
}
print(playlist_prices)    

def update_playlist_prices(playlist_name, new_price):
    playlist_prices[playlist_name] = new_price

update_playlist_prices("workout", 1099)
   

print(playlist_prices)