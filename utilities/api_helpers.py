import requests
import configparser


class ApiHelper:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('automation_framework/config/config.ini')
        self.base_url = config.get('URL', 'BASE_URL')
        self.drones = config.get('API', 'DRONES')

    def get_drones(self):
        response = requests.get(f"{self.base_url}/{self.drones}")
        if response.status_code == 200:
            return response
        else:
            return f"Error: {response.status_code}"

    def get_drone_by_id(self, drone_id):
        response = requests.get(f"{self.base_url}/{self.drones}/{drone_id}")
        if response.status_code == 200:
            return response
        else:
            return f"Error: {response.status_code}"

    def get_drone_image(self, drone_id):
        response = requests.get(f"{self.base_url}/{self.drones}/{drone_id}/image")
        if response.status_code == 200:
            return response
        else:
            return f"Error: {response.status_code}"
