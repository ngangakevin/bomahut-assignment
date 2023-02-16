# Write an algorithm that given an M X N  matrix return all numbers that are the maximum value inits row but the minimum in its column
def min_max_numbers(matrix: list):
    """
    Finds all maximum values in row but minimum in their respective columns.

    Parameters
    ----------
    matrix : list
        2D list m * n \n
        ● m == mat.length \n
        ● n == mat[i].length \n
        ● 1 <= n, m <= 50 \n
        ● 1 <= matrix[i][j] <= 105. \n
    
    Returns
    -------
    list
        The list of numbers satisfying criterion: \n \t●All maximum values in row but minimum in their respective columns
    """
    result = []
    for i, j in enumerate(matrix):
        max_value = max(j)
        max_column = j.index(max_value)
        is_min = True
        for k in range(len(matrix)):
            if matrix[k][max_column] < max_value:
                is_min = False
                break
        if is_min:
            result.append(max_value)
    return result

if __name__ == '__main__':
    rows  = int(input("Enter the number of rows: \n"))
    columns = int(input("Enter the number of columns: \n"))

    matrix = []

    for i in range(rows):
        a = []
        for j in range(columns):
            a.append(int(input(f"Pass Matrix value matrix[{i}][{j}]: \t")))
        matrix.append(a)

    print(min_max_numbers(matrix=matrix))

