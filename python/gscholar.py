from scholarly import scholarly
from tqdm import tqdm

# Retrieve the author's data, fill-in, and print
# Get an iterator for the author results
search_query = scholarly.search_author('Samothrakis')
# Retrieve the first result from the iterator
first_author_result = next(search_query)
#scholarly.pprint(first_author_result)

# Retrieve all the details for the author
author = scholarly.fill(first_author_result )
#scholarly.pprint(author)

# Take a closer look at the first publication
first_publication = author['publications'][0]
first_publication_filled = scholarly.fill(first_publication)
first_publication_filled["bib"]["ID"] = 10
first_publication_filled["bib"]["ENTRYTYPE"] = "Journal"


with open('biblio.bib', 'w') as f:
    for i,publication in tqdm(enumerate(author["publications"])):
        scholarly.fill(publication)
        publication["bib"]["ID"] = i
        #print(publication["bib"])

        if("journal" in publication["bib"]):
            publication["bib"]["ENTRYTYPE"] = "journal"
        #else:
        elif("conference" in publication["bib"]):
            publication["bib"]["ENTRYTYPE"] = "inproceedings"
        else:
            publication["bib"]["ENTRYTYPE"] = "misc"
        f.write(scholarly.bibtex(publication) + "\n")

# Print the titles of the author's publications
#publication_titles = [(pub['bib']['title'],pub['bib']['journal'] ) for pub in author['publications']]

#print(publication_titles)

# Which papers cited that publication?
#citations = [citation['bib']['title'] for citation in scholarly.citedby(first_publication_filled)]
#print(citations)