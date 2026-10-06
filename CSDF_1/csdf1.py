import re

path = r"C:\Users\sidra\Desktop\BE\LP4\CSDF_1\New assignment_ _Assignment no 04_.eml"

with open(path, "r") as file:
    data = file.read()

fields = ["From", "To", "Subject", "Date", "Message-ID", "Received"]

for field in fields:
    result = re.search(rf"^{field}:\s*(.*)", data, re.MULTILINE)

    if result:
        print(field, ":", result.group(1).strip())