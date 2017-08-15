#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
import random
# @asyncio.coroutine
async def wget(host):
    print('Wget: %s' % host)
    connect = asyncio.open_connection(host,80)
    reader, writer = await connect
    header = 'GET / HTTP/1.0\r\nHost:%s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        # await asyncio.sleep(random.random()) #随机阻塞0-1s
        await asyncio.sleep(0.1)
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()
loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.163.com', 'www.sohu.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()