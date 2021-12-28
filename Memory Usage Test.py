import matplotlib.pyplot as plt
import time


def Test():
    start_time = time.time()
    for _ in range(int(2e6)):
        n = 7e10 * 8e12
        n *= n
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time


number_of_tests = int(input("Select the number of test you want to make: "))

times = []

for i in range(number_of_tests):
    times.append(Test())

print(times)
numbers = range(number_of_tests)


plt.plot(numbers, times, label="Time")
plt.title("CPU")
plt.xlabel("Test number")
plt.ylabel("Seconds Taken")
plt.legend()
plt.show()
