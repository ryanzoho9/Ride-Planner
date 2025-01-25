import requests


def geocoding(address):
    address = address
    url = "https://geocode.maps.co/search"
    params = {"q": address, "api_key": "6794c4d24174c941914862fej683978"}

    response = requests.get(url, params=params)

    assert response.status_code == 200, f"Error: {response.status_code}"
    try:
        json_response = response.json()
        coordX = float(json_response[0]["lat"])
        coordY = float(json_response[0]["lon"])
        return (coordX, coordY)
    except:
        return "Err Occurred in Geocoding AP"
