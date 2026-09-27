from sqlalchemy import select

from .database import SessionLocal
from .models import User


session = SessionLocal()

result = session.execute(
    select(User)
)

users = result.scalars().all()

for user in users:
    print(
        user.id,
        user.name,
        user.email
    )

session.close()