# Language ID in the Wild: Unexpected Challenges on the Path to a Thousand-Language Web Text Corpus

## 📊 Benchmark Details

**Name**: Language ID in the Wild: Unexpected Challenges on the Path to a Thousand-Language Web Text Corpus

**Overview**: This paper demonstrates the challenges of language identification (LangID) when generating web text corpora across numerous languages. It highlights the inaccuracies of current LangID methods when applied to real-world data and proposes new evaluation techniques to generate a more robust and cleaner web text corpus in over 600 languages.

**Data Type**: sentence corpus

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- OSCAR
- CCNet

**Resources**:
- [GitHub Repository](https://github.com/google-research-datasets/TF-IDF-IIF-top100-wordlists)

## 🎯 Purpose and Intended Users

**Goal**: To create accurate and robust multilingual web text corpora for enhancing language technology applications in low-resource languages.

**Target Audience**:
- ML Researchers
- Language Technologists
- Data Scientists

**Tasks**:
- Language Identification
- Text Corpus Generation

**Limitations**: The effectiveness of the generated dataset may vary based on the specific characteristics of individual languages.

## 💾 Data

**Source**: Comprehensive web crawl across various languages using automated language identification models and data filtering techniques.

**Size**: 600 languages, >100 billion documents

**Format**: Text corpus

**Annotation**: Human-judged evaluations for precision and recall, automated filtering using curated wordlists.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Document-consistency filtering

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are derived from the proportion of in-language sentences to total sentences evaluated.

**Interpretation**: Higher precision indicates a cleaner dataset, while recall measures the coverage of the original languages in the crawl.

**Baseline Results**: Initial precision of generated corpora at 5%, improved to 71.2% using proposed filtering techniques.

**Validation**: Validation through human evaluation and comparison against other public datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: Analysis of lower-resource language representation in dataset.

**Potential Harm**: ['Including disallowed data from misclassified languages in corpus.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The work is licensed under a Creative Commons Attribution 4.0 International License.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
