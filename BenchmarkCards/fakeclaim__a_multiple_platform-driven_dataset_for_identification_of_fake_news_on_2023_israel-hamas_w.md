# FakeClaim: A Multiple Platform-driven Dataset for Identification of Fake News on 2023 Israel-Hamas War

## 📊 Benchmark Details

**Name**: FakeClaim: A Multiple Platform-driven Dataset for Identification of Fake News on 2023 Israel-Hamas War

**Overview**: The paper introduces the first publicly available dataset of factual claims from different platforms and fake YouTube videos on the 2023 Israel-Hamas war for automatic fake YouTube video classification. The dataset comprises 1,499 claims collected from 1,370 fact-checked articles published by 60 fact-checking organizations in 30 languages.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Gautamshahi/FakeClaim)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to provide a dataset for automatic fake YouTube video classification and to support research in fake news detection.

**Target Audience**:
- ML Researchers
- Fact Checkers

**Tasks**:
- Text Classification

**Limitations**: The true class was not manually checked or fact-checked.

## 💾 Data

**Source**: Collected from 1,370 fact-checked articles published by 60 fact-checking organizations in 30 languages.

**Size**: 1,499 claims

**Format**: N/A

**Annotation**: Enriched with metadata curated by trained journalists specialized in fact-checking.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Machine learning classification

**Metrics**:
- Macro F1 Score

**Calculation**: F1 Score is calculated based on precision and recall.

**Interpretation**: An F1 Score closer to 1 indicates better model performance.

**Baseline Results**: Universal Sentence Encoder achieved a Macro F1 of 87%.

**Validation**: Classified each video using textual information and user comments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Users' personal information is neither used nor stored for classification in this paper.

**Data Licensing**: The dataset is available publicly for further research following the policy for sharing data.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
