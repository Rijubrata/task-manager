from .database import SessionLocal
from .models import User


session = SessionLocal()

users = [
    User(
        name="Rahul",
        age=28,
        email="rahul@example.com"
    ),
    User(
        name="Priya",
        age=32,
        email="priya@example.com"
    ),
    User(
        name="Amit",
        age=25,
        email="amit@example.com"
    )
]

session.add_all(users)

session.commit()

session.close()