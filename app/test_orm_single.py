from .database import SessionLocal
from .models import User


session = SessionLocal()

user = User(
    name="Ankit",
    age=30,
    email="ankit@example.com"
)

session.add(user)

session.commit()

print("ID:", user.id)
print("Name:", user.name)
print("Age:", user.age)
print("Email:", user.email)

session.close()