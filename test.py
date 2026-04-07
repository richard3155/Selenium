import pytest
import allure
from receipt import calculate_total, generate_receipt


@allure.feature("Кассовый модуль")
class TestReceipt:

    @allure.story("Расчёт стоимости")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_total_correct(self):
        items = [("A", 100), ("B", 100)]
        result = calculate_total(items, discount=10, tax=10)
        assert result == 198.0

    @allure.story("Валидация")
    def test_negative_price(self):
        with pytest.raises(ValueError):
            calculate_total([("A", -10)])

    @allure.story("Валидация")
    def test_empty_cart(self):
        with pytest.raises(ValueError):
            calculate_total([])

    @allure.story("Валидация")
    def test_discount_limit(self):
        with pytest.raises(ValueError):
            calculate_total([("A", 100)], discount=60)

    @allure.story("Расчёт стоимости")
    def test_receipt_generation(self):
        items = [("A", 50)]
        receipt = generate_receipt(items, "card")
        assert "Итого" in receipt
        assert "card" in receipt

    @allure.story("Граничные случаи")
    def test_edge_cases(self):
        items = [("Service", 100)]
        result = calculate_total(items, discount=50, tax=0)
        assert result == 50.0