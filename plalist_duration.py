class InvalidDurationError(Exception):
    pass


def get_playlist_duration(songs):
    for duration in songs:
        if duration < 0:
            raise InvalidDurationError("Duration cannot be negative")

    total_seconds = sum(songs)
    total_minutes = total_seconds / 60

    return total_minutes


print(get_playlist_duration([395, 523, 677]))
