from pywinauto import Application


class BasePage:
    PLUS_BUTTON = "Add"
    MINUS_BTN = "Subtract"
    EQUAL_BUTTON = "Equals"
    RESULT = "Result"

    def __init__(self, app: Application):
        self.app = app
        self.window_app = app["Calculator"]
        self.window_app.wait("ready", timeout=5)

    # Method entering a number from a button
    def click_number(self, number: int):
        self.window_app.child_window(title=str(number)).set_focus().click()

    # Method pressing the addition button
    def click_plus(self):
        self.window_app.child_window(title=self.PLUS_BUTTON).click_input()

    # Method pressing the subtraction button
    def click_minus(self):
        self.window_app.child_window(title=self.MINUS_BTN).click_input()

    # Method pressing the equals button
    def click_equal(self):
        self.window_app.child_window(title=self.EQUAL_BUTTON).click_input()

    # Method displaying the result from the scoreboard
    def get_result(self) -> int:
        result = self.window_app.child_window(title=self.RESULT).legacy_properties()["Value"]
        return int(result)

    # Method intended for entering numbers from the keyboard
    def set_numbers(self, number: int):
        self.window_app.child_window(title=self.RESULT).type_keys(number)
