# BELB (Biomedical Entity Linking Benchmark)

## 📊 Benchmark Details

**Name**: BELB (Biomedical Entity Linking Benchmark)

**Overview**: BELB provides access in a unified format to 11 corpora linked to 7 knowledge bases and spanning six entity types: gene, disease, chemical, species, cell line and variant. It serves as a standardized testbed for reproducible experiments in the biomedical entity linking task.

**Data Type**: text

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- BLUE
- BLURB

**Resources**:
- [GitHub Repository](https://github.com/sg-wbi/belb)
- [GitHub Repository](https://github.com/sg-wbi/belb-exp)

## 🎯 Purpose and Intended Users

**Goal**: To standardize experimental setups for biomedical entity linking and facilitate research by providing a common benchmark.

**Target Audience**:
- ML Researchers
- Biomedical Researchers

**Tasks**:
- Biomedical Entity Linking

**Limitations**: N/A

## 💾 Data

**Source**: 11 corpora linked to 7 knowledge bases including specialized databases for various biomedical entities.

**Size**: N/A

**Format**: Unified format across multiple corpora

**Annotation**: Extensive data cleaning and normalization to ensure consistency.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Mention-level recall@1

**Calculation**: Metrics are calculated based on the accuracy of predictions against gold standard mentions.

**Interpretation**: Results indicate the model's ability to correctly identify and link entity mentions to their corresponding entities in the knowledge base.

**Baseline Results**: Multiple baseline models were evaluated including both rule-based and neural approaches.

**Validation**: Validation against extensive benchmarked test sets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**
- **Fairness**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
