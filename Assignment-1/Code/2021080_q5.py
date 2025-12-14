import math

def compute_demand(a, b, price):
    return math.exp(a - b * price)

def compute_supply(c, d, price):
    return math.exp(c + d * price)

def find_equilibrium_price(a, b, c, d, min_price, max_iterations=1000):
    price = min_price
    for _ in range(max_iterations):
        demand = compute_demand(a, b, price)
        supply = compute_supply(c, d, price)

        if supply >= demand:
            return price, demand, supply

        price *= 1.05  # Increase the price by 5%

    return None, None, None  # No equilibrium found within max_iterations

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

def _test():
    # Test compute_demand
    assert math.isclose(compute_demand(10, 1.05, 1), math.exp(10 - 1.05 * 1), rel_tol=1e-9)
    assert math.isclose(compute_demand(10, 1.05, 2), math.exp(10 - 1.05 * 2), rel_tol=1e-9)

    # Test compute_supply
    assert math.isclose(compute_supply(1, 1.06, 1), math.exp(1 + 1.06 * 1), rel_tol=1e-9)
    assert math.isclose(compute_supply(1, 1.06, 2), math.exp(1 + 1.06 * 2), rel_tol=1e-9)

    # Test find_equilibrium_price
    a = 10
    b = 1.05
    c = 1
    d = 1.06
    min_price = 1.0
    equilibrium = find_equilibrium_price(a, b, c, d, min_price)
    assert equilibrium is not None
    price, demand, supply = equilibrium
    assert supply >= demand

    print("All tests passed!")

def main():
    _test()  # Run tests
    
    a = 10
    b = 1.05
    c = 1
    d = 1.06
    min_price = 1.0

    equilibrium = find_equilibrium_price(a, b, c, d, min_price)
    
    if equilibrium:
        price, demand, supply = equilibrium
        print(f"Equilibrium found at price: {price:.2f}")
        print(f"Demand at equilibrium: {demand:.2f}")
        print(f"Supply at equilibrium: {supply:.2f}")
    else:
        print("No equilibrium found.")

if __name__ == "__main__":
    main()