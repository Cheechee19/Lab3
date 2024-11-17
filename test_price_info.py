import price_info as price

def test_total_cost():
    total=price.total_cost_shopping()
    assert(total==46.75)
def test_fruit_cost():
    total=price.cost_of_fruits('orange',10)
    assert(total==14)