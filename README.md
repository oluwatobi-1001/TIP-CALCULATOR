# Tip Calculator

A simple command-line program written in Python as part of a "100 Days of Coding" challenge. It calculates how much each person should pay after splitting a bill and a tip evenly among a group.

## Description

The program asks the user for three things: the total bill amount, the tip percentage they'd like to leave, and the number of people splitting the bill. It then calculates the total bill including tip, divides it evenly across everyone, and prints the amount each person owes, rounded to 2 decimal places.

## How it works

1. Prompts the user to enter the total bill.
2. Prompts the user to enter a tip percentage (as a whole number, e.g. 10, 12, 15).
3. Prompts the user to enter how many people are splitting the bill.
4. Calculates the tip amount and adds it to the bill.
5. Divides the total by the number of people.
6. Formats the result to 2 decimal places and prints how much each person should pay.

## Example

Welcome to the tip calculator!
What was the total bill in #? 200
How much tip will you like to give? 10, 12, 15... 10
How many people will split the bill? 4
Each person should pay: #55.00
## Requirements

- Python 3

## Running the program

python tip.py
## Notes

- The tip should be entered as a whole number (e.g. 10 for 10%), not a decimal or a percentage sign.
- The number of people should be a whole number.
- Entering text instead of numbers will cause an error, since the program expects numeric input.

## Summary

This project is a small, beginner-friendly exercise in taking user input, doing basic arithmetic, and formatting output cleanly in Python.
