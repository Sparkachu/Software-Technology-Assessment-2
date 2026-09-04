# AI Usage

## Part C - AI as Tutor

Tool used: Microsoft Copilot

### Prompt

You said:
Act as a Python tutor. I am learning introductory software technology. Here is a small appointment-booking function. 1. Explain what the code does. 2. Identify three limitations. 3. Suggest improvements. 4. Do not rewrite the whole application. 5. Ask me two questions to test my understanding.

Use lists, dictionaries and functions to enhance the Python file
 
appointments = []
 
def book_appointment(patient_name, practitioner_name, appointment_time):
    if not patient_name:
        raise ValueError("Patient name cannot be empty")
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
display_appointments()

### Useful suggestions
- Validate practitioner name and appointment time.
- Prevent duplicate bookings for the same practitioner and time.
- Consider using better date/time validation.
- The program only stores data while it is running.

### Incorrect or unclear suggestion
Copilot said that `display_appointments()` is never called. This was incorrect because the provided program calls `display_appointments()` at the end.

### What I learned
The code uses a list to store appointments, dictionaries to store the details of each appointment, and functions to book and display appointments.

## Part D - Generate an Alternative
Create a simple, beginner-friendly Python function that stores a patient's name, practitioner's name, and appointment time. Use basic Python concepts such as lists, dictionaries, and functions. Do not use a database or GUI. Keep the code simple enough for a beginner Python student to understand.

Copilot said:
Here's a simple, beginner-friendly example that uses a list, dictionary, and functions to store appointment information.


Python
List to store appointments
appointments = []
 
Function to book an appointment
def book_appointment(patient_name, practitioner_name, appointment_time):
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
 
    appointments.append(appointment)
    print("Appointment booked successfully!")
 
Function to display all appointments
def display_appointments():
    if not appointments:
        print("No appointments recorded.")
        return
 
    print("\nAppointments:")
    for appointment in appointments:
        print(
            f"Patient: {appointment['patient']}, "
            f"Practitioner: {appointment['practitioner']}, "
            f"Time: {appointment['time']}"
        )
 
Example appointments
book_appointment("Alice Smith", "Dr. John Doe", "10:00 AM")
book_appointment("Bob Johnson", "Dr. Jane Roe", "11:30 AM")
 
Show all appointments
display_appointments()

Show less
How it works
List (appointments): Stores all appointment records.
Dictionary (appointment): Stores the details of one appointment using keys:
"patient"
"practitioner"
"time"
Function (book_appointment): Creates and stores a new appointment.
Function (display_appointments): Loops through the list and displays all appointments.
This example is suitable for an introductory Python student because it demonstrates the core concepts of variables, lists, dictionaries, functions, and loops without adding advanced features such as databases, files, or graphical interfaces.