# LAMP-CAP (Personalized Figure Caption Generation with Multimodal Figure Profiles)

## 📊 Benchmark Details

**Name**: LAMP-CAP (Personalized Figure Caption Generation with Multimodal Figure Profiles)

**Overview**: LAMP-CAP is a dataset for personalized caption generation with multimodal figure profiles, providing not only inputs such as figure images but also up to three other figures from the same document to help characterize context.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Crowd-AI-Lab/lamp-cap)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to enhance personalized caption generation for scientific figures using multimodal profiles.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Text Generation

**Limitations**: N/A

## 💾 Data

**Source**: Curated from the SCI-CAP Challenge Dataset

**Size**: 110,828 target figures

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- BLEU Score
- ROUGE-L

**Calculation**: Metrics were calculated based on the similarity of generated captions to original captions.

**Interpretation**: Higher scores indicate that the generated captions are more similar to the original captions.

**Baseline Results**: N/A

**Validation**: Dataset was split into training, validation, and testing sets following the SCICAP Challenge's split.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
