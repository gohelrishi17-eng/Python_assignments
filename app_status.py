app_status = "Offline"


def check_status():
    user_status = "Online"

    print("Inside function - User:", user_status)
    print("Inside function - App:", app_status)


print("Before function:", app_status)

check_status()
print("After function:", app_status)