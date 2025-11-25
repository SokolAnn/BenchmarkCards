# DeepJSONEval

## 📊 Benchmark Details

**Name**: DeepJSONEval

**Overview**: DeepJSONEval is a pioneering multilingual deep-nested JSON evaluation benchmark designed to assess LLMs' ability to convert raw text into structured JSON formats with complex nested calculations. It features 2100 instances categorized by difficulty, allowing for robust evaluation in web data mining contexts.

**Data Type**: JSON instances

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/GTS-AI-Intra-Lab-SotaS/DeepJSONEval)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for assessing the structured output capabilities of large language models in deep nested JSON generation and information extraction tasks.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Structured Data Extraction

**Limitations**: N/A

## 💾 Data

**Source**: Diverse web sources collected through systematic text aggregation and schema generation algorithms.

**Size**: 2,100 instances

**Format**: JSON

**Annotation**: Ground truth established through expert validation and a human-in-the-loop quality control process.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Syntax Score
- Hierarchical key matching Score
- Strict Score

**Calculation**: Metrics are calculated based on a multi-dimensional evaluation framework assessing JSON structural correctness, format adherence, and content accuracy.

**Interpretation**: Higher scores indicate better performance in generating accurate and structured JSON outputs.

**Validation**: Systematic dual review process involving independent evaluation and consensus checks to ensure quality and fidelity.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
