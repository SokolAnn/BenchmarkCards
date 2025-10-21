# MuChin (Chinese Colloquial Music Description Benchmark)

## 📊 Benchmark Details

**Name**: MuChin (Chinese Colloquial Music Description Benchmark)

**Overview**: MuChin is the first open-source benchmark designed to evaluate the performance of multimodal large language models in understanding and describing music in Chinese colloquial language. It employs a robust annotation platform to ensure high-precision and popular semantic alignment.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Music

**Languages**:
- Chinese

**Similar Benchmarks**:
- MARBLE

**Resources**:
- [GitHub Repository](https://github.com/CarlWangChina/MuChin)

## 🎯 Purpose and Intended Users

**Goal**: To establish a benchmark for evaluating language models on their ability to generate and understand descriptions of music, particularly from a colloquial perspective.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Textual Description
- Lyric Generation

**Limitations**: N/A

## 💾 Data

**Source**: Caichong Music Annotation Platform (CaiMAP)

**Size**: 1,000 entries

**Format**: JSON

**Annotation**: Multi-person, multi-stage quality assurance process involving both amateur and professional annotators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Semantic Similarity Score

**Calculation**: Scores are calculated based on the similarity of generated lyrics to ground truth across various dimensions including song structure, section similarity, and rhyme matching.

**Interpretation**: Higher scores indicate better alignment and quality of generated music descriptions compared to human annotations.

**Baseline Results**: N/A

**Validation**: Results validated through a multi-tiered quality assurance process involving professional annotators and system checks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
