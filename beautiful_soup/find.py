"""Understanding the find() from bs4."""
from bs4 import BeautifulSoup

HTML = """
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

SOUP = BeautifulSoup(HTML, "html.parser")
print(SOUP)
print(type(SOUP))
# print(SOUP.body.div)  # Gives first div found
print(SOUP.find("div"))
D = SOUP.find("div")
print(type(D))
D2 = SOUP.find_all("div")

FIND_BY_ID = SOUP.find(id="first")
FIND_ALL_CLASS = SOUP.find_all(class_="special")
FIND_ALL_BY_ATTRIBUTE = SOUP.find_all(atts={"data-example": "yes"})

SELECT = SOUP.select("#first")[0]  # Gives a list back

EL = SOUP.select(".special")[0]
print(EL.get_text())
print(EL.name)
