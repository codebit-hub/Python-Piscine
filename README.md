
*This project has been created as part of the 42 curriculum by dporhomo.*

## Description
The **Python Discovery Piscine** is an intensive introductory course designed to build a solid foundation in Python 3. Over nine modules, the project covers the essential building blocks of the language, ranging from basic syntax and data types to functional programming concepts and data manipulation.

The goal was to transition from "knowing of" Python to being able to write functional, clean, and "Pythonic" scripts that handle user input, manipulate strings and arrays, manage system arguments, and process complex data structures like dictionaries.

## Instructions

### Prerequisites
* Python 3.x installed on your system.
* A terminal or command-line interface.

### Execution
Most exercises are standalone scripts. You can run them by navigating to the specific module/exercise folder and using the following command:

```bash
python3 name_of_script.py [arguments]

```

**Examples:**

* **Module 6 (CLI Arguments):** `python3 upcase_it.py "hello"` will output `HELLO`.
* **Module 4 (User Input):** `python3 calculator.py` will prompt for two numbers and display arithmetic results.
* **Module 9 (Dictionaries):** `python3 family_affairs.py` will process a hardcoded dictionary to filter specific values.

## Resources

* [Official Python 3 Documentation](https://docs.python.org/3/)
* [Real Python Tutorials](https://realpython.com/)
* [W3Schools Python Reference](https://www.w3schools.com/python/)

### AI Usage

AI was utilized during this project as a peer-learning tool to:

* Clarify the difference between `list` and `set` comprehensions.
* Debug specific `ValueError` exceptions when handling `sys.argv` inputs.
* Refine logic for complex dictionary filtering and sorting in Module 9.

---

## Scope: Technical Implementation & Core Competencies

### Data Handling & Type Safety

*
**Integer/Float Validation**: Implementing robust error handling using `try/except` blocks to manage `ValueError` during user input and system argument parsing.


*
**Arithmetic Precision**: Utilizing f-string formatting with `:g` for significant figure management in calculator logic.


*
**Type Checking**: Employing `isinstance()` to ensure function arguments meet expected data types (e.g., string validation).



### Control Structures & Logic

*
**Conditional Logic**: Developing branching logic to handle state (e.g., positive, negative, or zero results).


*
**Iterative Logic**: implementing both `while` loops for continuous user interaction and `for` loops for list/argument processing.



### Functional Programming & Data Structures

*
**Dictionary Processing**: Using `.items()`, `.keys()`, and `.values()` to manipulate complex key-value datasets.


*
**Higher-Order Functions**: Implementing `filter()` and `sorted()` with custom lambda-style key functions to process data objects.


*
**List & Set Comprehensions**: Creating efficient, one-line data transformations including conditional filtering within the comprehension.



### System & String Engineering

*
**CLI Argument Parsing**: Utilizing `sys.argv` to create command-line tools that accept external parameters.


*
**String Manipulation**: Applying `.strip()`, `.capitalize()`, `.upper()`, and `.swapcase()` to normalize and process text data.


*
**RegEx Integration**: Implementing the `re` module for pattern matching and search functionality.
