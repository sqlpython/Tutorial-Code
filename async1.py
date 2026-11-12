import asyncio
import time

def async_timer(func):
    """An asynchronous decorator to measure execution time."""
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        # Await the result of the original async function
        result = await func(*args, **kwargs)
        end_time = time.time()
        print(f"'{func.__name__}' ran in {end_time - start_time:.2f} seconds")
        return result
    return wrapper

@async_timer
async def async_example(seconds):
    """An example asynchronous function."""
    print(f"Starting async sleep for {seconds} seconds 😴")
    await asyncio.sleep(seconds)
    print(f"Finished async sleep for {seconds} seconds ⏰")
    return f"Slept for {seconds}s"

# To run the decorated async function
if __name__ == "__main__":
    asyncio.run(async_example(2))
#Key Components
async def wrapper(*args, **kwargs): The inner wrapper function must be defined as a coroutine using async def so it can use await and be awaited itself.
await func(*args, **kwargs): This line is where the decorator yields control back to the event loop and waits for the original function (func) to complete, allowing other tasks to run concurrently.
return wrapper: The decorator returns the wrapper coroutine function, which replaces the original function. 
Patreon
Patreon
 +2
Decorators for Both Sync and Async Functions 
For decorators that need to work with both synchronous and asynchronous functions (often called "async-agnostic" decorators), you can use the inspect module to check the function type or, more commonly, a helper library. 
Patreon
Patreon
python
import inspect

def unified_decorator(func):
    if inspect.iscoroutinefunction(func):
        async def wrapper(*args, **kwargs):
            print("Async wrapper: before call")
            result = await func(*args, **kwargs)
            print("Async wrapper: after call")
            return result
        return wrapper
    else:
        def wrapper(*args, **kwargs):
            print("Sync wrapper: before call")
            result = func(*args, **kwargs)
            print("Sync wrapper: after call")
            return result
        return wrapper

# Example usage with an async function
@unified_decorator
async def my_async_func():
    await asyncio.sleep(1)

# Example usage with a sync function
@unified_decorator
def my_sync_func():
    time.sleep(1)