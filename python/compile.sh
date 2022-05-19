bibtex2html -d -r --nodoc --nobibsource biblio.bib
cat publications.md biblio.html > ../content/publications.md
