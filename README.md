### Haren Chowdary Doppalapudi | hd337

# Advanced Calculator App

## Video Presentation Link
https://drive.google.com/file/d/1yjmvIsOwcV9w_6AY8lpv9b_7Arm4TPYl/view?usp=drive_link

## Summary

Advanced Calculator App is a robust Python program for carrying out many mathematical calculations . It includes statistical analysis, fundamental math, and dynamically loaded plugins that expand capabilities. The calculator app's setup, use, and development information are described in this README file.

## Features

1. **Arithmetic Operations**: Accommodates division, multiplication, subtraction, and addition.
2. **Statistical Operations**: Determine the standard deviation, mean, and median.
3. **Environment Variables**: Use environment variables to modify behavior.
4. **Plugin System**: Use plugins to implement new operations to extend functionality.
5. **History Management**: Maintains track of previous computations and provides views, saves, clears, and deletes options.

Architectural Structure
-----------------------

### Modular Design

TThe calculator application prioritizes modularity, aiming to simplify extension and upkeep. Each mathematical operation resides within its own strategy class, following the Strategy Design Pattern. This approach facilitates the addition of new operations without altering existing code, in line with the Open/Closed Principle.

### Strategy Design Pattern

Operations such as addition, subtraction, multiplication, and division adhere to the Strategy pattern. This allows for runtime selection of the calculator's behavior, enabling the addition of new strategies for operations without necessitating changes to client code.

### Use of Environment Variables

Configuration via environment variables facilitates easy adaptation to various environments without code alterations. It supports configurations like logging levels and history feature toggling, enhancing the app's flexibility and ease of configuration.

### Plugin System for Extensibility

A plugin system enables the dynamic loading of additional operations, expanding the calculator's functionality. Leveraging Python's dynamic import capabilities, new plugins can seamlessly integrate into the application by being added to the plugins directory.

### Logging

A comprehensive logging system, configurable via environment variables, captures operational data, errors, and informational messages. This facilitates debugging and monitoring, swiftly identifying and addressing any issues that arise.


### Facade Pattern for History Management

The HistoryManager class acts as a facade, streamlining history management complexities including viewing, saving, clearing, and deleting calculation histories. It abstracts file handling and DataFrame operations, simplifying the application's core functionality.

### Error Handling and Validation

Robust error handling and input validation ensure the application's reliability and user-friendliness. Decorators wrap operation execution, providing a standardized approach to handling exceptions and validating input across different operations.

### Testing and Code Quality

Unit Testing: Pytest is utilized for comprehensive unit testing, ensuring each component behaves as expected, covering a range of scenarios for each operation, including edge cases.
Static Code Analysis: Pylint enforces code quality and adherence to PEP 8 standards, enhancing maintainability and code readability.

### Continuous Integration

GitHub Actions automates testing and linting with each push or pull request to the main branch, ensuring code quality and functional integrity throughout the development lifecycle..
## Instructions for Installation and build


### Installation

1. Use `git clone <repository_url>} to clone the project to your local machine, and then open the project directory.

2. Establish a virtual setting for the dependencies of the project:

  `source ./venv/bin/activate} after `python3 -m venv env}

3. Install required Python packages with `pip install -r requirements.txt`.

4. In the project root, create a `.env` file to define configurations like `LOG_LEVEL} and `HISTORY_SAVE_PATH}.

## Usage

Run the calculator application in the command line:

```bash
python main.py
```

## Operations list

- **Basic Arithmetic**: `add`, `subtract`, `multiply`, `divide`
- **Statistical Calculations**: `mean`, `median`, `stddev`
- **History Commands**: `view history`, `clear history`, `delete history`

## Logging
All operations performed in the app create a log in the `operations.log` in the `logs` directory.

## History Management

The `HistoryManager` class offers features for organizing and managing calculation history, which is kept in the `data` folder's `history.csv` file. Verify that the application can create the file and directory or that they already exist.

## Environment Variables

Configure the application behavior using the following environment variables in your `.env` file:

- `LOG_LEVEL`: Sets the logging level (e.g., `INFO`, `DEBUG`).
- `HISTORY_SAVE_PATH`: Specifies the path for saving the history file.
- `ENABLE_HISTORY_FEATURE`: Enables or disables history management (`True` or `False`).



