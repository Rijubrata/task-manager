from sqlalchemy import select

from .database import SessionLocal
from .models import User


session = SessionLocal()

stmt = select(User).where(User.id == 2)

result = session.execute(stmt)

user = result.scalar_one_or_none()

if user:
    print("Deleting:", user.name, user.email)

    session.delete(user)

    session.commit()

    print("User deleted")
else:
    print("User not found")

session.close()