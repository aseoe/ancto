from tornado import httpclient

async def f():
    http_client = httpclient.AsyncHTTPClient()
    try:
        response = await http_client.fetch("http://www.baidu.com/")
    except Exception as e:
        print("Error")
    else:
        print(response.body.decode("utf8"))

if __name__ == "__main__":
    import tornado
    io_loop = tornado.ioloop.IOLoop.current()
    # io_loop.run_sync(f)
    #asyncio 方式获取数据
    import asyncio
    # asyncio.ensure_future(f())
    # asyncio.get_event_loop().run_forever()

    # 另一种方式
    asyncio.get_event_loop().run_until_complete(f())


