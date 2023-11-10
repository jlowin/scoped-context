from scoped_context.core import scoped_context

import asyncio

async def my_async_func():
    print(scoped_context.get('x'))  # Output will vary based on context
    async with scoped_context(x=2):
        print(scoped_context.get('x'))  # Will print 2

def my_sync_func():
    print(scoped_context.get('x'))  # Output will vary based on context
    with scoped_context(x=3):
        print(scoped_context.get('x'))  # Will print 3

# Async call
async def main_async():
    print(scoped_context.get('x'))  # None
    async with scoped_context(x=10):
        await my_async_func()  # first print is 10, second should be 2

# Sync call
def main_sync():
    print(scoped_context.get('x'))  # None
    with scoped_context(x=20):
        my_sync_func()  # first print is 20, second should be 3

# Running the main coroutine
asyncio.run(main_async())

# Running the sync main function
main_sync()