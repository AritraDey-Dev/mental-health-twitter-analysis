# LocationTagger

**This is for Task 3 of Human-AI GSoC: Crisis Geolocation & Mapping (Basic Geospatial Analysis & Visualization).**

LocationTagger is a Python package designed to detect and extract location entities—such as countries, regions/states, and cities—from text or URLs. It also identifies relationships among these geographical entities.

---

## About the Project
In the realm of [Natural Language Processing (NLP)](https://en.wikipedia.org/wiki/Natural_language_processing), Named Entity Recognition ([NER](https://en.wikipedia.org/wiki/Named-entity_recognition)) is a crucial task that identifies entities like names of people, organizations, products, and places within text. However, standard NER tools may not always accurately distinguish location names from other entities.  
LocationTagger addresses this challenge by specifically focusing on extracting and tagging place names from text data.

### Approach  
![Approach](https://github.com/AritraDey-Dev/Task-3-locationtagger/blob/main/locationtagger/data/diagram.jpg?raw=true)

---

## Installation and Setup
**Environment:** Python 3.5 or higher

Install the package using pip:

```bash
pip install locationtagger
```

Before installing LocationTagger, ensure that the following libraries are installed:

- `nltk`
- `spacy`
- `newspaper3k`
- `pycountry`

Additionally, download essential NLTK and spaCy modules using the commands in `/locationtagger/bin/locationtagger-nltk-spacy` on an IPython shell or Jupyter Notebook.

---

## Usage

### Text as Input

```python
import locationtagger

text = "Unlike India and Japan, A winter weather advisory remains in effect through 5 PM along and east of a line from Blue Earth, to Red Wing line in Minnesota and continuing to along an Ellsworth, to Menomonie, and Chippewa Falls line in Wisconsin."

entities = locationtagger.find_locations(text=text)
```

Extracted locations:

```python
entities.countries
```
Output:
```
['India', 'Japan']
```

```python
entities.regions
```
Output:
```
['Minnesota', 'Wisconsin']
```

```python
entities.cities
```
Output:
```
['Ellsworth', 'Red Wing', 'Blue Earth', 'Chippewa Falls', 'Menomonie']
```

Find the countries associated with extracted cities and regions:

```python
entities.country_regions
```
Output:
```
{'United States': ['Minnesota', 'Wisconsin']}
```

```python
entities.country_cities
```
Output:
```
{'United States': ['Ellsworth', 'Red Wing', 'Blue Earth', 'Chippewa Falls', 'Menomonie']}
```

Since "United States" is a country but was not explicitly mentioned in the text, it was inferred from the regions and cities present in the text:

```python
entities.other_countries
```
Output:
```
['United States']
```

To determine which regions these cities may belong to:

```python
entities.region_cities
```
Output:
```
{
  'Maine': ['Ellsworth'],
  'Minnesota': ['Red Wing', 'Blue Earth'],
  'Wisconsin': ['Ellsworth', 'Chippewa Falls', 'Menomonie'],
  'Pennsylvania': ['Ellsworth'],
  'Michigan': ['Ellsworth'],
  'Illinois': ['Ellsworth'],
  'Kansas': ['Ellsworth'],
  'Iowa': ['Ellsworth']
}
```

Regions that were inferred but not explicitly mentioned in the text:

```python
entities.other_regions
```
Output:
```
['Maine', 'Minnesota', 'Wisconsin', 'Pennsylvania', 'Michigan', 'Illinois', 'Kansas', 'Iowa']
```

Words that were identified as named entities by `nltk` and `spacy` but were not categorized as locations:

```python
entities.other
```
Output:
```
['winter', 'PM', 'Chippewa']
```

---

### URL as Input  

LocationTagger can also extract places from URLs:

```python
URL = 'https://edition.cnn.com/2020/01/14/americas/staggering-number-of-human-rights-defenders-killed-in-colombia-the-un-says/index.html'
entities2 = locationtagger.find_locations(url=URL)
```

Extracted locations:

```python
entities2.countries
```
Output:
```
['Switzerland', 'Colombia']
```

```python
entities2.regions
```
Output:
```
['Geneva']
```

```python
entities2.cities
```
Output:
```
['Geneva', 'Colombia']
```

To determine how many times each place is mentioned in the URL content:

```python
entities2.country_mentions
```
Example output:
```
[('Colombia', 3), ('Switzerland', 1)]
```

---

