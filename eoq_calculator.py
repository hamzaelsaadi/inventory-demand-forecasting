def eoq(demand, ordering_cost, holding_cost):
    return ((2 * demand * ordering_cost) / holding_cost) ** 0.5

annual_demand = 10000
ordering_cost = 50
holding_cost = 2

result = eoq(annual_demand, ordering_cost, holding_cost)

print(f"Economic Order Quantity: {result:.2f}")
