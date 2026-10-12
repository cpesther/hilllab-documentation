# hilllab.indexer.parsers

Extract text from local document formats for indexing; these are not assay-data loaders.

## Functions

| Function | Purpose | Status |
| --- | --- | --- |
| [`parse_csv`](parse_csv.md) | Returns every nonblank UTF-8 CSV cell as strings using csv.reader's default dialect, including header cells and numeric-looking text. | documentation in progress |
| [`parse_excel`](parse_excel.md) | Returns nonblank string cell values from pandas' default first worksheet, excluding numeric cells and header names. | documentation in progress |
| [`parse_html`](parse_html.md) | Reads UTF-8 HTML with BeautifulSoup and returns stripped, nonempty extracted text lines; errors return None. | documentation in progress |
| [`parse_json`](parse_json.md) | Returns nonblank string values from recursively traversed UTF-8 JSON dictionaries/lists; dictionary keys and numeric values are ignored. | documentation in progress |
| [`parse_pdf`](parse_pdf.md) | Returns stripped nonempty lines extracted from PDF pages by PyPDF2; errors return None. | documentation in progress |
| [`parse_powerpoint`](parse_powerpoint.md) | Returns nonempty text from PowerPoint shapes exposing a text attribute; errors return None. | documentation in progress |
| [`parse_txt`](parse_txt.md) | Returns stripped nonempty lines from a UTF-8 text file. | documentation in progress |
| [`parse_word`](parse_word.md) | Returns words split on literal spaces from nonempty document paragraphs; errors return None. | documentation in progress |
| [`parse_yaml`](parse_yaml.md) | Loads UTF-8 YAML with safe_load and returns recursively encountered nonblank string values. | documentation in progress |

## Methods and callbacks

| Function | Purpose | Status |
| --- | --- | --- |
| [`parse_json.extract_strings`](parse_json.extract_strings.md) | Closure-local recursive visitor appending string values to the parent words list. | documentation in progress |
| [`parse_yaml.extract_strings`](parse_yaml.extract_strings.md) | Closure-local recursive YAML visitor appending string values into the parent words list. | documentation in progress |

## Data and supporting resources

(resource-stopwords-txt)=

### stopwords.txt

Stopword list consumed by indexer.scanner after text extraction. Words are removed by lowercase exact membership after character cleaning.

[View resource source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/indexer/parsers/stopwords.txt).

```{toctree}
:hidden:
:maxdepth: 1

parse_csv <parse_csv>
parse_excel <parse_excel>
parse_html <parse_html>
parse_json <parse_json>
parse_json.extract_strings <parse_json.extract_strings>
parse_pdf <parse_pdf>
parse_powerpoint <parse_powerpoint>
parse_txt <parse_txt>
parse_word <parse_word>
parse_yaml <parse_yaml>
parse_yaml.extract_strings <parse_yaml.extract_strings>
```
