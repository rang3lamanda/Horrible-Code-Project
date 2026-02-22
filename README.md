# Horrible-Code-Project

This project is a simple calculator designed to demonstrate good and bad coding practices.
The goal is to compare a version of the program with good coding practices (good_calculator.py) with the
other version of the program with bad coding practices (bad_calculator.py)
to practice writing clean, maintainable code.

## Project Files

- `good_calculator.py` – Implements the good version of the calculator  
- `bad_calculator.py` – Implements the bad version of the calculator




## Principles Demonstrated
----------------------------------------------------------------------------------------------------
1. KISS (keeping it simple)

Good version:
    Each function was implemented to perform one simple task. By following this principle
    this version of the code is easy to follow and it also avoids any unnecessary complex code.

Bad Version:

----------------------------------------------------------------------------------------------------
2. DRY (Don't Repeat Yourself)

Good version:
    Each function that includes mathematical operations is only written once and it is not reused in
    anywhere later in the code.

Bad Version:

----------------------------------------------------------------------------------------------------
3. Single Responsibility Principle

Good version: 
    The mathematical functions only perform the necessary calculations, and errors such as dividing
    by zero are handled appropriately. The main function manages user input and output.
    Implementing this helps to keep the code organized and easy to read.

Bad Version:



