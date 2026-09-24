from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class AppointmentStatus(Enum):
    SCHEDULED = "scheduled"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


@dataclass
class Appointment:
    patient: Patient
    practitioner: Practitioner
    appointment_time: datetime
    status: AppointmentStatus = AppointmentStatus.SCHEDULED

    def cancel(self) -> None:
        """
        Cancel the appointment.

        Cancelled appointments are retained as objects and are not deleted.
        """
        if self.status == AppointmentStatus.COMPLETED:
            raise ValueError("A completed appointment cannot be cancelled.")

        if self.status == AppointmentStatus.CANCELLED:
            raise ValueError("Appointment is already cancelled.")

        self.status = AppointmentStatus.CANCELLED

    def update_status(self, new_status: AppointmentStatus) -> None:
        """
        Update the appointment status while enforcing valid transitions.
        """
        if not isinstance(new_status, AppointmentStatus):
            raise TypeError(
                "new_status must be an AppointmentStatus value."
            )

        valid_transitions = {
            AppointmentStatus.SCHEDULED: {
                AppointmentStatus.COMPLETED,
                AppointmentStatus.CANCELLED,
            },
            AppointmentStatus.COMPLETED: set(),
            AppointmentStatus.CANCELLED: set(),
        }

        if new_status == self.status:
            return

        if new_status not in valid_transitions[self.status]:
            raise ValueError(
                f"Invalid status transition from "
                f"{self.status.value} to {new_status.value}."
            )

        self.status = new_status

class Patient:
    def __init__(self, patient_id: str, name: str):
        if not patient_id:
            raise ValueError("Patient ID cannot be empty")
        if not name:
            raise ValueError("Patient name cannot be empty")

        self.patient_id = patient_id
        self.name = name

    def get_details(self) -> str:
        return f"{self.patient_id}: {self.name}"
    
class Practitioner:
    def __init__(self, practitioner_id: str, name: str, specialty: str):
        if not practitioner_id:
            raise ValueError("Practitioner ID cannot be empty")
        if not name:
            raise ValueError("Practitioner name cannot be empty")
        if not specialty:
            raise ValueError("Specialty cannot be empty")

        self.practitioner_id = practitioner_id
        self.name = name
        self.specialty = specialty

    def get_details(self) -> str:
        return f"{self.practitioner_id}: {self.name} - {self.specialty}"

print("TEST 1: Valid objects")

patient = Patient("P001", "Alice")
practitioner = Practitioner("PR001", "Dr Smith", "General Practice")

appointment = Appointment(
    patient,
    practitioner,
    datetime(2026, 9, 24, 10, 0)
)

print(patient.get_details())
print(practitioner.get_details())
print(appointment.status)


print("\nTEST 2: Cancel appointment")

appointment.cancel()
print(appointment.status)


print("\nTEST 3: Cancel already cancelled appointment")

try:
    appointment.cancel()
except ValueError as error:
    print("Error:", error)


print("\nTEST 4: Invalid patient")

try:
    invalid_patient = Patient("P002", "")
except ValueError as error:
    print("Error:", error)