import pytest
from automation_framework.utilities.api_helpers import ApiHelper
from automation_framework.utilities.test_helpers import get_data_for_drones

class TestDrones:
    @pytest.fixture(scope="class")
    def api(self):
        return ApiHelper()

    def test_get_drones(self, api):
        drone_data = get_data_for_drones(api)

        # Assert that the drone data is not None
        assert drone_data is not None, "Drone data is None"

        # Assert that the drone data is a list (assuming the API returns a list of drones)
        assert isinstance(drone_data, list), "Drone data is not a list"

        # Additional assertions could be made based on the expected structure of the drone data
        if drone_data:
            for drone in drone_data:
                assert 'drone_code' in drone, "Drone entry does not have 'id'"
                assert 'name' in drone, "Drone entry does not have 'name'"
                # Add more assertions based on the expected fields in the drone data

    def test_get_drone_by_id(self, api):
        # Assuming there is a drone with ID 1 for the test
        drone_id = "M3T"
        response = api.get_drone_by_id(drone_id)

        # Assert that the response is not None
        assert response is not None, f"Response for drone ID {drone_id} is None"

        # Assert that the status code is 200
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

        # Additional assertions could be made based on the expected structure of the response

    def test_get_drone_image(self, api):
        # Assuming there is a drone with ID 1 for the test
        drone_id = "M3T"
        response = api.get_drone_image(drone_id)

        # Assert that the response is not None
        assert response is not None, f"Response for drone image ID {drone_id} is None"

        # Assert that the status code is 200
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

        # Assert that the content type is an image
        content_type = response.headers.get('Content-Type', '')
        assert content_type.startswith('image/'), "Response is not an image"

        # Print the address of the image
        print(f"The address of the image for drone ID {drone_id} is: {response.url}")