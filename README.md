# meal-rest-api
Rest API to fetch data from database and display all available meals for a specific day and meal type


# Functionality
Accessing the Rest API
- Using plain HTTP GET request
  - Access localhost:8000/menu/<YYYY-MM-DD>/<meal_type>
  - Here's an example: localhost:8000/menu/2021-03-03/MEAL_KIT

- Using browser to access Swagger documentation
  - Access localhost:8000/docs
  - Use the graphic interface to access endpoints


#### Extra functionality
I took liberty to implement an extra feature to fetch all meals for a determined week
- To access this feature, use Swagger interface or send GET request to localhost:8000/<YYYY-MM-DD>
