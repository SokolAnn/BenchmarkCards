# GRAPHIC BENCH

## 📊 Benchmark Details

**Name**: GRAPHIC BENCH

**Overview**: GRAPHIC BENCH is a planning benchmark for graphic design that covers 1,079 user queries and input images across four design types.

**Data Type**: user queries and input images

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/adobe-research)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the design planning abilities of LLM agents in graphic design tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Workflow Planning
- Design Generation

**Limitations**: GRAPHIC BENCH assumes user queries explicitly specify text and image content.

## 💾 Data

**Source**: 1,079 user queries paired with input images collected from various design projects on the Behance platform.

**Size**: 1,079 examples

**Format**: JSON

**Annotation**: Human-annotated user queries and design outputs.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Model-based evaluation

**Metrics**:
- Delivery Rate
- Design Pass Rate
- Success Rate
- Fidelity
- Content Similarity

**Calculation**: Metrics are calculated based on the performance of LLM agents in completing design tasks.

**Interpretation**: Scores across various metrics indicate the effectiveness and accuracy of design outputs.

**Baseline Results**: N/A

**Validation**: Validated through automated evaluations and human assessments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
