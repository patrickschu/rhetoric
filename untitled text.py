import re
from string import punctuation

cleantext=["...", "I.", "assi", "...assi", "go", "home", "well-desvered", ".", "!"]
print cleantext
endtext=[i.strip(punctuation) for i in cleantext if re.search("\w+", i)]
print endtext