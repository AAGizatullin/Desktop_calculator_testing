from pages.calculator_page import StandardPage


# The test is designed to add two single-digit numbers
def test_amount_numbers(app):
    standard_page = StandardPage(app)
    result = standard_page.amount_numbers(4, 9)
    assert result == 13


# The test is designed to subtract two numbers. Including polysemantic ones
def test_difference_numbers(app):
    standard_page = StandardPage(app)
    result = standard_page.number_difference(234, 76)
    assert result == 158
