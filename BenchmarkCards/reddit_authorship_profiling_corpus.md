# Reddit Authorship Profiling Corpus

## 📊 Benchmark Details

**Name**: Reddit Authorship Profiling Corpus

**Overview**: This paper introduces a corpus of short texts in the Romanian language, annotated with certain author characteristic keywords, based on posts extracted from over 100 Romanian subreddits, aimed at advancing authorship profiling technology for Romanian.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Romanian

**Resources**:
- [Resource](https://huggingface.co/roship-profiling)

## 🎯 Purpose and Intended Users

**Goal**: To advance the capabilities of authorship profiling technology for the Romanian language.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Linguists

**Tasks**:
- Authorship Profiling

**Limitations**: N/A

## 💾 Data

**Source**: Posts extracted from 100+ Romanian subreddits using the Reddit API.

**Size**: 29,317 examples

**Format**: CSV

**Annotation**: Manual annotation with keywords corresponding to author characteristics.

## 🔬 Methodology

**Methods**:
- Fine-tuning of Large Language Models
- Human evaluation

**Metrics**:
- Accuracy
- Intersection over Union (IoU)

**Calculation**: Accuracy is calculated based on exact match of generated keywords against expected keywords.

**Interpretation**: Higher accuracy and IoU indicate better performance of the authorship profiling model.

**Baseline Results**: Accuracy of 78.5% on the test split.

**Validation**: Dataset was split into training (95%), evaluation (5%), and test (5%) sets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
