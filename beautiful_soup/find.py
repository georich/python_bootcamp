"""Understanding the find() from bs4."""
from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div>bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
print(soup)
print(type(soup))
# print(soup.body.div)  # Gives first div found
print(soup.find("div"))
d = soup.find("div")
print(type(d))
d2 = soup.find_all("div")

find_by_id = soup.find(id="first")
find_all_class = soup.find_all(class_="special")
find_all_by_attribute = soup.find_all(atts={"data-example": "yes"})
