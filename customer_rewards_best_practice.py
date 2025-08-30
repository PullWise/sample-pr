from typing import List, Dict


class Customer:
    """
    Represents a customer with a rewards points account.
    """

    def __init__(self, customer_id: str, points: int = 0) -> None:
        self.customer_id = customer_id
        self.points = points

    def add_points(self, amount: float) -> None:
        """
        Add reward points based on the purchase amount.

        Args:
            amount (float): Purchase amount in dollars.
        """
        earned_points = int(amount // 10)  # 1 point per $10
        self.points += earned_points

    def redeem_points(self, points: int) -> float:
        """
        Redeem points for a discount.

        Args:
            points (int): Points to redeem.

        Returns:
            float: Discount amount.
        """
        if points > self.points:
            points = self.points
        self.points -= points
        return points * 0.5  # Each point worth $0.5


def main() -> None:
    customer = Customer(customer_id="CUST001")
    customer.add_points(250)  # Earn 25 points
    discount = customer.redeem_points(10)  # Redeem 10 points
    print(f"Customer points remaining: {customer.points}")
    print(f"Discount applied: ${discount:.2f}")


if __name__ == "__main__":
    main()
