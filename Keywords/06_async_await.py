# async, await (asynchronously : 비동기로)
# Python의 asyncio library에서 제공한다.
# 동시 코드를 작성하는 데 사용된다.

import asyncio

async def main():
    print("Hello")
    await asyncio.sleep(1)
    print("world")

# asyncio.run(main())
# Hello
# sleep(1)...
# world