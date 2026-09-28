def format_follower_count(n):
    if n >= 1000000:
        value = n / 1000000
        return f"{value:.1f}M"

    if n >= 1000:
        value = n / 1000
        return f"{value:.1f}K"

    else:
        return str(n)

print(format_follower_count(1500))
