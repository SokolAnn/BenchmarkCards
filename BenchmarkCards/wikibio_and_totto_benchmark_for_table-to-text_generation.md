# WikiBio and ToTTo Benchmark for Table-to-Text Generation

## 📊 Benchmark Details

**Name**: WikiBio and ToTTo Benchmark for Table-to-Text Generation

**Overview**: This paper investigates the effectiveness of in-context learning strategies for table-to-text generation using the WikiBio and ToTTo datasets.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2410.12878)

## 🎯 Purpose and Intended Users

**Goal**: To comprehensively explore the performance of in-context learning in the table-to-text generation task.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Table-to-Text Generation
- Text Generation

**Limitations**: N/A

## 💾 Data

**Source**: WikiBio dataset and ToTTo dataset.

**Size**: Approx. 700,000 pairs of Wikipedia infoboxes and human-written descriptions; 120,000 examples in ToTTo.

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Self-evaluation using LLMs

**Metrics**:
- BLEU
- BERTScore

**Calculation**: BLEU score calculated by overlapping n-grams, BERTScore by using token embeddings for semantic similarity.

**Interpretation**: Higher BLEU and BERT scores indicate better performance.

**Baseline Results**: N/A

**Validation**: Evaluated using various prompting strategies across the datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Hallucination in generated text']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
