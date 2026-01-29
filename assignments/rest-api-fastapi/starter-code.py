"""
REST API with FastAPI - Starter Code
Complete the implementation of a task management API
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import json
import os

app = FastAPI(title="Task Manager API", version="1.0")

# TODO: Define your Pydantic model for a Task
class Task(BaseModel):
    pass  # Add fields: id, title, description, completed


# TODO: Initialize an empty list to store tasks
tasks = []

# TODO: Implement file operations to save and load tasks
DATA_FILE = "tasks.json"


def load_tasks():
    """Load tasks from JSON file"""
    pass  # Implement this function


def save_tasks():
    """Save tasks to JSON file"""
    pass  # Implement this function


# TODO: Implement GET endpoint to retrieve all tasks
@app.get("/tasks")
def get_tasks():
    """Get all tasks"""
    pass


# TODO: Implement POST endpoint to create a new task
@app.post("/tasks")
def create_task(task: Task):
    """Create a new task"""
    pass


# TODO: Implement PUT endpoint to update a task
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    """Update an existing task"""
    pass


# TODO: Implement DELETE endpoint to remove a task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    """Delete a task"""
    pass


# Optional: Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Manager API"}
