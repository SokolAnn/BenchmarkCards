# BenchIEFL (BenchIE Full Annotation)

## 📊 Benchmark Details

**Name**: BenchIEFL (BenchIE Full Annotation)

**Overview**: BenchIEFL is a new Open Information Extraction (OIE) benchmark created by re-annotating the existing BenchIE dataset to correct errors and improve annotation consistency and methodology.

**Data Type**: extraction tuples

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- BenchIE
- CaRB
- WiRE57

**Resources**:
- [GitHub Repository](https://github.com/rali-udem/benchie_fl.git)

## 🎯 Purpose and Intended Users

**Goal**: To provide a more reliable and accurate benchmark for evaluating Open Information Extraction systems, leading to better performance assessments on downstream tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Open Information Extraction
- Question Answering
- Knowledge Base Population

**Limitations**: The benchmark lacks a sufficient size for training models and is currently only available in English.

## 💾 Data

**Source**: The benchmark is created from re-annotated sentences originally from BenchIE.

**Size**: 300 sentences

**Format**: JSON

**Annotation**: Annotations were performed manually following specific guidelines aimed at improving accuracy and consistency.

## 🔬 Methodology

**Methods**:
- Manual evaluation
- Matching function using heuristics

**Metrics**:
- F1 Score
- Precision
- Recall

**Calculation**: Metrics are calculated based on the new matching function which allows more flexible captures of valid extractions.

**Interpretation**: Higher scores indicate better alignment of extractions with the annotated tuples while considering the validation of tuples across various defined heuristics.

**Baseline Results**: Comparison results from state-of-the-art extractors such as ReVerb and MinIE, with BenchIEFL showing more accurate reflections of performance.

**Validation**: Validation procedures included assessments from multiple expert annotators to ensure adherence to the benchmark guidelines.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: There is a lack of demographic breakdown in the dataset.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
