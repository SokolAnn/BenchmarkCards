# TRACSUM: A New Benchmark for Aspect-Based Summarization with Sentence-Level Traceability in Medical Domain

## 📊 Benchmark Details

**Name**: TRACSUM: A New Benchmark for Aspect-Based Summarization with Sentence-Level Traceability in Medical Domain

**Overview**: TRACSUM is a benchmark for generating traceable, aspect-based summaries of medical abstracts, paired with sentence-level citations to support factual accuracy. It includes a dataset of annotated medical abstracts across seven aspects, resulting in 3.5K summary-citation pairs, and establishes a fine-grained evaluation framework for assessing completeness and consistency in generated content.

**Data Type**: summary-citation pairs

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/chubohao/TracSum)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for evaluating traceable aspect-based summarization in the medical domain.

**Target Audience**:
- ML Researchers
- Medical Professionals
- NLP Practitioners

**Tasks**:
- Aspect-Based Summarization

**Limitations**: The dataset was generated using the Mistral Large model, which may introduce model-specific biases.

## 💾 Data

**Source**: Annotated medical abstracts from PubMed focusing on melanoma, filtered for key criteria and annotated for seven medical aspects.

**Size**: 3,500 summary-citation pairs

**Format**: JSON

**Annotation**: Annotated by a team of medical students and NLP researchers, incorporating qualitative evaluation metrics.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Completeness
- Conciseness
- Traceability

**Calculation**: Metrics are calculated based on the recall and precision of generated summaries and their corresponding citations using predefined evaluation frameworks.

**Interpretation**: Higher values for completeness and conciseness indicate better performance of the summarization model.

**Baseline Results**: TRACK-THEN-SUM (TTS) serves as the baseline method against which other systems are compared.

**Validation**: The performance is evaluated through a combination of qualitative human assessments and quantitative metrics based on the dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Participants gave explicit consent for data usage for research purposes during the annotation process.

**Compliance With Regulations**: Not Applicable
