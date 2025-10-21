# MLLM-Bench

## 📊 Benchmark Details

**Name**: MLLM-Bench

**Overview**: We propose a new evaluation paradigm for MLLMs, evaluating MLLMs with per-sample criteria using potent MLLM as the judge. To validate this paradigm, we design a benchmark, dubbed MLLM-Bench, by curating the evaluation samples across six comprehensive cognitive levels.

**Data Type**: image-instruction pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMBench
- MM-Vet
- Alpaca-Eval

**Resources**:
- [Resource](https://mllm-bench.llmzoo.com)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of multimodal large language models using a new paradigm that focuses on real-world user experiences through per-sample criteria.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Image Captioning
- Object Recognition
- Medical Image Understanding

**Limitations**: N/A

## 💾 Data

**Source**: Images curated from social networks or personal captures, instruction construction based on GPT-4V output.

**Size**: 420 image-instruction pairs

**Format**: N/A

**Annotation**: Data collected and annotated by six volunteers under specific guidelines.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Pairwise evaluation using GPT-4V

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Win/tie/loss ratios from pairwise evaluations.

**Interpretation**: Higher win rates indicate better model performance relative to the anchor model.

**Baseline Results**: LLaV A-v1.5-13B acts as the anchor model for evaluations.

**Validation**: Three rounds of cross-review and expert verification.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
