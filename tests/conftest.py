import pytest
from pywinauto import Application


@pytest.fixture()
def app():
    app = Application(backend="uia").start(fr"calc.exe", timeout=5)
    app.connect(best_match="Calculator", timeout=5)
    yield app
    app.kill(soft=True)

