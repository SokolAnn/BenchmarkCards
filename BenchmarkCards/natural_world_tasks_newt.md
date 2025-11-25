# Natural World Tasks (NeWT)

## 📊 Benchmark Details

**Name**: Natural World Tasks (NeWT)

**Overview**: NeWT is specifically designed for challenging fine-grained ecological classification tasks requiring expert annotation, offering a comprehensive evaluation of AI models in small-data contexts.

**Data Type**: binary classification tasks

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/samuelstevens/mindthegap)

## 🎯 Purpose and Intended Users

**Goal**: To emphasize the critical-but-neglected small-data regime and advocate for its inclusion in AI research benchmarks.

**Target Audience**:
- AI Researchers
- Ecologists
- Data Scientists

**Tasks**:
- Binary Classification

**Limitations**: N/A

## 💾 Data

**Source**: Manually curated ecological datasets for classification tasks.

**Size**: 164 tasks with 200 to 400 training samples each

**Format**: N/A

**Annotation**: Manual annotation by experts

## 🔬 Methodology

**Methods**:
- Experimental comparison of AI models

**Metrics**:
- Mean Accuracy

**Calculation**: Mean accuracy computed with bootstrapped confidence intervals.

**Interpretation**: A higher mean accuracy indicates better model performance in ecological classification tasks.

**Baseline Results**: N/A

**Validation**: Confidence intervals computed by resampling test sets 1,000 times with replacement.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
