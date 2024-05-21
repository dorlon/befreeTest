## Welcome to my API Drones Automation - Home Assignment

### Exam 1 - Get drones
In this test I get all the drones from the API, also I check if I din't get None
also I assert that the drones data is a list.
Additional assertions to validate values of each drone: drone_code and name


### Exam 2 - Get drone by ID
In this test I get drone by ID. 
if it does, then I get the whole data of the specific drone
also im checking status code 200 for validation, or any error status code of response


### Exam 3 - Get drone image
In this test, I want to check the drone image using the drone ID. 
To do this, I use the drone ID with the get_drone_image function from api_drones.py to get the data of the specific drone. 
Additionally, I want to validate that the value of the "Content-Type" header, which holds the type of the content, indicates that it is an image type.


## How to run 
1. Clone this project to your local computer.
2. This project already contains the packages (requests, configparser, pytest) folder for your ease, so if you're using Windows - just type in the terminal "pytest"
3. And all set!

Good luck! :)
