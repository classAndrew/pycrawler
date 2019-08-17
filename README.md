# pycrawler
> An asynchronous webcrawler written in Python.

## Examples
- Basic Example
```python
import aiohttp
import crawler
depth, calls = 2, 50 # Arbitrary integers
async with aiohttp.ClientSession() as session:
  c = crawler.Crawler("http://starting.link", session):
  links = await c.start(depth, calls)
```
- Write links to a file
```python
import aiohttp
import crawler
depth, calls = 2, 50 # Arbitrary integers
async with aiohttp.ClientSession() as session:
  c = crawler.Crawler("http://starting.link", session):
  c.write_out("neatfile") # This will write out the list of stored links seperated by newlines to the file named "neatfile"
```
