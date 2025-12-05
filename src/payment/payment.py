class Payment:
    def __init__(self, payment_id, user_id, amount):
        self.payment_id = payment_id
        self.user_id = user_id
        self.amount = amount

    def display_payment(self):
        print(f"Payment ID: {self.payment_id}, User ID: {self.user_id}, Amount: ${self.amount}")
# Change in payment.py