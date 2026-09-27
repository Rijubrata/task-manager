from sqlalchemy import select

from .database import SessionLocal
from .models import User


session = SessionLocal()

stmt = select(User)

result = session.execute(stmt)

users = result.scalars().all()

for user in users:
    print(
        user.id,
        user.name,
        user.age,
        user.email
    )

session.close()