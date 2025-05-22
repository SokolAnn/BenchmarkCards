# ChineseSafe

## 📊 Benchmark Details

**Name**: ChineseSafe

**Overview**: A Chinese Benchmark for Evaluating Safety in Large Language Models, facilitating research on content safety of large language models with 205,034 examples across 4 classes and 10 sub-classes of safety issues.

**Data Type**: text

**Domains**:
- Chinese language
- Internet content moderation

**Languages**:
- Chinese

**Similar Benchmarks**:
- SafetyBench
- CHiSafetyBench
- CHBench

**Resources**:
- [Resource](https://huggingface.co/spaces/SUSTech/ChineseSafe-Benchmark)
- [Resource](https://huggingface.co/datasets/SUSTech/ChineseSafe)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the safety of large language models in recognizing illegal and unsafe content in Chinese contexts.

**Target Audience**:
- Researchers
- Developers

**Tasks**:
- Safety assessment of LLMs
- Content moderation

**Limitations**: N/A

**Out of Scope Uses**:
- Evaluation outside Chinese context

## 💾 Data

**Source**: Open-sourced datasets and web resources

**Size**: 205,034 examples in total

**Format**: N/A

**Annotation**: Categorized into 4 classes and 10 sub-classes of safety issues.

## 🔬 Methodology

**Methods**:
- Generation-based evaluation
- Perplexity-based evaluation

**Metrics**:
- Overall accuracy
- Precision
- Recall

**Calculation**: N/A

**Interpretation**: Higher precision indicates better identification of unsafe content.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Legal risks
- Safety vulnerabilities

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Societal Impact**: Impact on cultural diversity, Impact on education: plagiarism

**Demographic Analysis**: N/A

**Potential Harm**: ['Legal consequences for content providers', 'Misinformation impact in society']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Aligned with Chinese Internet content moderation regulations.
