async def yield_test():
    yield 1
    yield 2
    yield 3


async def main():
    await yield_test()

my_yield = yield_test()
# for item in my_yield:
#     print(item)

