# Wi-Fi Password Crack Attempt Detection

MAX_ATTEMPTS = 3
failed = {}

while True:
    ip = input("Enter Device IP: ")
    password = input("Enter Wi-Fi Password: ")

    correct_password = "wifi123"

    if ip in failed and failed[ip] >= MAX_ATTEMPTS:
        print("ACCESS BLOCKED! Suspicious device detected.")
        continue

    if password == correct_password:
        print("Access Granted")
        failed[ip] = 0
    else:
        failed[ip] = failed.get(ip, 0) + 1
        print("Wrong Password!")

        if failed[ip] >= MAX_ATTEMPTS:
            print("ALERT: Password cracking attempt detected!")
            print("Device", ip, "has been BLOCKED.")