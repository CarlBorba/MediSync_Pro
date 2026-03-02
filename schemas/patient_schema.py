from typing import Optional

from sqlmodel import SQLModel, Field

class PatientSchemaBase(SQLModel):
    name: str
    age: int
    document_id: str = Field(index=True, unique=True)
    gender: str
    mail: str
    phone: str
    historical: Optional[str] = None
    address: Optional[str] = None

class PatientSchemaResponse(PatientSchemaBase):
    id: int