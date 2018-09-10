from cs50 import SQL
from flask import redirect, render_template, url_for, request

db = SQL("sqlite:///tripplanner.db")


# For errors found throughout the doc regarding numbers (cash).
def error(amount):
    # Return error with custom message if negative number
    if amount < 0:
        positive = "Please enter a valid amount value. Only positive values."
        return render_template("error.html", errortype=positive)
    # Return error with custom message if zero
    elif amount == 0:
        zero = "Please enter some positive value."
        return render_template("error.html", errortype=zero)
    # Return error with custom message if expense is greater than current cash
    else:
        notenough = "Not enough money! Please enter more on allowance."
        return render_template("error.html", errortype=notenough)