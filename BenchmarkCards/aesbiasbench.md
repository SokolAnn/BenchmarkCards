# AesBiasBench

## 📊 Benchmark Details

**Name**: AesBiasBench

**Overview**: AesBiasBench is a benchmark designed to evaluate Multimodal Large Language Models (MLLMs) along two dimensions: stereotype bias, measured by variations in evaluations across demographic groups, and alignment between model outputs and human aesthetic preferences. It includes three subtasks: Aesthetic Perception, Aesthetic Assessment, and Aesthetic Empathy, with structured metrics such as IFD, NRD, and AAS.

**Data Type**: image-quality assessments

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- PARA
- LAPIS

**Resources**:
- [Resource](https://arxiv.org/abs/2509.11620)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark and identify bias in MLLMs for Personalized Image Aesthetic Assessment, fostering greater awareness within the research community and contributing to the development of more equitable AI systems.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Aesthetic Perception
- Aesthetic Assessment
- Aesthetic Empathy

**Limitations**: The analysis is focused on three identity attributes: age, gender, and education, limiting the understanding of bias in MLLMs.

## 💾 Data

**Source**: Personalized Image Aesthetics Database (PARA) and Leuven Art Personalized Image Set (LAPIS)

**Size**: 31,220 images in PARA; 11,723 images in LAPIS

**Format**: N/A

**Annotation**: Annotated by human raters for aesthetic properties and preferences.

## 🔬 Methodology

**Methods**:
- Bias analysis using Identity Frequency Disparity (IFD) and Normalized Representation Disparity (NRD)
- Aesthetic Alignment Score (AAS) for alignment evaluation

**Metrics**:
- Identity Frequency Disparity (IFD)
- Normalized Representation Disparity (NRD)
- Aesthetic Alignment Score (AAS)

**Calculation**: Metrics are calculated using demographic group comparisons and deviations from demographic parity.

**Interpretation**: Higher scores indicate greater stereotype bias (IFD, NRD) and closer alignment with human preferences (AAS).

**Baseline Results**: Results indicating smaller models exhibit stronger stereotypes biases, while larger models align more closely with human preferences.

**Validation**: Evaluated across multiple models and datasets, highlighting the robustness of findings.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Transparency

**Atlas Risks**:
- **Fairness**: Output bias, Data bias
- **Transparency**: Lack of training data transparency

**Demographic Analysis**: Analysis based on gender, age, and education.

**Potential Harm**: ['Potential reinforcement of societal stereotypes', 'Bias in aesthetic evaluations influenced by demographic factors']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All demographic attributes used for analysis are anonymized and aggregated, with no personally identifiable information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
