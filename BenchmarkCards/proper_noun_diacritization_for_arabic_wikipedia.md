# Proper Noun Diacritization for Arabic Wikipedia

## 📊 Benchmark Details

**Name**: Proper Noun Diacritization for Arabic Wikipedia

**Overview**: We introduce a new manually diacritized dataset of Arabic proper nouns of various origins paired with their English Wikipedia equivalents, enabling the study of joint diacritization and transliteration.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Arabic
- English

**Similar Benchmarks**:
- CP-S AMA
- CP-W IKI

**Resources**:
- [GitHub Repository](https://github.com/CAMeL-Lab/CamelProp)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate further research on Arabic Wikipedia proper noun diacritization and improve the quality of Arabic NLP resources.

**Target Audience**:
- ML Researchers
- NLP Practitioners
- Academics

**Tasks**:
- Diacritization
- Transliteration

**Limitations**: N/A

## 💾 Data

**Source**: Manually selected from Arabic Wikipedia entries and annotated with English glosses.

**Size**: 3,362 pairs

**Format**: CSV

**Annotation**: Manual annotation by experts

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Levenshtein edit distance

**Calculation**: Metrics are calculated based on exact matches and edit distances between generated outputs and gold-standard diacritizations.

**Interpretation**: Higher accuracy indicates better performance in producing correct diacritizations.

**Baseline Results**: GPT-4o achieved a best accuracy of 73% on the task.

**Validation**: Results were validated through inter-annotator agreement, and performance evaluations were conducted with varied input formats.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data sourced from publicly available resources, no personal data involved.

**Data Licensing**: CC BY-SA

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
