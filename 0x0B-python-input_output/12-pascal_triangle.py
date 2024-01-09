def pascal_triangle(n):
    """Generates Pascal's Triangle up to n rows.

    Args:
        n (int): The number of rows in Pascal's Triangle.

    Returns:
        list of lists: A list of lists of integers representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # First element of each row is always 1

        # Calculate the rest of the row based on the previous row
        if triangle:
            prev_row = triangle[-1]
            row.extend([prev_row[j] + prev_row[j + 1] for j in range(len(prev_row) - 1)])
            row.append(1)  # Last element of each row is always 1

        triangle.append(row)

    return triangle

# Example usage:
# result = pascal_triangle(5)
# print(result)

