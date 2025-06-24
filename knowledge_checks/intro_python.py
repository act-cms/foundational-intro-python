python_intro_questions = [
    {
        "question": "When was the Python programming language first introduced?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "1985", "correct": False, "feedback": "Not quite - Python came a bit later."},
            {"answer": "1991", "correct": True, "feedback": "Correct! Python was first introduced in 1991."},
            {"answer": "1995", "correct": False, "feedback": "Close, but Python was introduced a few years earlier."},
            {"answer": "2000", "correct": False, "feedback": "Python is older than that."}
        ]
    },
    {
        "question": "What does it mean that Python is 'free and open-source'?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "Anyone can download, install, and use Python and it does not cost money", "correct": True, "feedback": "Correct! The paragraph explains that free and open-source means 'anyone can download, install, and use Python.'"},
            {"answer": "Python programs run faster than other languages", "correct": False, "feedback": "No, free and open-source refers to cost and accessibility, not speed."},
            {"answer": "Python is only available to students", "correct": False, "feedback": "No, the opposite - it's available to anyone, not just students."},
            {"answer": "You need a license to use Python", "correct": False, "feedback": "No, free and open-source means you don't need to pay for a license."}
        ]
    }
]


variables_quiz = [
    {
        "question": "What is the correct syntax for assigning a variable in Python?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "variable_name == variable_value", "correct": False, "feedback": "No, == is used for comparison, not assignment."},
            {"answer": "variable_name = variable_value", "correct": True, "feedback": "Correct! The equals sign (=) is used to assign values to variables."},
            {"answer": "variable_value = variable_name", "correct": False, "feedback": "This is backwards - the variable name goes on the left, the value on the right."},
            {"answer": "assign variable_name variable_value", "correct": False, "feedback": "Python doesn't use an 'assign' keyword."}
        ]
    },
    {
        "question": "Which of the following are valid variable names in Python? (Select all that apply)",
        "type": "many_choice",
        "answers": [
            {"answer": "temperature", "correct": True, "feedback": "Correct! This starts with a letter and contains only letters."},
            {"answer": "temp_2", "correct": True, "feedback": "Correct! This starts with a letter and contains letters, numbers, and underscores."},
            {"answer": "2temp", "correct": False, "feedback": "Invalid! Variable names cannot start with a number."},
            {"answer": "_my_var", "correct": True, "feedback": "Correct! Variable names can start with an underscore."},
            {"answer": "my-variable", "correct": False, "feedback": "Invalid! Hyphens are not allowed in variable names, only underscores."}
        ]
    },
    {
        "question": "What does assigning a variable allow you to do?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "Save calculated values for later use", "correct": True, "feedback": "Correct! The text explains that variable assignment lets us 'save our calculated values for later use.'"},
            {"answer": "Make calculations run faster", "correct": False, "feedback": "No, assignment is about storing values, not speed."},
            {"answer": "Print results to the screen", "correct": False, "feedback": "No, assignment stores values but doesn't display them."},
            {"answer": "Delete old calculations", "correct": False, "feedback": "No, assignment is about saving values, not deleting them."}
        ]
    }
]

functions_quiz = [
    {
        "question": "What are functions in Python?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "Variables that store numbers", "correct": False, "feedback": "No, that describes variables, not functions."},
            {"answer": "Reusable pieces of code that perform certain tasks", "correct": True, "feedback": "Correct! The text defines functions as 'reusable pieces of code that perform certain tasks.'"},
            {"answer": "A way to write comments in code", "correct": False, "feedback": "No, comments are written with # symbols."},
            {"answer": "Special symbols used in calculations", "correct": False, "feedback": "No, functions are code, not symbols."}
        ]
    },
    {
        "question": "What is the correct syntax for calling a function with arguments?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "function_name[argument1, argument2]", "correct": False, "feedback": "No, functions use parentheses, not square brackets."},
            {"answer": "function_name(argument1, argument2)", "correct": True, "feedback": "Correct! Functions use parentheses containing arguments separated by commas."},
            {"answer": "function_name argument1 argument2", "correct": False, "feedback": "No, arguments must be enclosed in parentheses."},
            {"answer": "call function_name(argument1, argument2)", "correct": False, "feedback": "No, Python doesn't use a 'call' keyword."}
        ]
    },
    {
        "question": "According to the text, what happens when you just call a function or perform a calculation with a variable?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "The result automatically overwrites the original variable", "correct": False, "feedback": "No, the text emphasizes that this does NOT happen automatically."},
            {"answer": "The result is automatically saved for later use", "correct": False, "feedback": "No, results are not automatically saved."},
            {"answer": "The result is not saved unless you assign it to a variable", "correct": True, "feedback": "Correct! The text explains that 'just calling a function or performing a calculation with a variable does not save the result.'"},
            {"answer": "Python gives you an error", "correct": False, "feedback": "No, calling functions doesn't cause errors, but the result won't be saved."}
        ]
    }
]

