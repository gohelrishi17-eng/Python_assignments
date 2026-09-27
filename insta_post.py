def insta_posts_generator(posts):
    for post in posts:
        yield post


posts = ["Good vibes only!", "New day, new goals!", "Weekend memories!", "Keep smiling!"] 


post_generator = insta_posts_generator(posts)

try:
    while True:
        print(next(post_generator))
except StopIteration:
    print("All posts printed")
