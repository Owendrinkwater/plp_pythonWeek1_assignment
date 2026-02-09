def calculate_discount(price, discount_percent):
    """calculates the final price after applying a discount.

    Args:
        price (float):  original price 
        discount_percent (float): dicount allowed

    Returns:
        float: If the discount is 20% or higher, 
        apply the discount; otherwise, return the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


# User input
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(price, discount_percent)

# Output result
if final_price < price:
    print(f"Discount applied! Final price: {final_price}")
else:
    print(f"No discount applied. Price remains: {final_price}")
