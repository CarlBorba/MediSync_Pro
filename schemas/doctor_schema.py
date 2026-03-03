from sqlmodel import SQLModel, Field

class DoctorSchemaBase(SQLModel):
    name: str
    crm: str = Field(unique=True, index=True)
    specialty: str = Field(index=True)
    mail: str
    phone: str

class DoctorSchemaResponse(DoctorSchemaBase):
    id: int