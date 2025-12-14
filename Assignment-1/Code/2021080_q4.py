import math

def calculate_population_after_years(initial_pop, growth_rate, years):
    assert initial_pop > 0, "Initial population must be positive."
    assert years >= 0, "Years must be non-negative."
    return initial_pop * (1 + growth_rate / 100) ** years

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

def simulate_world_population(pgrowth):
    pop = [50, 1450, 1400, 1700, 1500, 600, 1200]
    growth_reduction = 0.4
    annual_reduction = 0.1

    total_population = 0
    for p in pop:
        total_population += p
    assert total_population > 0, "Total population must be positive."
    print(f"Current total population: {total_population:.2f} million")

    max_population = total_population
    max_year = 0

    for year in range(1, 101):  # Simulate for up to 100 years
        new_total = 0
        for i in range(7):  # 7 groups
            group_growth = pgrowth - i * growth_reduction - year * annual_reduction
            new_pop = calculate_population_after_years(pop[i], group_growth, 1)
            assert new_pop >= 0, "New population must be non-negative."
            new_total += new_pop
            pop[i] = new_pop

        assert new_total >= 0, "New total population must be non-negative."
        if new_total > max_population:
            max_population = new_total
            max_year = year
        elif new_total < max_population:
            break

    return max_year, max_population

def test():
    assert abs(calculate_population_after_years(100, 2, 5) - 110.40808032) < 0.0001
    assert abs(calculate_population_after_years(200, 3, 10) - 268.78320000) < 0.0001

    # Additional assertions for edge cases
    assert calculate_population_after_years(1, 0, 0) == 1, "Population should remain the same with 0 growth rate and 0 years."
    assert calculate_population_after_years(100, 0, 10) == 100, "Population should remain the same with 0 growth rate."
    assert calculate_population_after_years(100, 2, 0) == 100, "Population should remain the same with 0 years."

    pgrowth_rates = [2.0, 2.25, 2.5, 2.75, 3.0]
    for rate in pgrowth_rates:
        max_year, max_population = simulate_world_population(rate)
        print(f"pgrowth rate: {rate}%")
        print(f"Maximum population reached after {max_year} years")
        print(f"Maximum population: {max_population:.2f} million")

        # Additional assertions for simulate_world_population
        assert max_year > 0, "Max year should be greater than 0."
        assert max_population > 0, "Max population should be greater than 0."

if __name__ == "__main__":
    test()