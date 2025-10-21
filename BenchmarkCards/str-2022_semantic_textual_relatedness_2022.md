# STR-2022 (Semantic Textual Relatedness 2022)

## 📊 Benchmark Details

**Name**: STR-2022 (Semantic Textual Relatedness 2022)

**Overview**: The first manually annotated dataset of sentence-sentence semantic relatedness with 5,500 English sentence pairs and fine-grained relatedness scores from 0 to 1.

**Data Type**: sentence pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- STS (Semantic Textual Similarity)

**Resources**:
- [Resource](https://doi.org/10.5281/zenodo.7599667)
- [GitHub Repository](https://github.com/Priya22/semantic-textual-relatedness)
- [Resource](https://huggingface.co/datasets/vkpriya/str-2022)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for exploring the semantic relatedness of sentence pairs and to evaluate automatic methods of sentence representation.

**Target Audience**:
- ML Researchers
- NLP Practitioners

**Tasks**:
- Sentence Relatedness

**Limitations**: N/A

## 💾 Data

**Source**: Curated from various sources including Goodreads, Wikipedia, SNLI, among others.

**Size**: 5,500 sentence pairs

**Format**: CSV

**Annotation**: Manually annotated using a comparative annotation framework.

## 🔬 Methodology

**Methods**:
- Comparative annotation
- Crowdsourced annotation via Amazon Mechanical Turk

**Metrics**:
- Reliability measured using Split-Half Reliability (SHR)

**Calculation**: Spearman correlation between predicted and gold relatedness scores.

**Interpretation**: A higher score indicates greater semantic relatedness between two sentences.

**Baseline Results**: N/A

**Validation**: Validation was performed using a reliable annotation process with repeat annotations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The dataset may include more sentences from people with certain socio-economic and educational backgrounds.

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No identifiable information was collected from annotators, and sentences were selected to pose no privacy risk.

**Data Licensing**: Not Applicable

**Consent Procedures**: The crowd-sourced task was approved by the Institutional Research Ethics Board.

**Compliance With Regulations**: Not Applicable
