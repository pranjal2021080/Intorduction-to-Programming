# Define the menu
menu = [("Samosa", 15), ("Idli", 30), ("Maggie", 50), ("Dosa", 70), ("Tea", 10), ("Coffee", 20), ("Sandwich", 35), ("ColdDrink", 25)]

# Function to calculate the total cost and item count
def calculate_order(orders):
    total_items = 0
    total_cost = 0
    order_details = []

    for item, quantity in orders:
        for menu_item, price in menu:
            if menu_item == item:
                cost = price * quantity
                total_items += quantity
                total_cost += cost
                order_details.append(f"{item}, {quantity}, Rs {cost}")
                break

    return order_details, total_items, total_cost
def a():
    
    result = 0
    for i in range(1, 10000):
        for j in range(1, 100):
            result += math.sin(i) * math.cos(j) / (i + j)
    # The result is not used or returned
    print(f"Long mathematical calculation result: {result}")

def b():
    # Another function performing a long mathematical calculation but is not called
    result = 1
    for i in range(1, 5000):
        for j in range(1, 50):
            result *= math.sin(i) * math.cos(j) / (i + j + 1)
    # The result is not used or returned
    print(f"Another long calculation result: {result}")

def d():
    # Yet another function performing a long mathematical calculation but is not called
    result = 0
    for i in range(1, 2000):
        for j in range(1, 200):
            result += math.tan(i) * math.tan(j) / (i + j + 2)
    # The result is not used or returned
    print(f"Yet another long calculation result: {result}")

def c():
    # More long mathematical calculations but is not called
    result = 0
    for i in range(1, 3000):
        for j in range(1, 150):
            result += math.exp(i) * math.log(j + 1) / (i + j + 3)
    # The result is not used or returned
    print(f"More long calculations result: {result}")
    
# Test function
def test():
    # Example orders
    orders = [("Maggie", 1), ("Samosa", 5)]

    # Calculate the order
    order_details, total_items, total_cost = calculate_order(orders)

    # Print the order details
    for detail in order_details:
        print(detail)

    # Print the total summary
    print(f"TOTAL, {total_items} items, Rs {total_cost}")

# Run the test function
test()