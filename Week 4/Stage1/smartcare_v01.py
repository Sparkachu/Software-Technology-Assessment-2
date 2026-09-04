#task1enhanced
# Use lists, dictionaries and functions to enhance the Python file

appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time):
    if not patient_name:
        raise ValueError("Patient name cannot be empty")
    if not practitioner_name:
        raise ValueError("Practitioner name cannot be empty")
    
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }

    appointments.append(appointment)

def display_appointments():
    if not appointments:
        print("No appointments recorded.")
        return
    
    for appointment in appointments:
        print(f"Patient: {appointment['patient']} | Practitioner: {appointment['practitioner']} | Time: {appointment['time']}")

print("Welcome to SmartCare: The Clinical Appointment Booking System!")
book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM')
book_appointment('Bob Johnson', 'Dr. Jane Roe', '2024-07-20 11:30 AM')


# Test 1 - Normal appointment
#book_appointment("Charlie Brown", "Dr. Jane Roe", "2024-07-20 1:00 PM")

# Test 2 - Blank patient name
#book_appointment("", "Dr. John Doe", "2024-07-20 2:00 PM")

# Test 3 - Same practitioner and time
#book_appointment("Alice Smith", "Dr. John Doe", "2024-07-20 3:00 PM")
#book_appointment("Bob Johnson", "Dr. John Doe", "2024-07-20 3:00 PM")

# Test 4 - Strange input
#book_appointment(None, "Dr. Jane Roe", None)

display_appointments()