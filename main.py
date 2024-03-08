import timeit
import random
import matplotlib.pyplot as plt


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def time_calculator(algorithm, input_size):
    setup = f"from __main__ import {algorithm.__name__}"
    stmt = f"{algorithm.__name__}({[random.randint(1, 1000) for _ in range(input_size)]})"
    # Считаем среднюю по 10 полным итерациям 
    execution_time = timeit.timeit(stmt, setup, number=10) / 10
    return execution_time


def plot_complexity(algorithms, max_input_size):
    input_sizes = list(range(1, max_input_size + 1))

    for algorithm in algorithms:
        execution_times = [time_calculator(algorithm, size) for size in input_sizes]
        plt.plot(input_sizes, execution_times, label=algorithm.__name__)

    plt.xlabel('Размер входного массива')
    plt.ylabel('Время выполнения (s)')
    plt.title('Асимптоты алгоритмов')
    plt.legend()
    plt.show()


# Set the maximum input size for the plot
max_input_size = 500

# Plot the complexity for both algorithms
algorithms = [bubble_sort, merge_sort]
plot_complexity(algorithms, max_input_size)
