def format_amount(amount: float) -> str:
    """Format whole numbers without trailing .0, and decimals to 2 places."""
    if amount.is_integer():
        return str(int(amount))
    return f"{amount:.2f}"


def main() -> None:
    customer_name = input("Enter customer name: ").strip()

    product_1 = input("Enter name of Product 1: ").strip()
    price_1 = float(input(f"Enter price of {product_1 or 'Product 1'}: "))

    product_2 = input("Enter name of Product 2: ").strip()
    price_2 = float(input(f"Enter price of {product_2 or 'Product 2'}: "))

    product_3 = input("Enter name of Product 3: ").strip()
    price_3 = float(input(f"Enter price of {product_3 or 'Product 3'}: "))

    subtotal = price_1 + price_2 + price_3

    if subtotal >= 5000:
        discount_rate = 0.20
    elif subtotal >= 3000:
        discount_rate = 0.10
    elif subtotal >= 1000:
        discount_rate = 0.05
    else:
        discount_rate = 0.0

    discount = subtotal * discount_rate
    final_total = subtotal - discount

    summary = (
        f"\nCustomer Name: {customer_name}\n"
        f"Product 1: {product_1}\n"
        f"Price: {format_amount(price_1)}\n"
        f"Product 2: {product_2}\n"
        f"Price: {format_amount(price_2)}\n"
        f"Product 3: {product_3}\n"
        f"Price: {format_amount(price_3)}\n"
        f"Subtotal: {format_amount(subtotal)}\n"
        f"Discount: {format_amount(discount)}\n"
        f"Final Total: {format_amount(final_total)}"
    )
    print(summary)


if __name__ == "__main__":
    main()
