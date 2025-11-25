# CoCoNUTS (Concentrating on Content while Neglecting Uninformative Textual Styles for AI-Generated Peer Review Detection)

## 📊 Benchmark Details

**Name**: CoCoNUTS (Concentrating on Content while Neglecting Uninformative Textual Styles for AI-Generated Peer Review Detection)

**Overview**: CoCoNUTS is a content-oriented benchmark for AI-generated peer review detection, capturing six distinct modes of human-AI collaboration. It aims to facilitate a more accurate and robust evaluation of AI involvement in the peer review process.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- M4GT-Bench
- MGTBench
- FAIDset
- LLMDetect
- AIPR-Detection-Benchmark

**Resources**:
- [GitHub Repository](https://github.com/Y1hanChen/COCONUTS)

## 🎯 Purpose and Intended Users

**Goal**: To provide a foundation for evaluating AI's role in peer review and improve detection methods for AI-generated content.

**Target Audience**:
- ML Researchers
- Academic Publishers
- Conference Organizers

**Tasks**:
- AI Text Detection

**Limitations**: N/A

## 💾 Data

**Source**: Reviews collected from OpenReview across several academic venues, including ICLR, NeurIPS, UAI, CoRL, and EMNLP.

**Size**: 315,535 instances

**Format**: JSON

**Annotation**: Automatically generated with multi-task learning integration.

## 🔬 Methodology

**Methods**:
- Multi-task learning
- Content Composition Identification
- Collaboration Mode Attribution
- Content Source Attribution
- Textual Style Attribution

**Metrics**:
- Macro F1 Score

**Calculation**: F1 Score is calculated for each class (Human, Mix, AI) to evaluate model performance.

**Interpretation**: A higher F1 Score indicates better performance in detecting AI-generated content in peer reviews.

**Baseline Results**: CoCoDet achieved a macro F1 score exceeding 98% on the ternary detection task.

**Validation**: Data partitioned into training, validation, and test sets with stratified random sampling.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Misuse of AI in peer review processes.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
