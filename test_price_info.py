from price_info import total_cost_shopping,cost_of_fruits

def test_total_cost():
    total_cost =46.75
    assert(total_cost_shopping()==total_cost)

def test_fruit_cost():
    
    assert (cost_of_fruits("apple",5)==6.0)