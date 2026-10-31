
"""Apartment society maintenance dues ledger."""

import ast
import operator
import sqlite3

CONNECTION = sqlite3.connect(":memory:")

CONNECTION.execute(
    """
    CREATE TABLE IF NOT EXISTS dues (
        flat TEXT,
        month TEXT,
        amount INTEGER,
        paid INTEGER
    )
    """
)


def add_due(flat, month, amount, history=None):
    """Add a maintenance due record and update its history."""
    if history is None:
        history = []

    CONNECTION.execute(
        "INSERT INTO dues VALUES (?, ?, ?, ?)",
        (flat, month, amount, 0),
    )
    history.append((flat, month))
    return history


def collect(flat, month):
    """Mark a flat's monthly dues as paid and return its amount."""
    row = CONNECTION.execute(
        "SELECT amount FROM dues WHERE flat = ? AND month = ?",
        (flat, month),
    ).fetchone()

    if row:
        CONNECTION.execute(
            "UPDATE dues SET paid = 1 WHERE flat = ? AND month = ?",
            (flat, month),
        )
        return row[0]

    return None


def evaluate_expression(node):
    """Safely evaluate basic arithmetic expressions using an AST."""
    operations = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.FloorDiv: operator.floordiv,
        ast.Mod: operator.mod,
    }

    if isinstance(node, ast.Expression):
        return evaluate_expression(node.body)

    if isinstance(node, ast.Constant):
        if type(node.value) in (int, float):
            return node.value
        raise ValueError("Only numeric values are allowed")

    if isinstance(node, ast.BinOp):
        operation = operations.get(type(node.op))
        if operation is None:
            raise ValueError("Unsupported arithmetic operation")

        left = evaluate_expression(node.left)
        right = evaluate_expression(node.right)
        return operation(left, right)

    if isinstance(node, ast.UnaryOp):
        if isinstance(node.op, ast.UAdd):
            return evaluate_expression(node.operand)
        if isinstance(node.op, ast.USub):
            return -evaluate_expression(node.operand)

    raise ValueError("Invalid arithmetic expression")


def penalty(rule):
    """Calculate a penalty from a safe arithmetic expression."""
    try:
        expression = ast.parse(rule, mode="eval")
        late_fee = evaluate_expression(expression)
    except (ValueError, SyntaxError, TypeError, ZeroDivisionError):
        late_fee = 0

    return late_fee


def pending():
    """Return the flat numbers with unpaid maintenance dues."""
    rows = CONNECTION.execute(
        "SELECT flat FROM dues WHERE paid = 0"
    ).fetchall()

    return [row[0] for row in rows]


def main():
    """Run a demonstration of the society dues ledger."""
    add_due("A-101", "Oct", 2500)
    add_due("A-102", "Oct", 2500)

    print(collect("A-101", "Oct"))
    print(penalty("50 * 2"))
    print(pending())


if __name__ == "__main__":
    main()
