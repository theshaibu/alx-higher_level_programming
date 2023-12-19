#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        # Try to execute the function with the provided arguments
        result = fct(*args)
        return result
    except Exception as e:
        # Handle the exception and print the error to stderr
        print(f"Exception: {e}", file=sys.stderr)
        return None