for_loops_quiz = [
    {
        "question": "What is the correct syntax for a for loop in Python?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "for variable in list\n    do things", "correct": False, "feedback": "Missing the colon (:) after the list name. Python requires a colon at the end of the for statement."},
            {"answer": "for variable in list:\ndo things", "correct": False, "feedback": "Missing indentation. The code inside the loop must be indented."},
            {"answer": "for variable in list:\n    do things", "correct": True, "feedback": "Correct! A for loop needs a colon after the list name and the code inside must be indented."},
            {"answer": "loop variable in list:\n    do things", "correct": False, "feedback": "Missing the 'for' keyword. Python for loops must start with 'for'."}
        ]
    },
    {
        "question": "What does the append method do?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "Removes the last item from a list", "correct": False, "feedback": "No, append adds items. You're thinking of a different method."},
            {"answer": "Adds a new item to the end of an existing list", "correct": True, "feedback": "Correct! The append method adds a new item to the end of an existing list."},
            {"answer": "Sorts the items in a list", "correct": False, "feedback": "No, append doesn't sort anything, it just adds items."},
            {"answer": "Counts the number of items in a list", "correct": False, "feedback": "No, that would be the len() function, not append."}
        ]
    },
    {
        "question": "Why did this code produce an error?\n\n```python\nfor number in energy_kcal:\n    kJ = number * 4.184\n    energy_kJ.append(kJ)\n```",
        "type": "multiple_choice",
        "answers": [
            {"answer": "The calculation is wrong", "correct": False, "feedback": "No, the calculation is correct. The error is about the list."},
            {"answer": "Missing indentation", "correct": False, "feedback": "No, the indentation looks correct in this example."},
            {"answer": "The list energy_kJ doesn't exist yet", "correct": True, "feedback": "Correct! You can't append to a list that doesn't exist. The list energy_kJ needs to be created (even as an empty list) before the loop."},
            {"answer": "Missing colon after the for statement", "correct": False, "feedback": "No, there is a colon in the for statement."}
        ]
    },
    {
        "question": "How do you create an empty list in Python?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "empty_list = ()", "correct": False, "feedback": "No, parentheses create an empty tuple, not a list."},
            {"answer": "empty_list = []", "correct": True, "feedback": "Correct! Square brackets with nothing inside create an empty list."},
            {"answer": "empty_list = {}", "correct": False, "feedback": "No, curly braces create an empty dictionary, not a list."},
            {"answer": "empty_list = null", "correct": False, "feedback": "No, 'null' isn't valid Python syntax. You might be thinking of 'None', but that's not an empty list."}
        ]
    }
]

lists_conditionals_quiz = [
    {
        "question": "What is the correct syntax for a basic if statement in Python?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "if condition { code }", "correct": False, "feedback": "No, Python doesn't use curly brackets for code blocks."},
            {"answer": "if condition: code", "correct": False, "feedback": "Close, but the code should be on the next line and indented."},
            {"answer": "if condition:\n    code", "correct": True, "feedback": "Correct! Python uses a colon and indentation to define code blocks."},
            {"answer": "if (condition) then code", "correct": False, "feedback": "No, Python doesn't use 'then' keyword."}
        ]
    },
    {
        "question": "Given the list `temps = [15, -5, 22, 0, 18]`, what does `temps[1]` return?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "15", "correct": False, "feedback": "No, that's temps[0]. Remember Python uses zero-based indexing."},
            {"answer": "-5", "correct": True, "feedback": "Correct! temps[1] returns the second element, which is -5."},
            {"answer": "22", "correct": False, "feedback": "No, that would be temps[2]."},
            {"answer": "5", "correct": False, "feedback": "No, the element at index 1 is -5, not 5."}
        ]
    },
    {
        "question": "What would this code print?\n\n```python\nvalues = [10, 25, 8, 30]\nif values[2] < 15:\n    print(\"Small number\")\n```",
        "type": "multiple_choice",
        "answers": [
            {"answer": "Nothing - no output", "correct": False, "feedback": "Actually, values[2] is 8, which is less than 15, so the condition is True."},
            {"answer": "Small number", "correct": True, "feedback": "Correct! values[2] is 8, which is less than 15, so the condition is True and 'Small number' is printed."},
            {"answer": "10", "correct": False, "feedback": "No, this code doesn't print the value itself, it prints text based on a condition."},
            {"answer": "Error", "correct": False, "feedback": "No, this code runs without errors."}
        ]
    },
    {
        "question": "Which of the following correctly checks if the first element of a list called `data` is greater than 100?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "if data[1] > 100:", "correct": False, "feedback": "No, data[1] is the second element. The first element is data[0]."},
            {"answer": "if data[0] > 100:", "correct": True, "feedback": "Correct! data[0] accesses the first element since Python uses zero-based indexing."},
            {"answer": "if data.first() > 100:", "correct": False, "feedback": "No, lists don't have a first() method in Python."},
            {"answer": "if first(data) > 100:", "correct": False, "feedback": "No, there's no built-in first() function in Python."}
        ]
    }
]

predict_output_quiz = [
    {
        "question": "What does the following code print?\n\n```python\nenergy_kcal = [-13.4, -2.7, 5.4, 42.1]\nslice1 = energy_kcal[1:]\nslice2 = energy_kcal[:3]\nprint('slice1 is', slice1)\nprint('slice2 is', slice2)\n```",
        "type": "multiple_choice",
        "answers": [
            {"answer": "slice1 is [-2.7, 5.4, 42.1]\nslice2 is [-13.4, -2.7, 5.4]", "correct": True, "feedback": "Correct! slice1 = energy_kcal[1:] takes from index 1 to the end. slice2 = energy_kcal[:3] takes from the beginning up to (but not including) index 3."},
            {"answer": "slice1 is [-13.4, -2.7, 5.4]\nslice2 is [-2.7, 5.4, 42.1]", "correct": False, "feedback": "Not quite. Remember that [1:] starts at index 1 and goes to the end, while [:3] starts at the beginning and goes up to (but not including) index 3."},
            {"answer": "slice1 is [5.4, 42.1]\nslice2 is [-13.4, -2.7]", "correct": False, "feedback": "No, [1:] means from index 1 to the end (not from index 2), and [:3] means up to but not including index 3 (so it includes 3 elements, not 2)."},
            {"answer": "slice1 is [-2.7, 5.4]\nslice2 is [-13.4, -2.7, 5.4, 42.1]", "correct": False, "feedback": "Not correct. [1:] goes from index 1 to the end (includes the last element), and [:3] stops before index 3 (doesn't include all elements)."}
        ]
    }
]