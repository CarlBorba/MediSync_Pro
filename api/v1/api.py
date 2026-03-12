from fastapi.routing import APIRouter

from api.v1.endpoints import appointment
from api.v1.endpoints import doctor
from api.v1.endpoints import patient
from api.v1.endpoints import user

api_router = APIRouter()
api_router.include_router(appointment.router, prefix="/appointments", tags=["appointments"])
api_router.include_router(doctor.router, prefix="/doctors", tags=["doctors"])
api_router.include_router(patient.router, prefix="/patients", tags=["patients"])
api_router.include_router(user.router, prefix="/users", tags=["users"])