# ArgCMV (Argument Summarization Benchmark for the LLM-era)

## 📊 Benchmark Details

**Name**: ArgCMV (Argument Summarization Benchmark for the LLM-era)

**Overview**: ArgCMV is a key point-based argument summarization benchmark consisting of long-context, multi-turn arguments from actual online human debates sourced from Reddit’s r/ChangeMyView, aiming to evaluate the key point extraction task with complex arguments.

**Data Type**: argument-key point pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ArgKP21

**Resources**:
- [GitHub Repository](https://github.com/omkar2810/ArgCMV)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for key point extraction in argument summarization, improving upon the limitations of previous datasets like ArgKP21.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Key Point Extraction
- Argument Summarization

**Limitations**: Limited number of arguments in certain topics and restricted to discussions occurring in 2020.

## 💾 Data

**Source**: Threads from Reddit’s r/ChangeMyView community.

**Size**: 12,262 arguments

**Format**: JSON

**Annotation**: Key points extracted using a combination of state-of-the-art language models followed by human validation.

## 🔬 Methodology

**Methods**:
- Key Point Extraction using LLMs
- Ground truth mapping with human validation

**Metrics**:
- Rouge
- Precision
- Recall
- F1 Score

**Calculation**: Metrics calculated using ground-truth key points compared to model outputs.

**Interpretation**: Higher recall indicates more key points found in the responses, while higher precision indicates fewer wrong matches in key point extraction.

**Baseline Results**: Existing models show lower performance on ArgCMV compared to ArgKP21.

**Validation**: Manual validation of extracted key points by human annotators with high inter-annotator agreement.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Collected data was anonymized by not linking comments back to authorship.

**Data Licensing**: Not Applicable

**Consent Procedures**: Data was collected passively and in accordance with Reddit’s API policy.

**Compliance With Regulations**: Not Applicable
