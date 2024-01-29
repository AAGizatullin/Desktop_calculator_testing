from pages.base_page import BasePage


class StandardPage(BasePage):

    # Method for adding two single-digit numbers
    def amount_numbers(self, num1, num2) -> int:
        self.click_number(num1)
        if self.get_result() == num1:
            self.click_plus()
            self.click_number(num2)
            if self.get_result() == num2:
                self.click_equal()
                return self.get_result()

    # Method for subtracting two multi-digit numbers. Numbers are entered from the keyboard
    def number_difference(self, num1, num2) -> int:
        self.set_numbers(num1)
        if self.get_result() == num1:
            self.click_minus()
            self.set_numbers(num2)
            if self.get_result() == num2:
                self.click_equal()
                return self.get_result()
