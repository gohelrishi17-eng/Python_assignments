class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.play_count = 0

    def play_preview(self):
        print(f"Playing 30-second preview of {self.title} by {self.artist}")

    def increment_play_count(self):
        self.play_count += 1


song1 = Song("Blinding Lights", "The Weeknd", 200)

print("Title:", song1.title)
print("Artist:", song1.artist)

song1.play_preview()

song1.increment_play_count()
song1.increment_play_count()
song1.increment_play_count()

print("Play Count:", song1.play_count)


class FoodOrder:
    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name
        self.items = []
        self.total_price = 0

    def add_item(self, item, price):
        self.items.append(item)
        self.total_price += price


order1 = FoodOrder("Zomato Restaurant")

order1.add_item("Pizza", 250)
order1.add_item("Burger", 150)

print("Restaurant:", order1.restaurant_name)
print("Items:", order1.items)
print("Total Price:", order1.total_price)
