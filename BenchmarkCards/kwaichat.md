# KwaiChat

## 📊 Benchmark Details

**Name**: KwaiChat

**Overview**: KwaiChat is a human-to-human video-driven multilingual mixed-type dialogue corpus created to facilitate the study of video-driven mixed-type multi-participant dialogue generation. It contains a total of 93,209 videos and 246,080 dialogues across 4 dialogue types, 30 domains, and 4 languages.

**Data Type**: video-dialogue pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese
- Indonesian
- Portuguese
- Spanish

**Similar Benchmarks**:
- VisDial
- YTD-18M
- A VSD

**Resources**:
- [GitHub Repository](https://github.com/Stan-lei/KwaiChat-NAACL2025)

## 🎯 Purpose and Intended Users

**Goal**: To promote research on video-driven mixed-type multi-participant dialogue generation.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Dialogue Generation

**Limitations**: N/A

## 💾 Data

**Source**: Collected from a video-sharing platform Kwai

**Size**: 93,209 videos and 246,080 dialogues

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- BLEU Score
- ROUGE-L
- Diversity measures (DIST-2, DIST-3)

**Calculation**: BLEU measures are calculated as the ratio of n-grams in the generated response that are present in the reference response; ROUGE-L focuses on the longest common subsequence.

**Interpretation**: Higher BLEU scores indicate better performance in generating text that matches reference text.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Societal Impact

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Societal Impact**: Impact on affected communities

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Content that could compromise privacy was removed from the dataset.

**Data Licensing**: Not Applicable

**Consent Procedures**: Permission was secured to access the data.

**Compliance With Regulations**: Not Applicable
