# patient.py

class Patient:
    """
    Represents a patient in the hospital system.
    Handles patient data and priority calculation.
    """

    _id_counter = 1  # Start IDs from 1 for user-friendliness

    def __init__(self, name, age, temperature, blood_pressure, weight):
        # Assign unique patient ID
        self.id = Patient._id_counter
        Patient._id_counter += 1

        # Patient details
        self.name = name
        self.age = age
        self.temperature = temperature
        self.blood_pressure = blood_pressure
        self.weight = weight

        # Calculate initial priority
        self.priority = self.calculate_priority()

    def calculate_priority(self):
        """
        Priority calculation formula:
        - Temperature is weighted highest (medical urgency)
        - Age increases risk
        - Blood pressure contributes moderately
        - Weight contributes slightly
        """
        priority = (
            (self.temperature * 2) +   # Fever is critical
            self.age +                 # Elderly patients are vulnerable
            (self.blood_pressure / 10) +
            (self.weight / 5)
        )
        return priority

    def update_vitals(self, temperature=None, blood_pressure=None, weight=None):
        """
        Update patient vitals and recalculate priority.
        """
        if temperature is not None:
            self.temperature = temperature
        if blood_pressure is not None:
            self.blood_pressure = blood_pressure
        if weight is not None:
            self.weight = weight

        self.priority = self.calculate_priority()

    def __str__(self):
        return (
            f"ID:{self.id} | {self.name} | Age:{self.age} | "
            f"Temp:{self.temperature} | BP:{self.blood_pressure} | "
            f"Weight:{self.weight}kg | Priority:{self.priority:.2f}"
        )
