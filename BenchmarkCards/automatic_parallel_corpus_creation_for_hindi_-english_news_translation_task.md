# Automatic Parallel Corpus Creation for Hindi -English News Translation Task

## 📊 Benchmark Details

**Name**: Automatic Parallel Corpus Creation for Hindi -English News Translation Task

**Overview**: We have developed an automatic parallel corpus generation system prototype, which creates Hindi-English parallel corpus for news translation task. Further to verify the quality of generated parallel corpus we have experimented by taking various performance metrics (Gestalt pattern matching, Hamming distance, Damerau-Levenshtein distance).

**Data Type**: text (Hindi-English parallel sentence pairs for news)

**Domains**:
- Natural Language Processing
- Machine Translation

**Languages**:
- Hindi
- English

**Similar Benchmarks**:
- Bleualign
- Hunalign
- ABBYY Aligner
- Unitex Aligner

**Resources**:
- [GitHub Repository](https://github.com/rsennrich/Bleualign)
- [Resource](http://mokk.bme.hu/resources/hunalign/)
- [Resource](http://www.abbyy.com/aligner/)
- [Resource](http://www-igm.univ-mlv.fr/~unitex/#)

## 🎯 Purpose and Intended Users

**Goal**: To develop an automatic parallel corpus generation prototype that creates Hindi-English parallel corpus for news translation tasks and to verify the quality of the generated parallel corpus using various performance metrics.

**Tasks**:
- Machine Translation
- Sentence Alignment
- Parallel Corpus Creation

**Limitations**: Current generated corpus size is limited for higher thresholds (e.g., 202 sentence-pairs at 80% threshold in the reported experiment). Authors state they will try to increase the quantity of parallel corpus, mainly for the 80% threshold.

## 💾 Data

**Source**: Crawled Hindi news from Navbharat Times; crawled English news from web pages including Times of India, The Hindu, Quora and other news sources. Translated Hindi content to English using Google Translator API to create a baseline for alignment.

**Size**: For December 2017 experiment: 22,625 Hindi news articles crawled; 226,250 English news articles crawled. Final parallel corpus sentence-pairs: 12,798 sentence-pairs (50% threshold); 3,443 sentence-pairs (60% threshold); 987 sentence-pairs (70% threshold); 202 sentence-pairs (80% threshold).

**Format**: N/A

**Annotation**: Automatically generated: Hindi headlines/content translated to English via Google Translator API; sentence pairs extracted and aligned using fuzzy string matching algorithm and thresholding. No manual annotation described.

## 🔬 Methodology

**Methods**:
- Automated crawling and translation using Google Translator API
- Sentence boundary disambiguation using rule-based system
- Fuzzy string matching algorithm (based on Levenshtein distance) for alignment
- Automated evaluation using string similarity metrics (Gestalt Pattern Matching, Hamming Distance, Damerau-Levenshtein Distance)

**Metrics**:
- Gestalt Pattern Matching
- Hamming Distance
- Damerau-Levenshtein Distance
- Simple ratio of fuzzy string matching (based on Levenshtein distance) and a word-level 'value words' metric

**Calculation**: Hamming distance: counts differing characters between equal-length strings (padding applied when lengths differ). Damerau-Levenshtein distance: minimal number of edit operations including insertions, deletions, substitutions and transpositions as defined by the recursive formulation in the paper. Gestalt pattern matching: finds the longest adjacent identical subsequence (anchor) and recurses on subsequences. Simple ratio: weighted comparison using Levenshtein distance and word-level comparisons ('value words').

**Interpretation**: Higher fuzzy-matching similarity threshold yields higher accuracy of the generated parallel corpus. Among the evaluated metrics, Hamming distance produced higher accuracy values than the others across reported thresholds.

**Baseline Results**: Accuracy of parallel corpora for different thresholds (Table VII):
50% — Gestalt Pattern Matching: 49.79; Hamming Distance: 71.73; Damerau-Levenshtein Distance: 33.09
60% — Gestalt Pattern Matching: 50.04; Hamming Distance: 73.4; Damerau-Levenshtein Distance: 43.14
70% — Gestalt Pattern Matching: 66.6; Hamming Distance: 77.98; Damerau-Levenshtein Distance: 56.3
80% — Gestalt Pattern Matching: 80.04; Hamming Distance: 85.19; Damerau-Levenshtein Distance: 69.36

**Validation**: Validated by computing accuracies of the generated parallel corpus at multiple similarity thresholds (50%, 60%, 70%, 80%) using Gestalt Pattern Matching, Hamming Distance, and Damerau-Levenshtein Distance on data crawled for December 2017 (22,625 Hindi articles; 226,250 English articles). Sample sentence-pairs for each threshold are provided in Tables II–V.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
