from typing import List, Dict


class Product:
    """
    Represents a product in the catalog.
    """

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price


class OrderItem:
    """
    Represents a line item in an order.
    """

    def __init__(self, product: Product, quantity: int) -> None:
        self.product = product
        self.quantity = quantity


class Order:
    """
    Represents a customer's order containing multiple items.
    """

    def __init__(self, customer_id: str, items: List[OrderItem]) -> None:
        self.customer_id = customer_id
        self.items = items

    def total_amount(self) -> float:
        """
        Calculate the total order amount without discounts.
        """
        return sum(item.product.price * item.quantity for item in self.items)

    def apply_discount(self, discount_rate: float) -> float:
        """
        Apply a percentage discount to the total amount.

        Args:
            discount_rate (float): Discount rate in percentage (e.g., 10 for 10%).

        Returns:
            float: Total amount after discount.
        """
        total = self.total_amount()
        discount = total * (discount_rate / 100)
        return total - discount


def generate_invoice(order: Order, discount_rate: float = 0.0) -> Dict[str, float]:
    """
    Generate a summary invoice for the order.

    Args:
        order (Order): The order to process.
        discount_rate (float, optional): Discount rate to apply. Defaults to 0.0.

    Returns:
        Dict[str, float]: Invoice with subtotal, discount, and total amount.
    """
    subtotal = order.total_amount()
    total = order.apply_discount(discount_rate)
    discount_amount = subtotal - total
    return {"subtotal": subtotal, "discount": discount_amount, "total": total}


def main() -> None:
    """
    Example usage of the order processing system.
    """
    product1 = Product(name="Laptop", price=1200.0)
    product2 = Product(name="Mouse", price=25.0)
    product3 = Product(name="Keyboard", price=45.0)

    items = [
        OrderItem(product=product1, quantity=1),
        OrderItem(product=product2, quantity=2),
        OrderItem(product=product3, quantity=1),
    ]

    order = Order(customer_id="CUST123", items=items)
    invoice = generate_invoice(order, discount_rate=10.0)

    print("Invoice Summary:")
    print(f"Subtotal: ${invoice['subtotal']:.2f}")
    print(f"Discount: ${invoice['discount']:.2f}")
    print(f"Total: ${invoice['total']:.2f}")


if __name__ == "__main__":
    main()
