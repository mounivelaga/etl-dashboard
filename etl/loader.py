from sqlalchemy.orm import sessionmaker

from database.connection import engine
from database.models import Order


class DataLoader:
    def __init__(self):
        session = sessionmaker(bind=engine)
        self.session = session()

    def load(self, data):
        for _, row in data.iterrows():
            existing = (
                self.session.query(Order).filter_by(order_id=row["order_id"]).first()
            )

            if existing:
                print(f"skipped duplicate Order ID: {row['order_id']}")
                continue

            order = Order(
                order_id=row["order_id"],
                customer_name=row["customer_name"],
                email=row["email"],
                amount=row["amount"],
                order_date=row["order_date"],
            )
            self.session.add(order)

        self.session.commit()

        print(f"{len(data)} Records loaded sucessfully..")
