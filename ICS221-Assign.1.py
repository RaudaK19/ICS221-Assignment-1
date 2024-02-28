import matplotlib.pyplot as plt
import numpy as np
import time

# Chocolate Distribution Algorithm
def distribute_chocolates_iter(chocolates, students):
    return [(student, chocolate) for student, chocolate in zip(students, chocolates)]

def distribute_chocolates_rec(chocolates, students, index=0):
    if index >= len(students) or index >= len(chocolates):
        return []
    else:
        return [(students[index], chocolates[index])] + distribute_chocolates_rec(chocolates, students, index + 1)

# Sorting Algorithms
def sort_by_weight(chocolates):
    return sorted(chocolates, key=lambda x: x[2])

def sort_by_price(chocolates):
    return sorted(chocolates, key=lambda x: x[3])

# Searching Algorithm
def search_chocolate(chocolates, target):
    for chocolate in chocolates:
        if chocolate[2] == target or chocolate[3] == target:
            return chocolate
    return None

# Time Complexity Functions
def linear(n):
    return n

def nlogn(n):
    return n * np.log(n)

def constant(n):
    return np.ones_like(n)

# Define the range of input values
n_values = np.arange(1, 100)

# Sensitivity analysis for each algorithm
execution_times = {'Distribution': [], 'Sorting': [], 'Searching': []}
min_threshold = 0.001  # Set a minimum threshold for execution time

for n in n_values:
    # Chocolate Distribution Algorithm
    chocolates = [(i, "Milk", np.random.randint(10, 100), np.random.uniform(1.0, 5.0)) for i in range(n)]
    students = ["Student" + str(i) for i in range(n)]
    start_time = time.time()
    distribute_chocolates_iter(chocolates, students)
    end_time = time.time()
    exec_time = end_time - start_time
    execution_times['Distribution'].append(max(exec_time, min_threshold))

    # Sorting Algorithm
    start_time = time.time()
    sort_by_weight(chocolates)
    end_time = time.time()
    exec_time = end_time - start_time
    execution_times['Sorting'].append(max(exec_time, min_threshold))

    # Searching Algorithm
    sorted_by_weight = sort_by_weight(chocolates)
    start_time = time.time()
    search_chocolate(sorted_by_weight, 40)
    end_time = time.time()
    exec_time = end_time - start_time
    execution_times['Searching'].append(max(exec_time, min_threshold))

# Plotting the Time Complexities

# Create subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Plotting Chocolate Distribution Algorithm
axs[0, 0].plot(n_values, linear(n_values), label='Chocolate Distribution Algorithm', color='blue')
filtered_execution_times_distribution = [max(t, min_threshold) for t in execution_times['Distribution']]
axs[0, 0].scatter(n_values, filtered_execution_times_distribution, color='blue')
axs[0, 0].set_title('Chocolate Distribution Algorithm')
axs[0, 0].set_xlabel('Input Size (n)')
axs[0, 0].set_ylabel('Time (T)')
axs[0, 0].grid(True)
axs[0, 0].legend()
axs[0, 0].set_ylim(ymin=5)  # Set minimum y-axis limit greater than zero for this subplot

# Plotting Sorting Algorithm
axs[0, 1].plot(n_values, nlogn(n_values), label='Sorting Algorithm', color='green')
filtered_execution_times_sorting = [max(t, min_threshold) for t in execution_times['Sorting']]
axs[0, 1].scatter(n_values, filtered_execution_times_sorting, color='green')
axs[0, 1].set_title('Sorting Algorithm')
axs[0, 1].set_xlabel('Input Size (n)')
axs[0, 1].set_ylabel('Time (T)')
axs[0, 1].grid(True)
axs[0, 1].legend()
axs[0, 1].set_ylim(ymin=5)  # Set minimum y-axis limit greater than zero for this subplot

# Plotting Searching Algorithm
axs[1, 0].plot(n_values, constant(n_values), label='Searching Algorithm', color='red')
filtered_execution_times_searching = [max(t, min_threshold) for t in execution_times['Searching']]
axs[1, 0].scatter(n_values, filtered_execution_times_searching, color='red')
axs[1, 0].set_title('Searching Algorithm')
axs[1, 0].set_xlabel('Input Size (n)')
axs[1, 0].set_ylabel('Time (T)')
axs[1, 0].grid(True)
axs[1, 0].legend()
axs[1, 0].set_ylim(ymin=0.2)  # Set minimum y-axis limit greater than zero for this subplot

# Plotting Combined Graph
axs[1, 1].plot(n_values, linear(n_values), label='Chocolate Distribution Algorithm', color='blue')
axs[1, 1].plot(n_values, nlogn(n_values), label='Sorting Algorithm', color='green')
axs[1, 1].plot(n_values, constant(n_values), label='Searching Algorithm', color='red')
axs[1, 1].set_title('Combined Time Complexity Analysis')
axs[1, 1].set_xlabel('Input Size (n)')
axs[1, 1].set_ylabel('Time (T)')
axs[1, 1].grid(True)
axs[1, 1].legend()

plt.tight_layout()
plt.ylim(ymin=0)  # Set minimum y-axis limit greater than zero
plt.show()