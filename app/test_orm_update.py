from sqlalchemy import select

from .database import SessionLocal
from .models import User


session = SessionLocal()

stmt = select(User).where(User.id == 2)

result = session.execute(stmt)

user = result.scalar_one_or_none()

if user:
    print("Before:", user.name)

    user.name = "Riju Updated"

    session.commit()

    print("After:", user.name)

session.close()