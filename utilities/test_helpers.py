import requests
def get_data_for_drones(api):
    response = api.get_drones()
    if isinstance(response, requests.models.Response):  # Check if the response is an instance of requests response
        data = response.json()
        return data
    else:
        print(response)  # Print the error message if response is not successful
        return None