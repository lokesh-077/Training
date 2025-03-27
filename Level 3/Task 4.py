#Decorator Timer
import time

def timer_decorator(func):
    def wrapper():
        start_time = time.time()
        func()  # Run the function
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time:.2f} seconds")
    return wrapper

@timer_decorator
def sample_function():
    time.sleep(1)  

sample_function()

