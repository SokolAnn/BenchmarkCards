# ArxEval

## 📊 Benchmark Details

**Name**: ArxEval

**Overview**: ArxEval is an evaluation pipeline designed for assessing the frequency with which language models hallucinate when generating responses in scientific literature. It includes two main tasks: Jumbled Titles and Mixed Titles, aimed at evaluating the reliability of language models in handling academic content accurately.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2501.10483)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to evaluate the extent of hallucination in large language models when generating responses related to scientific literature.

**Target Audience**:
- Researchers
- Developers
- Practitioners

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: ArXiv dataset

**Size**: 528 titles

**Format**: CSV

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Cosine Similarity
- BERTScore
- STS

**Calculation**: Metrics are calculated based on the cosine similarity between the generated response and the original abstract using various scoring models.

**Interpretation**: Higher similarity scores indicate better adherence to factual accuracy and ability to generate coherent responses under prompt constraints.

**Baseline Results**: Mistral v0.3 achieved the highest similarity scores, while Orca-2 was the lowest performing model.

**Validation**: The evaluation was conducted using a comparative analysis of multiple language models against defined tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Impact on factual accuracy in academic contexts']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
