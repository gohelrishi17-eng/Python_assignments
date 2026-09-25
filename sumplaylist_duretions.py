def sum_playlist_durations(durations):
    if len(durations) == 0:
        return 0

    return durations[0] + sum_playlist_durations(durations[1:])


durations = [321, 564, 987]

print(sum_playlist_durations(durations))