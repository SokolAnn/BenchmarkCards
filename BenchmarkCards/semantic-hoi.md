# Semantic-HOI

## 📊 Benchmark Details

**Name**: Semantic-HOI

**Overview**: Semantic-HOI is a new dataset featuring over 20K paired Human-Object Interaction (HOI) states with fine-grained descriptions for each state and the body movements that happen between two consecutive states.

**Data Type**: paired HOI states with descriptions

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://f-hoi.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To bridge the annotation gap present in current datasets by providing fine-grained descriptions for HOI states and the body movement between two consecutive states.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Understanding
- Reasoning
- Generation

**Limitations**: N/A

## 💾 Data

**Source**: Derived from three existing datasets: GRAB, CHAIRS, and BEHAVE.

**Size**: 20,441 pairs

**Format**: N/A

**Annotation**: Fine-grained descriptions generated using prompts for state descriptions and movements, verified manually.

## 🔬 Methodology

**Methods**:
- Multi-task training
- Prompt-based manual verification

**Metrics**:
- BLEU-4
- ROUGE

**Calculation**: Metrics calculated based on textual descriptions comparing predicted outputs to ground truth.

**Interpretation**: Higher BLEU-4 and ROUGE scores indicate better alignment with fine-grained semantic descriptions.

**Baseline Results**: N/A

**Validation**: The dataset was split into training and testing sets, with about 70% used for training and 30% for testing.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
