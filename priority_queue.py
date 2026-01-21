# priority_queue.py

import heapq


class AdaptablePriorityQueue:
    """
    Adaptable Priority Queue using heapq.
    """

    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def add_patient(self, patient):
        """
        Insert patient into priority queue.
        Negative priority is used because heapq is a min-heap.
        """
        heapq.heappush(self.heap, (-patient.priority, patient.id, patient))

    def serve_next_patient(self):
        """
        Remove and return the highest-priority patient.
        """
        if self.is_empty():
            return None
        return heapq.heappop(self.heap)[2]

    def update_patient_priority(self, patient_id, new_temperature, new_bp, new_weight):
        """
        Update patient priority by removing and reinserting.
        Heap does not support direct updates.
        """
        for i, (_, pid, patient) in enumerate(self.heap):
            if pid == patient_id:
                # Remove old entry
                self.heap.pop(i)
                heapq.heapify(self.heap)

                # Update patient vitals
                patient.update_vitals(
                    temperature=new_temperature,
                    blood_pressure=new_bp,
                    weight=new_weight
                )

                # Reinsert with updated priority
                self.add_patient(patient)
                return True

        return False  # Patient not found

    def get_all_patients(self):
        """
        Return all patients (unordered view).
        """
        return [item[2] for item in self.heap]
