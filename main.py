from bs4 import BeautifulSoup
import requests

#url = "https://en.wikiquote.org/wiki/George_Washington"
url = input("Please paste your url here: ")

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

#heading3 = soup.find_all('div', class_="mw-heading3")

#allText = soup.find_all('div', id="mw-content-text")

#allTextList = soup.find_all('ul')
#allListItems = soup.find_all('li')

#boldQuotes = soup.find_all('b')

#onlyText_heading3 = [title.text for title in heading3]
#onlyText_allText = [title.text.strip() for title in allText]
#onlyText_boldQuotes = [title.text for title in boldQuotes]

#cleaned_text = [re.sub(r'\n+', ' ', item) for item in onlyText_allText]

#print(onlyText_boldQuotes)

# This finds all ul tags after the Quotes h2 heading
quotesHeading = soup.find('h2', id='Quotes')
# Very very useful, but not needed anymore.
#findAllQuotesAfterHeading = quotesHeading.find_all_next('ul')

disputedHeading = soup.find('h2', id='Disputed')
# Very very useful, but not needed anymore.
#upUntil_disputed = disputed.find_all_previous('ul')

# The Below Code, when uncommented, gets all of the full texts that the quotes are from. So not just a snippet quote, but the full-blown conversation that the quote is from.
"""

current = quotesHeading
while current and current != disputedHeading:
    current = current.find_next()
    if current and current.name == 'ul':
        print(current.text.strip(), "\n")

"""

# This code gets only the quotes that are in bold(the quote snippets) on the wikiquotes page.
# Empty list
unique_texts = []

# Set current equal to quotesHeading i.e. h2
current = quotesHeading
# While quotesHeading not equal to disputedHeading
# So it begins iterating here and continues until it reaches the disputedHeading tag, then it stops running.
while current and current != disputedHeading:
    
    # The code in the loop looks for the next tag in the document structure.
    # If the tag is a <ul> (unordered list), it looks inside for all <b> (bold) elements.
    # It strips and checks each bold quote and appends it to unique_texts only if it isn't already in the list.
    
    # on head loop find next h2
    current = current.find_next()
    # If the h2 and the h2 name content are equal to the string "ul", run the following code.
    if current and current.name == 'ul':
        # Find all the important bold quotes on the page
        onlyText_boldQuotes = current.find_all('b')
        #onlyText_listItems = current.find_all('li')
        for b in onlyText_boldQuotes:
            # Strip all useless text from boldquote
            boldQuotes = b.text.strip()
    		#print(b.text.strip(), "\n")
            if boldQuotes not in unique_texts:
                unique_texts.append(boldQuotes)
            if boldQuotes not in unique_texts:
                print(True)

print(unique_texts)
with open("quoteList.txt", "w", encoding="utf-8") as output:
    for quote in unique_texts:
        output.write(f'"{quote}",\n')

for quote in unique_texts:
    print(f'"{quote}",\n')