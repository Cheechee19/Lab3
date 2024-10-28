import Lab2.bmi as bmi

def test_bmi_normal_weight():
    weight=70
    height=1.73
    result=bmi.calculate_bmi(height, weight)
    assert result ==0, f"Expected 0 for normal weight, but got {result}"
def test_bmi_over_weight():
    weight=100
    height=1.73
    result=bmi.calculate_bmi(height, weight)
    assert result ==1, f"Expected 0 for over weight, but got {result}"

def test_bmi_under_weight():
    weight=50
    height=1.73
    result=bmi.calculate_bmi(height, weight)
    assert result ==-1, f"Expected 0 for under weight, but got {result}"