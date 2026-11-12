# Personal Expense Tracker

A simple command-line Python program for entering expenses and viewing a total summary.

## Features

- Enter multiple expense amounts
- Rejects non-numeric and non-positive amounts
- Displays each expense and the running total
- Shows the transaction count and total expenses when finished
- Keeps expense data in memory for the current run only

## Requirements

- Python 3

## Run the program

From the repository folder, run:

```bash
python expense_tracker.py
```

If your system uses the `python3` command instead:

```bash
python3 expense_tracker.py
```

## Usage

Enter a positive amount at the prompt to record an expense. Type `quit` when you are done to see the expense list and summary.

```text
Enter Expense : 12.50
Enter Expense : 8
Enter Expense : quit
```

## Notes

- Expenses are not saved after the program exits.
- Amounts are displayed with a `$` symbol.
