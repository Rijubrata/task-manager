from sqlalchemy import select

from .database import SessionLocal
from .models import User
from sqlalchemy import or_


session = SessionLocal()

# stmt = select(User).where(
#     User.age > 25,
#     User.age < 32
# )

# stmt = select(User).where(
#     or_(
#         User.age < 28,
#         User.age > 31
#     )
# )

# stmt = select(User).where(
#     User.age.in_([25, 30, 32])
# )
# stmt = select(User).order_by(
#     User.age
# )
stmt = select(User).order_by(
    User.age.desc()
).limit(2)

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