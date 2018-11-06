def get_location_google(search_text, params):
    google_api_key = params['api_key']

    url = "https://maps.googleapis.com/maps/api/geocode/json?"
    params = dict(
        key=google_api_key,
        address=search_text
    )

    try:
        data = requests.get(url=url, params=params)
        binary = data.content
        result = json.loads(binary)
        if not result.has_key('status') or result['status'] != 'OK':
            return None

        result_location = result['results'][0]['geometry']['location']
        location = dict(
            Latitude=result_location['lat'],
            Longitude=result_location['lng']
        )
        return location
    except Exception as e:
        return None
