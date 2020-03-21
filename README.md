## xmlTextModifier
### Transforms xml data to gibberish/random data
This project was written to test for mdml (mx related xml format) marketdata randomisation.
This allows randomised import of data for import testing.
However, I decided to generalise it so that it can be applied to other situations.

### methodology
This code reads the first 20 lines for xml namespace, removes pre-existing ET namespace, and uses dictionary to create a new listing.

### technologies used
python 2.5

### limitations
Cannot use later versions of python ==> cannot pip install packages/cannot venv
(only can use pre-installed packages)


