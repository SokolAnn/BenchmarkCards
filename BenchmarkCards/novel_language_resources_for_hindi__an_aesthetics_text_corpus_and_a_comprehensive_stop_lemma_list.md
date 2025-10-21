# Novel Language Resources for Hindi: An Aesthetics Text Corpus and a Comprehensive Stop Lemma List

## 📊 Benchmark Details

**Name**: Novel Language Resources for Hindi: An Aesthetics Text Corpus and a Comprehensive Stop Lemma List

**Overview**: Two novel Hindi language resources have been created and released for public consumption. The first resource is a corpus consisting of nearly thousand pre-processed fictional and non-fictional texts spanning over hundred years. The second resource is an exhaustive list of stop lemmas created from 12 corpora across multiple domains, consisting of over 13 million words (from which more than 200,000 lemmas were generated) and 11 publicly available stop word lists (from which nearly 400 unique lemmas were generated). The resources are released for public use under the GNU General Public License.

**Data Type**: text (aesthetic texts: novels, short stories, non-fiction) and lexical list (stop lemmas)

**Domains**:
- Natural Language Processing
- Literature/Aesthetics

**Languages**:
- Hindi

**Similar Benchmarks**:
- CFILT Hindi Corpus
- IIT Bombay English-Hindi Parallel Corpus
- The Open Parallel Corpus (OPUS)
- Wikimedia Downloads
- TDIL (Technology Development for Indian Languages) corpora
- NLTK English stop word list

**Resources**:
- [GitHub Repository](https://github.com/gayatrivenugopal/hindi-corpus-stoplemmas)
- [Resource](https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Hindi_1900)
- [Resource](https://1000mostcommonwords.com/1000-most-common-hindi-words)
- [Resource](https://blogs.transparent.com/hindi/first-100-high-frequency-words-in-hindi)
- [Resource](http://home.iitk.ac.in/~prasant/HindiCorpus/word.html)
- [GitHub Repository](https://github.com/oprogramador/most-common-words-by-language)
- [GitHub Repository](https://github.com/Alir3z4/stop-words)
- [GitHub Repository](https://github.com/stopwords-iso/stopwords-hi)
- [Resource](http://dx.doi.org/10.17632/bsr3frvvjc.1)
- [Resource](https://www.ranks.nl/stopwords/hindi)
- [Resource](https://dumps.wikimedia.org/backup-index.html)
- [Resource](http://opus.nlpl.eu/)
- [Resource](https://www.cfilt.iitb.ac.in/Downloads.html)
- [Resource](http://www.tdil-dc.in)

## 🎯 Purpose and Intended Users

**Goal**: To build an unbiased time-independent aesthetics corpus in Hindi and to create and publish an exhaustive stop lemma list based on raw frequencies across multiple corpora.

**Target Audience**:
- Natural Language Processing researchers
- Model developers
- Academic researchers

**Tasks**:
- Language Modeling
- Text Classification
- Information Retrieval

**Limitations**: The list is limited to the texts collected from the specified sources; the corpus size is not comparable to Wiki dumps due to availability of public content; a formal evaluation method for the stop lemma list was suggested as future work.

## 💾 Data

**Source**: Scraped novels, short stories and non-fiction texts from https://hindisamay.com, https://premchand.co.in, http://borilib.com using Scrapy; additional corpora and resources acquired from TDIL (http://www.tdil-dc.in), CFILT (https://www.cfilt.iitb.ac.in/Downloads.html), Open Parallel Corpus (http://opus.nlpl.eu/), Wikimedia Dumps (https://dumps.wikimedia.org/backup-index.html), IIT Bombay resources and other publicly available stop word lists and corpora as listed in the paper.

**Size**: Aesthetics corpus: 978 articles; 145,508 words (corpus LR#12). Combined corpora used for stop lemma generation: over 13 million words (paper states 13+ million words; elsewhere reports 13,811,781 words), Set B comprised 213,554 lemmas, final exhaustive stop lemma list: 311 lemmas. Parts-of-speech analysis covered 10,722,288 unique words and 335,089 lemmas (as reported).

**Format**: N/A

**Annotation**: Automatic preprocessing: sentence splitting and tokenization; removal of special characters, English tokens and Latin numbers. Lemmatization and part-of-speech tagging performed using the StanfordNLP POS processor.

## 🔬 Methodology

**Methods**:
- Web scraping using Scrapy
- Text preprocessing (sentence split, tokenization, cleaning)
- Automatic lemmatization and POS tagging with StanfordNLP
- Frequency analysis of words and lemmas
- Statistical analysis using point biserial correlation coefficient and p-values
- Set operations (union and intersection) to create Set A, Set B and final Set C (exhaustive stop lemma list)
- Comparative assessment via translation and comparison with NLTK English stop word list

**Metrics**:
- Raw frequency counts
- Point biserial correlation coefficient
- P-value

**Calculation**: Raw frequencies of words and lemmas were computed across corpora. Point biserial correlation coefficients were computed between parts of speech (from StanfordNLP) and rank positions in top stop word/lemma lists. Set A was created by lemmatizing and uniting publicly available stop word lists; Set B was the union of top 100 lemmas from corpora; Set C = Set A ∩ Set B produced the final exhaustive stop lemma list.

**Interpretation**: Stop lemmas are more consistent across multiple sources than stop words. There was no significant relationship between part of speech and rank in stop word/lemma lists, leading authors to favor frequency-based selection and lemma-based lists. The final list of 311 lemmas is presented in decreasing order of frequency.

**Baseline Results**: Comparison with English NLTK stop word list: 179 English words produced 74 unique equivalent Hindi lemmas after translation and lemmatization; 73 of these 74 Hindi lemmas were present in the exhaustive Hindi stop lemma list.

**Validation**: Assessment was performed by translating the English NLTK stop word list to Hindi (with manual intervention), lemmatizing, and checking overlap with the exhaustive stop lemma list. The authors note a formal evaluation method is suggested as future work.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: State-wise distribution of authors is skewed (majority associated with Uttar Pradesh). Gender distribution: only 4.84% of publications are authored by females overall; 0% in the pre-independence era for this corpus; metadata of 164 out of 978 articles could not be found.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Released under the GNU General Public License

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
