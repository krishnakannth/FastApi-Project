from fastapi import FastAPI
import json
from models import Employee
from mongoengine import connect

app = FastAPI()
connect(db="hrms", host="localhost", port=27017)


@app.get("/")
def home():
    return "Hello World"


from pydantic import BaseModel


class NewEmployee(BaseModel):
    name: str
    age: int
    teams: list
    emp_id: int


@app.post("/NewEmployee")
def add_employee(employee: NewEmployee):
    new_employee = Employee(
        name=employee.name,
        age=employee.age,
        teams=employee.teams,
        emp_id=employee.emp_id
    )

    new_employee.save()

    return {
        "data": "Employee has been added successfully"
    }


@app.get("/get_all_employees")
def get_all_employees():
    employees = Employee.objects().to_json()
    # print(employees)
    employees_list = json.loads(employees)
    print(employees_list)
    return {"employees": employees_list}


@app.get("/get_employee/{emp_id}")
def get_employee_by_id(emp_id: int):
    print(emp_id)
    employees = Employee.objects.get(emp_id=emp_id)
    employee_dict = {
        "emp_id": employees.emp_id,
        "name": employees.name,
        "age": employees.age,
        "teams": employees.teams,

    }
    return employee_dict



