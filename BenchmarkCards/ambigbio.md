# AmbigBio

## 📊 Benchmark Details

**Name**: AmbigBio

**Overview**: AmbigBio is a new dataset developed for evaluating the factuality of long-form generations by large language models, particularly focusing on names with entity ambiguity, where each name corresponds to multiple entities in Wikipedia.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/d223302/Merging-Facts-Crafting-Fallacies)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the factuality of long-form generations from large language models by focusing on entity ambiguity.

**Target Audience**:
- ML Researchers
- NLP Practitioners

**Tasks**:
- Text Generation
- Fact Verification

**Limitations**: N/A

## 💾 Data

**Source**: 500 ambiguous names collected from Wikipedia disambiguation pages.

**Size**: 500 examples

**Format**: N/A

**Annotation**: Manual annotation by humans for evaluating factuality.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- D-FActScore

**Calculation**: D-FActScore is calculated by grouping atomic facts and verifying them against the best-matching Wikipedia entity.

**Interpretation**: A lower D-FActScore indicates a higher likelihood of mixing facts of different entities, thus being non-factual.

**Validation**: Human evaluation correlates with automatic evaluations for validating D-FActScore.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
