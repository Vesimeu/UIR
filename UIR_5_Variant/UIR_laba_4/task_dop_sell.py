def generate_custom_matrix(rows, cols):
    custom_matrix = [[0] * cols for _ in range(rows)]
    count = 1
    for i in range(cols - 1, -1, -1):
        if i % 2 == 0:
            for j in range(rows - 1, -1, -1):
                custom_matrix[j][i] = count
                count += 1
        else:
            for j in range(rows):
                custom_matrix[j][i] = count
                count += 1
    return custom_matrix


def create_mirror_bottom_left(original_matrix):
    mirror_bottom_left_array = original_matrix[::-1]
    return mirror_bottom_left_array


def create_mirror_bottom_right(mirror_bottom_left_array):
    mirror_bottom_right_array = [row[::-1] for row in mirror_bottom_left_array]
    return mirror_bottom_right_array


def create_mirror_upper_right(mirror_bottom_right_array):
    mirror_upper_right_array = mirror_bottom_right_array[::-1]
    return mirror_upper_right_array


def build_and_display_matrix(rows, cols):
    custom_matrix = generate_custom_matrix(rows, cols)

    print("Основная матрица:")
    for row in custom_matrix:
        print(' '.join(map(str, row)))

    print("Преобразование - Слева-снизу")
    for row in create_mirror_bottom_left(custom_matrix):
        print(' '.join(map(str, row)))

    print("Преобразование - Справа-снизу")
    for row in create_mirror_bottom_right(create_mirror_bottom_left(custom_matrix)):
        print(' '.join(map(str, row)))

    print("Преобразование - Справа-сверху")
    for row in create_mirror_upper_right(create_mirror_bottom_right(create_mirror_bottom_left(custom_matrix))):
        print(' '.join(map(str, row)))


def main():
    rows = int(input("Введите количество строк матрицы:\n"))
    while rows < 1:
        print("Вы допустили ошибку, повторите ввод")
        rows = int(input())

    cols = int(input("Введите количество столбцов матрицы:\n"))
    while cols < 1:
        print("Вы допустили ошибку, повторите ввод")
        cols = int(input())

    build_and_display_matrix(rows, cols)


if __name__ == "__main__":
    main()
