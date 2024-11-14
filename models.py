from sqlalchemy import Column,Integer,String,ForeignKey,Date,Boolean,Float
from database import Base
from sqlalchemy.orm import relationship

class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    employees = relationship("Employee", back_populates="department")


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    employees = relationship("Employee", back_populates="role")


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    department_id = Column(Integer, ForeignKey("departments.id"))
    role_id = Column(Integer, ForeignKey("roles.id"))

    department = relationship("Department", back_populates="employees")
    role = relationship("Role", back_populates="employees")

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    date = Column(Date)
    present = Column(Boolean, default=True)

class Salary(Base):
    __tablename__ = "salaries"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    amount = Column(Float)
    date = Column(Date)





