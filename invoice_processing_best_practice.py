from typing import List, Dict


class LineItem:
    """
    Represents an item in an invoice.
    """

    def __init__(self, description: str, unit_price: float, quantity: int) -> None:
        self.description = description
        self.unit_price = unit_price
        self.quantity = quantity

    def total(self) -> float:
        """
        Calculate total for this line item.
        """
        return self.unit_price * self.quantity


class Invoice:
    """
    Represents an invoice containing multiple line items.
    """

    def __init__(self, invoice_id: str, items: List[LineItem]) -> None:
        self.invoice_id = invoice_id
        self.items = items

    def subtotal(self) -> float:
        """
        Calculate subtotal for the invoice.
        """
        return sum(item.total() for item in self.items)

    def apply_tax(self, tax_rate: float) -> float:
        """
        Apply tax to the subtotal.

        Args:
            tax_rate (float): Tax percentage (e.g., 5 for 5%).

        Returns:
            float: Total amount including tax.
        """
        return self.subtotal() * (1 + tax_rate / 100)


def main() -> None:
    items = [
        LineItem(description="Chair", unit_price=50.0, quantity=4),
        LineItem(description="Table", unit_price=150.0, quantity=1),
    ]
    invoice = Invoice(invoice_id="INV1001", items=items)
    total = invoice.apply_tax(5.0)
    print(f"Invoice total with tax: ${total:.2f}")


if __name__ == "__main__":
    main()
