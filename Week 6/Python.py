class Patient:
    def __init__(self, patient_id, patient_name):
        self.patient_id = patient_id
        self.patient_name = patient_name



class Practitioner:
    def __init__(self, practitioner_id, practitioner_name):
        self.practitioner_id = practitioner_id
        self.practitioner_name = practitioner_name



class Appointment:
    def __init__(self, patient, practitioner, appointment_time, status):
        self.patient = patient
        self.practitioner = practitioner
        self.appointment_time = appointment_time
        self.status = status

