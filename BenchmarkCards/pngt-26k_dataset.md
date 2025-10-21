# PNGT-26K Dataset

## 📊 Benchmark Details

**Name**: PNGT-26K Dataset

**Overview**: PNGT-26K is a comprehensive dataset of approximately 26,000 Persian names, their commonly associated gender, and their English transliteration, systematically curated to address the transliteration bottleneck.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Persian

**Resources**:
- [Resource](https://huggingface.co/datasets/farbodbij/persian-gender-by-name)
- [GitHub Repository](https://github.com/farbodbj/Nominalist)
- [GitHub Repository](https://github.com/farbodbj/Open-Gender-Detection)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large, open, and systematically curated resource for Persian names with transliterations, offering researchers and practitioners a foundation for developing culturally-aware NLP applications.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Domain Experts

**Tasks**:
- Gender Detection
- Username Generation

**Limitations**: N/A

## 💾 Data

**Source**: Curated from existing datasets including iranian-Names-Database-By-Gender, persian-names, and persian-names-gender using careful sampling and validation by native speakers.

**Size**: 26,000 tuples

**Format**: Tuple

**Annotation**: Manually validated and annotated by native speakers.

## 🔬 Methodology

**Methods**:
- Data Compilation
- Probabilistic Gender Detection
- Username Generation Framework

**Metrics**:
- Accuracy

**Calculation**: Calculated using normalized Levenshtein distance and multimodal approaches combining image and name inference.

**Interpretation**: Probabilistic output reflecting confidence in gender prediction based on name and profile analysis.

**Baseline Results**: N/A

**Validation**: Manual review of flagged records for transliteration and validation against existing name databases.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
