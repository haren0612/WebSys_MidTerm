import logging

from App import CalculatorApp


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app = CalculatorApp()
    app.run()
