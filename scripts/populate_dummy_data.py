from faker import Faker
import random
fake = Faker()
for _ in range(50000):
    student = {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'email': fake.email(),
        'campus_id': random.randint(1,5),
        'department_id': random.randint(1,20),
        'semester': random.randint(1,8),
    }
    # Insert into PostgreSQL DB
