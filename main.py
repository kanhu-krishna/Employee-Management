from fastapi import FastAPI,HTTPException,Depends
from typing import List
import models,schemas
from database import engine,SessionLocal
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()    

#CRUD for department
@app.post("/departments/",response_model=schemas.Department)
async def create_department(department: schemas.DepartmentCreate, db: Session = Depends(get_db)):
    db_department = models.Department(name=department.name)
    db.add(db_department)
    db.commit()
    db.refresh(db_department)
    return db_department

@app.get("/departments/",response_model=List[schemas.Department])
async def read_departments(skip: int = 0,limit: int = 10,db: Session = Depends(get_db)):
    return db.query(models.Department).offset(skip).limit(limit).all()

#CRUD fro role
@app.post("/roles/",response_model=schemas.Role)
async def create_role(role: schemas.RoleCreate, db: Session = Depends(get_db)):
    db_role = models.Role(title=role.title)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role


@app.get("/roles/",response_model=List[schemas.Role])
async def read_roles(skip: int = 0,limit: int = 10,db: Session = Depends(get_db)):
    return db.query(models.Role).offset(skip).limit(limit).all()

#CRUD for employee
@app.post("/employees/",response_model=schemas.Employee)
async def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = models.Employee(
        name=employee.name,
        age=employee.age,
        department_id=employee.department_id,
        role_id=employee.role_id
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

@app.get("/employees/",response_model=List[schemas.Employee])
async def read_employees(skip: int = 0,limit: int = 10,db: Session = Depends(get_db)):
    return db.query(models.Employee).offset(skip).limit(limit).all()

@app.put("/employees/{employee_id}",response_model=schemas.Employee)
async def update_employee(employee_id: int, employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    db_employee =db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if not db_employee:
        raise HTTPException(status_code=404, details="Employee not found")
    db_employee.name=employee.name,
    db_employee.age=employee.age,
    db_employee.department_id=employee.department_id,
    db_employee.role_id=employee.role_id
    db.commit()
    db.refresh(db_employee)
    return db_employee

@app.delete("/employees/{employee_id}", response_model=dict)
async def delete_employee(employee_id: int, db: Session = Depends(get_db)):
      db_employee =db.query(models.Employee).filter(models.Employee.id == employee_id).first()
      if not db_employee:
        raise HTTPException(status_code=404, details="Employee not found")
      db.delete(db_employee)
      db.commit()
      return {"message": "Employee deleted successfully"}

#crud for project

#crud for attendance
#crud for salary

