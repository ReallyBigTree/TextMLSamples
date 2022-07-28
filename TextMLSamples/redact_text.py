import spacy

# Load the large English NLP model
nlp = spacy.load('en_core_web_sm')


# Replace a token with "REDACTED" if it is a name
def replace_name_with_placeholder(token):
    if token.ent_iob != 0 and token.ent_type_ == "PERSON":
        return "[REDACTED] "
    else:
        return token.text


# Loop through all the entities in a document and check if they are names -- updated based on  # #https://stackoverflow.com/questions/66725902/attributeerror-spacy-tokens-span-span-object-has-no-attribute-merge

def scrub(text):
	doc = nlp(text)
	with doc.retokenize() as retokenizer:
		for ent in doc.ents:
			retokenizer.merge(ent)
	tokens = map(replace_name_with_placeholder, doc)
	return "".join(tokens)


s = """
In 1950, Alan Turing published his famous article "Computing Machinery and Intelligence". In 1957, Noam Chomsky's 
Syntactic Structures revolutionized Linguistics with universal grammar, a rule based system of syntactic structures.
"""

print(scrub(s))
