from datetime import datetime, timedelta
class Clinic:
    def __init__(self, day, start_time, end_time, doctor, room, department, specialization):
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
        self.doctor = doctor
        self.room = room
        self.department = department
        self.specialization = specialization

    def __repr__(self):
        remaining_time = datetime.combine(datetime.today(), self.end_time) - datetime.now()
        remaining_minutes = remaining_time.total_seconds() / 60 if remaining_time.total_seconds() > 0 else 0
        return (f"Clinic(day={self.day}, start_time={self.start_time.strftime('%H:%M')}, "
                f"end_time={self.end_time.strftime('%H:%M')}, doctor={self.doctor}, room={self.room}, "
                f"department={self.department}, specialization={self.specialization}, "
                f"remaining_minutes={remaining_minutes:.2f})")

# Helper function to convert time strings to datetime objects
def convert_time(time_str):
    return datetime.strptime(time_str, '%H:%M').time()

# Create a schedule dictionary with 7 clinics for each day, department, and specialization
schedule = {
    'Monday': [
        Clinic('Monday', convert_time('08:00'), convert_time('09:00'), 'Dr. Smith', 'Room 101', 'Dentistry', 'Orthodontics'),
        Clinic('Monday', convert_time('09:00'), convert_time('10:00'), 'Dr. Johnson', 'Room 102', 'Cardiology', 'Pediatric Cardiology'),
        Clinic('Monday', convert_time('10:00'), convert_time('11:00'), 'Dr. Williams', 'Room 103', 'Neurology', 'Epilepsy'),
        Clinic('Monday', convert_time('11:00'), convert_time('12:00'), 'Dr. Brown', 'Room 104', 'Oncology', 'Radiation Oncology'),
        Clinic('Monday', convert_time('12:00'), convert_time('13:00'), 'Dr. Jones', 'Room 105', 'Pediatrics', 'Neonatology'),
        Clinic('Monday', convert_time('13:00'), convert_time('14:00'), 'Dr. Davis', 'Room 106', 'Orthopedics', 'Sports Medicine'),
        Clinic('Monday', convert_time('14:00'), convert_time('15:00'), 'Dr. Garcia', 'Room 107', 'Gastroenterology', 'Hepatology')
    ],
    'Tuesday': [
        Clinic('Tuesday', convert_time('08:00'), convert_time('09:00'), 'Dr. Martinez', 'Room 108', 'Pulmonology', 'Sleep Medicine'),
        Clinic('Tuesday', convert_time('09:00'), convert_time('10:00'), 'Dr. Rodriguez', 'Room 109', 'Dermatology', 'Cosmetic Dermatology'),
        Clinic('Tuesday', convert_time('10:00'), convert_time('11:00'), 'Dr. Wilson', 'Room 110', 'Psychiatry', 'Child Psychiatry'),
        Clinic('Tuesday', convert_time('11:00'), convert_time('12:00'), 'Dr. Anderson', 'Room 111', 'Ophthalmology', 'Glaucoma'),
        Clinic('Tuesday', convert_time('12:00'), convert_time('13:00'), 'Dr. Taylor', 'Room 112', 'ENT', 'Rhinology'),
        Clinic('Tuesday', convert_time('13:00'), convert_time('14:00'), 'Dr. Thomas', 'Room 113', 'Urology', 'Andrology'),
        Clinic('Tuesday', convert_time('14:00'), convert_time('15:00'), 'Dr. Lee', 'Room 114', 'Endocrinology', 'Diabetes')
    ],
    'Wednesday': [
        Clinic('Wednesday', convert_time('08:00'), convert_time('09:00'), 'Dr. Harris', 'Room 115', 'Cardiology', 'Pediatric Cardiology'),
        Clinic('Wednesday', convert_time('09:00'), convert_time('10:00'), 'Dr. Clark', 'Room 116', 'Neurology', 'Epilepsy'),
        Clinic('Wednesday', convert_time('10:00'), convert_time('11:00'), 'Dr. Lewis', 'Room 117', 'Oncology', 'Radiation Oncology'),
        Clinic('Wednesday', convert_time('11:00'), convert_time('12:00'), 'Dr. Walker', 'Room 118', 'Pediatrics', 'Neonatology'),
        Clinic('Wednesday', convert_time('12:00'), convert_time('13:00'), 'Dr. Hall', 'Room 119', 'Orthopedics', 'Sports Medicine'),
        Clinic('Wednesday', convert_time('13:00'), convert_time('14:00'), 'Dr. Allen', 'Room 120', 'Gastroenterology', 'Hepatology'),
        Clinic('Wednesday', convert_time('14:00'), convert_time('15:00'), 'Dr. Young', 'Room 121', 'Pulmonology', 'Sleep Medicine')
    ],
    'Thursday': [
        Clinic('Thursday', convert_time('08:00'), convert_time('09:00'), 'Dr. King', 'Room 122', 'Dermatology', 'Cosmetic Dermatology'),
        Clinic('Thursday', convert_time('09:00'), convert_time('10:00'), 'Dr. Wright', 'Room 123', 'Psychiatry', 'Child Psychiatry'),
        Clinic('Thursday', convert_time('10:00'), convert_time('11:00'), 'Dr. Lopez', 'Room 124', 'Ophthalmology', 'Glaucoma'),
        Clinic('Thursday', convert_time('11:00'), convert_time('12:00'), 'Dr. Hill', 'Room 125', 'ENT', 'Rhinology'),
        Clinic('Thursday', convert_time('12:00'), convert_time('13:00'), 'Dr. Scott', 'Room 126', 'Urology', 'Andrology'),
        Clinic('Thursday', convert_time('13:00'), convert_time('14:00'), 'Dr. Green', 'Room 127', 'Endocrinology', 'Diabetes'),
        Clinic('Thursday', convert_time('14:00'), convert_time('15:00'), 'Dr. Adams', 'Room 128', 'Cardiology', 'Pediatric Cardiology')
    ],
    'Friday': [
        Clinic('Friday', convert_time('08:00'), convert_time('09:00'), 'Dr. Baker', 'Room 129', 'Neurology', 'Epilepsy'),
        Clinic('Friday', convert_time('09:00'), convert_time('10:00'), 'Dr. Gonzalez', 'Room 130', 'Oncology', 'Radiation Oncology'),
        Clinic('Friday', convert_time('10:00'), convert_time('11:00'), 'Dr. Nelson', 'Room 131', 'Pediatrics', 'Neonatology'),
        Clinic('Friday', convert_time('11:00'), convert_time('12:00'), 'Dr. Carter', 'Room 132', 'Orthopedics', 'Sports Medicine'),
        Clinic('Friday', convert_time('12:00'), convert_time('13:00'), 'Dr. Mitchell', 'Room 133', 'Gastroenterology', 'Hepatology'),
        Clinic('Friday', convert_time('13:00'), convert_time('14:00'), 'Dr. Perez', 'Room 134', 'Pulmonology', 'Sleep Medicine'),
        Clinic('Friday', convert_time('14:00'), convert_time('15:00'), 'Dr. Roberts', 'Room 135', 'Dermatology', 'Cosmetic Dermatology')
    ],
    'Saturday': [
        Clinic('Saturday', convert_time('08:00'), convert_time('09:00'), 'Dr. Turner', 'Room 136', 'Psychiatry', 'Child Psychiatry'),
        Clinic('Saturday', convert_time('09:00'), convert_time('10:00'), 'Dr. Phillips', 'Room 137', 'Ophthalmology', 'Glaucoma'),
        Clinic('Saturday', convert_time('10:00'), convert_time('11:00'), 'Dr. Campbell', 'Room 138', 'ENT', 'Rhinology'),
        Clinic('Saturday', convert_time('11:00'), convert_time('12:00'), 'Dr. Parker', 'Room 139', 'Urology', 'Andrology'),
        Clinic('Saturday', convert_time('12:00'), convert_time('13:00'), 'Dr. Evans', 'Room 140', 'Endocrinology', 'Diabetes'),
        Clinic('Saturday', convert_time('13:00'), convert_time('14:00'), 'Dr. Edwards', 'Room 141', 'Cardiology', 'Pediatric Cardiology'),
        Clinic('Saturday', convert_time('14:00'), convert_time('15:00'), 'Dr. Collins', 'Room 142', 'Neurology', 'Epilepsy')
    ],
    'Sunday': [
        Clinic('Sunday', convert_time('08:00'), convert_time('09:00'), 'Dr. Stewart', 'Room 143', 'Oncology', 'Radiation Oncology'),
        Clinic('Sunday', convert_time('09:00'), convert_time('10:00'), 'Dr. Sanchez', 'Room 144', 'Pediatrics', 'Neonatology'),
        Clinic('Sunday', convert_time('10:00'), convert_time('11:00'), 'Dr. Morris', 'Room 145', 'Orthopedics', 'Sports Medicine'),
        Clinic('Sunday', convert_time('11:00'), convert_time('12:00'), 'Dr. Rogers', 'Room 146', 'Gastroenterology', 'Hepatology'),
        Clinic('Sunday', convert_time('12:00'), convert_time('13:00'), 'Dr. Reed', 'Room 147', 'Pulmonology', 'Sleep Medicine'),
        Clinic('Sunday', convert_time('13:00'), convert_time('14:00'), 'Dr. Cook', 'Room 148', 'Dermatology', 'Cosmetic Dermatology'),
        Clinic('Sunday', convert_time('14:00'), convert_time('15:00'), 'Dr. Morgan', 'Room 149', 'Psychiatry', 'Child Psychiatry')
    ]
}

# Get the current day and time
current_day = datetime.now().strftime('%A')
current_time = datetime.now().time()

# Print the available clinics for today
print(f"Available clinics on {current_day}:")
if current_day in schedule:
    # Organize clinics by department
    clinics_by_department = {}
    c=0
    for clinic in schedule[current_day]:
        if clinic.end_time > current_time:
            c+=1
            if clinic.department not in clinics_by_department:
                clinics_by_department[clinic.department] = []
            clinics_by_department[clinic.department].append(clinic)
    if c==0:
        print("  No clinics available today.")
    # Print clinics grouped by department
    for department, clinics in clinics_by_department.items():
        print(f"\nDepartment: {department}")
        for clinic in clinics:
            remaining_time = datetime.combine(datetime.today(), clinic.end_time) - datetime.now()
            remaining_minutes = remaining_time.total_seconds() / 60
            print(f"  Clinic in {clinic.specialization} with {clinic.doctor} in {clinic.room} until {clinic.end_time.strftime('%H:%M')} "
                  f"({remaining_minutes:.2f} minutes remaining)")

