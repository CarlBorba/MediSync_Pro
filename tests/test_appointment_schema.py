import pytest
from pydantic import ValidationError
from datetime import date, time

from schemas.appointment_schema import AppointmentSchemaBase

def test_appointment_schema_valid():
    data = {
        "ap_date":"2026-03-10",
        "ap_time":"14:00:00",
        "doctor_id":1,
        "patient_id":1,
        "status":"Pending"
    }

    appointment = AppointmentSchemaBase(**data)

    assert appointment.doctor_id == 1
    assert isinstance(appointment.ap_date, date)