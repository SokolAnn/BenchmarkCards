# XOR-TYDIQA

## 📊 Benchmark Details

**Name**: XOR-TYDIQA

**Overview**: XOR-TYDIQA is a large-scale dataset that consists of 40,000 information-seeking questions across 7 diverse non-English languages, aimed at facilitating the task of cross-lingual open-retrieval question answering.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Arabic
- Bengali
- Finnish
- Japanese
- Korean
- Russian
- Telugu

**Similar Benchmarks**:
- TYDIQA

**Resources**:
- [Resource](https://nlp.cs.washington.edu/xorqa/)

## 🎯 Purpose and Intended Users

**Goal**: To support research in cross-lingual open-retrieval question answering by providing a dataset that helps address information scarcity in multilingual contexts.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Cross-lingual Document Retrieval
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Annotated questions and answers collected from TYDIQA and crowdsourced annotation from native speakers.

**Size**: 40,000 questions

**Format**: JSON

**Annotation**: Cross-lingual retrieval facilitated by professional translators and crowdsourced native speaker annotators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Exact Match (EM)
- BLEU Score

**Calculation**: Metrics are calculated based on the agreement between predicted answers and ground truth annotations.

**Interpretation**: Higher scores indicate better model performance in retrieving and answering questions accurately.

**Baseline Results**: The best baseline achieves an average of 18.7 F1 points on the XOR-FULL task.

**Validation**: Models were validated using question-answer pairs in the dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The dataset includes questions from native speakers of diverse languages, aiming to mitigate bias in QA systems.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Crowdworkers consented to have their responses used in this way through the Amazon Mechanical Turk Participation Agreement.

**Compliance With Regulations**: Not Applicable
