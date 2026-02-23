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
    The bad version violates KISS by mixing multiple responsibilites inside functions. For example, the math functions handle input, conversion, calculation, and printing all at once. The overall structure is less organized and more repetitive than necessary.

----------------------------------------------------------------------------------------------------
2. DRY (Don't Repeat Yourself)

Good version:
    Each function that includes mathematical operations is only written once and it is not reused in
    anywhere later in the code.

Bad Version: 
    The bad version repeats similar code across functions. Both math functions seperately collect input and convert it to floats instead of using a shared helper function. Some results are printed more than once unneccessarily. This duplication makes the code harder to maintain

----------------------------------------------------------------------------------------------------
3. Single Responsibility Principle

Good version: 
    The mathematical functions only perform the necessary calculations, and errors such as dividing
    by zero are handled appropriately. The main function manages user input and output.
    Implementing this helps to keep the code organized and easy to read.

Bad Version: 
    Functions in the bad version perform multiple tasks at once. For example, the operation functions gather input, perform calculations, and print results. The 'run_calculator()' function also handles the menu, loop control, and even modifies a global variable. This lack of seperation makes the code less strucutred and harder to maintain.



