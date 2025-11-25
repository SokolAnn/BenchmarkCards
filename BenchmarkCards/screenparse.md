# ScreenParse

## 📊 Benchmark Details

**Name**: ScreenParse

**Overview**: ScreenParse is a rigorously constructed benchmark to systematically assess structural perception capabilities of GUI models across diverse scenarios.

**Data Type**: image

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- ScreenSpot
- ScreenSpot-v2
- CAGUI-Grounding

**Resources**:
- [GitHub Repository](https://github.com/antgroup/SparkUI-Parser)

## 🎯 Purpose and Intended Users

**Goal**: To provide an evaluation for the performance of models in both locating specific elements and perceiving the overall structure of user interfaces.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Grounding
- Parsing

**Limitations**: N/A

## 💾 Data

**Source**: Open-source datasets and self-annotated Chinese datasets, including elements from common applications.

**Size**: 800 images

**Format**: Images

**Annotation**: Annotated with element types, semantic labels, and bounding boxes through a combination of automated and manual processes.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Element recall
- Element precision
- Semantic similarity

**Calculation**: Element recall is the ratio of correctly localized elements to the total number of ground truth elements, while element precision is the ratio of correctly localized elements to the total number of predicted elements.

**Interpretation**: Higher recall indicates an effective model in identifying elements, while higher precision means fewer incorrect localizations.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
