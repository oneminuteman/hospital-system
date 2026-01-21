# hospital-system
# Hospital Priority Queue System

## Description
This system simulates a hospital reception and arrival area using an adaptable priority queue.
Patients are assigned priority based on medical factors.

---

## Priority Formula
Priority is calculated as:

priority = (temperature × 2) + age

### Why temperature matters more
High temperature may indicate severe infection and requires immediate attention.
Multiplying by 2 increases its influence.

### Why age matters
Older patients are generally more vulnerable and require quicker medical response.

---

## Data Structure Used
A Priority Queue implemented using Python’s heapq (binary heap).

Each patient is stored as:
(priority, patient_id, patient_object)

patient_id avoids comparison conflicts.

---

## Algorithm Analysis

| Operation | Complexity |
|---------|------------|
| Insert Patient | O(log n) |
| Serve Patient | O(log n) |
| View Next | O(1) |
| Update Priority | O(n) + O(log n) |

Updating priority requires removing and reinserting because heaps do not support direct updates.

---

## Features Implemented
- Reception area (Add Patient)
- Arrival area (Serve Patient)
- Adaptable priority update
- GUI using Tkinter
