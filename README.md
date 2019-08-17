
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/classAndrew/pycrawler">
    <img src="https://i.imgur.com/Bn1dCVU.png" alt="Logo" width=256 height=128>
  </a>
  <h1 align="center">pyCrawler</h3>

  <h3 align="center">
        An asynchronous webcrawler written in Python.
</p>


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
