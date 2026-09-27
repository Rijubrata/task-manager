from sqlalchemy import select

from .database import SessionLocal
from .models import User


session = SessionLocal()

result = session.execute(
    select(User)
)

stmt = select(User).where(
    User.id == 2
)

result = session.execute(stmt)

user = result.scalar_one_or_none()

print(user)

if user:
    print("ID:", user.id)
    print("Name:", user.name)
    print("Email:", user.email)

session.close()