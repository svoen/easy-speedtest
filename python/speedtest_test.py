from speedtester import speedtester


response = speedtester()

download = round(float(response["download"]) / 1048576,2)
upload = round(float(response["upload"]) / 1048576,2)
ping = round(response["ping"])
location = {"lat": float(response["server"]["lat"]), "lon": float(response["server"]["lon"])}
name = response["server"]["name"]
country = response["server"]["country"]
sponsor = response["server"]["sponsor"]
timestamp = response["timestamp"]
up = round(float(response["bytes_sent"]) / 131072,2)
down = round(float(response["bytes_received"]) / 131072,2)

result = {"download": download,
        "upload": upload,
        "ping": ping,
        "location": location,
        "name": name,
        "country": country,
        "sponsor": sponsor,
        "datetime": timestamp,
        "up": up,
        "down": down
}

print(result)
