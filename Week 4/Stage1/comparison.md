# Part B - Run Both Programs, and identify at least five limitations

•	Appointment times are stored as plain strings and are not validated.
•	The enhanced version only checks whether the patient name is empty.
•	Practitioner names can be empty.
•	Appointment times can be empty.
•	Two appointments can be booked with the same practitioner at the same time.

# Part E - Human vs AI Comparison

| Question | Human version | AI version |
|---|---|---|
| Easy to understand? | Yes. The code is simple and uses basic lists, dictionaries and functions. | Yes. It is also beginner-friendly and very similar to the human version. |
| Runs successfully? | Yes. | Yes. |
| Uses only required features? | Yes. | Yes. It only uses lists, dictionaries, functions and printing. |
| Adds assumptions? | Very few. It assumes appointments can be stored in memory and includes a patient-name validation rule. | Very few. It adds a success message after booking an appointment. |
| Handles errors? | Partly. It checks if the patient name is empty. | No. It does not validate patient name, practitioner name or appointment time. |
| Could I explain it? | Yes. | Yes. The AI version uses concepts I understand. |

## Part F - Verification Testing

| Test | Result |
|---|---|
| Normal appointment | Works successfully and stores the appointment. |
| Blank patient name | Raises a ValueError and does not store the appointment. |
| Same practitioner and time | Both appointments are accepted, so the program does not detect scheduling conflicts. |
| patient_name=None | Raises a ValueError because `None` is treated as false. |
| appointment_time=None | The program accepts it because appointment time is not validated. |

## Part G - Controlled Improvement

I chose to add validation for an empty practitioner name.

The original program only checked whether the patient name was empty.
I added a second check that raises a ValueError if the practitioner
name is empty.

I tested the improvement using an empty practitioner name, and the
program correctly rejected the appointment.