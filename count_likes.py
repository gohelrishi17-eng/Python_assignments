def count_likes(post):
    total = post["likes"]

    if "replies" in post:
        for reply in post["replies"].values():
            total += count_likes(reply)

    return total


posts = {
    "post1": {
        "likes": 500,
        "replies": {
            "reply1": {
                "likes": 50
            },
            "reply2": {
                "likes": 30
            }
        }
    }
}

for post in posts.values():
    print(count_likes(post))