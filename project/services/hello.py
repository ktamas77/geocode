def get_location_hello(search_text, params):
    hello_app_id = params['app_id']
    hello_app_code = params['app_code']

    url = "https://geocoder.api.here.com/6.2/geocode.json?"
    params = dict(
        app_id=hello_app_id,
        app_code=hello_app_code,
        searchtext=search_text
    )

    try:
        data = requests.get(url=url, params=params)
        binary = data.content
        result = json.loads(binary)
        location = result['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]
        return location
    except Exception as e:
        return None
