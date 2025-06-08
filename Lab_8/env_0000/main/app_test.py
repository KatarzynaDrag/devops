import pytest
import requests

# API base URL
base_url = "http://127.0.0.1:5000"

@pytest.mark.parametrize("num1, num2, expected_result", [
    (5, 3, 8),   # addition
    (10, 4, 6),  # subtraction
    (6, 7, 42),  # multiplication
    (20, 5, 4)   # division
])
def test_calculator_operations(num1, num2, expected_result):
    # Test addition
    if expected_result == 8:
        operation = "add"
    elif expected_result == 6:
        operation = "subtract"
    elif expected_result == 42:
        operation = "multiply"
    elif expected_result == 4:
        operation = "divide"

    data = {"liczba1": num1, "liczba2": num2}
    response = requests.post(f"{base_url}/{operation}", json=data)
    assert response.status_code == 200
    assert response.json()["result"] == expected_result