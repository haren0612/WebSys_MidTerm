from App import CalculatorApp
from App.utils.logging import setup_logging
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    setup_logging()
    app = CalculatorApp()
    app.run()
