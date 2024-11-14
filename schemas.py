from pydantic import BaseModel
from typing import Optional
from datetime import date

#Department schema
class DepartmentBase(BaseModel):
    name: str
class DepartmentCreate(DepartmentBase):
    pass
class Department(DepartmentBase):
    id: int
    class Config:
        orm_mode = True
        
#Role schema
class Rolebase(BaseModel):
    title: str
class RoleCreate(Rolebase):
    pass
class Role(Rolebase):
    id: int 
    class Config:
        orm_mode = True

#Employee schema
class EmployeeBase(BaseModel):
    name: str
    age: int
    department_id: int
    role_id: int
class EmployeeCreate(EmployeeBase):
    pass
class Employee(EmployeeBase):
    id: int 
    department: Optional[Department]
    role: Optional[Role]
    class Config:
        orm_mode = True

#Project schema
class Projectbase(BaseModel):
    name: str
    description: str
class ProjectCreate(Projectbase):
    pass
class Project(Projectbase):
    id: int 
    class Config:
        orm_mode = True

#attendance schema
class AttendanceBase(BaseModel):
    employee_id: int
    date: date
    present: bool
class AttendanceCreate(AttendanceBase):
    pass
class Attendance(AttendanceBase):
    id: int 
    class Config:
        orm_mode = True

#Sallary schema
class SalaryBase(BaseModel):
    employee_id: int
    amount: float
    date: date
class SalaryCreate(SalaryBase):
    pass
class Salary(SalaryBase):
    id: int 
    class Config:
        orm_mode = True


