# 📘 Assignment: REST APIs with FastAPI

## 🎯 Objective

Build a RESTful API using the FastAPI framework to learn modern web service development, HTTP methods, data validation, and API documentation.

## 📝 Tasks

### 🛠️ Create a Task Management API

#### Description
Build a REST API that allows users to create, read, update, and delete tasks. The API should handle task data including title, description, and completion status.

#### Requirements
Completed program should:

- Implement GET endpoint to retrieve all tasks
- Implement POST endpoint to create a new task
- Implement PUT endpoint to update an existing task
- Implement DELETE endpoint to remove a task
- Use Pydantic models for data validation
- Return appropriate HTTP status codes (200, 201, 404, etc.)
- Include automatic API documentation (provided by FastAPI)


### 🛠️ Add Data Persistence

#### Description
Extend your API to save tasks to a JSON file so data persists between server restarts.

#### Requirements
Completed program should:

- Load existing tasks from a JSON file on startup
- Save tasks to the JSON file after each create, update, or delete operation
- Handle file not found errors gracefully
- Maintain data consistency across operations


### 🛠️ Implement Error Handling

#### Description
Add proper error handling and validation to make your API robust and user-friendly.

#### Requirements
Completed program should:

- Return 404 error when a task is not found
- Validate that required fields are present in requests
- Return meaningful error messages in responses
- Handle invalid data types appropriately
