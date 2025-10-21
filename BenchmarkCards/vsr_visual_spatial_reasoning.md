# VSR (Visual Spatial Reasoning)

## 📊 Benchmark Details

**Name**: VSR (Visual Spatial Reasoning)

**Overview**: The benchmark evaluates the capabilities of Vision Large Language Models (VLLMs) in recognizing visual positional information and following instructions related to spatial reasoning. It addresses issues of inconsistent performance and answer bias in existing models by proposing a unified instruction test set and expanding existing datasets.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MME
- MMBench
- SEED

**Resources**:
- [GitHub Repository](https://github.com/peijin360/vsre)

## 🎯 Purpose and Intended Users

**Goal**: To enhance the evaluation and optimization of VLLMs in visual spatial reasoning tasks by providing a unified instruction test set and expanded datasets.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Visual Spatial Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: The original VSR dataset and augmented data generated through diffusion models and instruction templates.

**Size**: 500,000 examples

**Format**: N/A

**Annotation**: Data was expanded through manual and GPT-4 generated templates.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy was calculated based on the model's responses to spatial reasoning questions.

**Interpretation**: Higher accuracy indicates better understanding and differentiation of visual positional relationships.

**Baseline Results**: LLaV A1.5 achieved scores of 54.3 / 65.3 before optimization.

**Validation**: The benchmark was validated through experiments with multiple VLLM architectures.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Output bias
- **Robustness**: Data poisoning
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
