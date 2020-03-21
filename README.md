## xmlTextModifier
### Transforms xml data to gibberish/random data
This project was written to test for mdml (mx related xml format) marketdata randomisation.
This allows randomised import of data for import testing.
However, I decided to generalise it so that it can be applied to other situations.

### methodology
This code reads the first 20 lines for xml namespace, removes pre-existing ET namespace, and uses dictionary to create a new listing.

### technologies used
python 2.5

### how to use
chmod 744 xmlTextModifier.py
./xmlTextModifier.py <xml> <first node> <second node>
example:
./xmlTextModifier.py sample.xml nd:billToZipCode nd:shipToZipCode

### limitations
Cannot use later versions of python ==> cannot pip install packages/cannot venv
(only can use pre-installed packages)
Assumes namespace is stated in the first 20 lines of the code. This might not be true if namespace is declared further down.

### problems faced
1. cannot use/install package ==> cannot use lxml or other xml packages thats makes life easier
2. namespace issue for xml etree is complicated; if namespace is not renamed, all the naming conventions for namespace will be renamed to ns0,ns1
3. elementree does not return the name for the namespace ( only returns ns0,ns1...)
