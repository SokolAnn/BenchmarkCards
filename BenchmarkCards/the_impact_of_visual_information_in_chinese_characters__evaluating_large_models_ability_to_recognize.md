# The Impact of Visual Information in Chinese Characters: Evaluating Large Models’ Ability to Recognize and Utilize Radicals

## 📊 Benchmark Details

**Name**: The Impact of Visual Information in Chinese Characters: Evaluating Large Models’ Ability to Recognize and Utilize Radicals

**Overview**: This study establishes a benchmark to evaluate LLMs’ and VLMs’ understanding of visual elements in Chinese characters, including radicals, composition structures, strokes, and stroke counts.

**Data Type**: Chinese character data with radicals, strokes, and structural compositions

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/xwu414/Chinese-Character-Benchmark)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate how contemporary LLMs and VLMs can recognize and utilize visual information present in Chinese characters.

**Target Audience**:
- ML Researchers
- NLP Practitioners

**Tasks**:
- Structure Recognition
- Radical Recognition
- Stroke Count Identification
- Stroke Decomposition

**Limitations**: The dataset does not represent the full range of Chinese characters, primarily focusing on simplified characters.

## 💾 Data

**Source**: Collected from the CJK Unified Ideographs with visual features sourced from authoritative Chinese dictionaries.

**Size**: 14,648 Chinese characters

**Format**: N/A

**Annotation**: Manual review and annotation of radicals and strokes by native Chinese speakers

## 🔬 Methodology

**Methods**:
- Automated metrics
- F1 Score evaluation

**Metrics**:
- F1 Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)

**Calculation**: Metrics are calculated based on model predictions against a ground truth derived from the benchmark dataset.

**Interpretation**: Higher F1 Scores indicate a better understanding of visual components in Chinese characters.

**Baseline Results**: PIXEL achieved an F1 score of 84.57 on the structure recognition task.

**Validation**: Models were evaluated using a variety of tasks assessing their understanding of visual aspects in the characters.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
