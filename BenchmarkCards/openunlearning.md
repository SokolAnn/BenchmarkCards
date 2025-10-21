# OpenUnlearning

## 📊 Benchmark Details

**Name**: OpenUnlearning

**Overview**: OpenUnlearning is a standardized and extensible framework designed explicitly for benchmarking LLM unlearning methods and metrics. It integrates unlearning algorithms and diverse evaluations across established benchmarks, facilitating comparative analysis and reproducibility in machine unlearning research.

**Data Type**: unlearning methods and metrics evaluation

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TOFU
- MUSE
- WMDP

**Resources**:
- [GitHub Repository](https://github.com/locuslab/open-unlearning)
- [Resource](https://huggingface.co/open-unlearning)

## 🎯 Purpose and Intended Users

**Goal**: To establish a unified framework for benchmarking and improving LLM unlearning methods and metrics, enabling rigorous and reproducible research.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Unlearning Evaluation
- Benchmarking Unlearning Methods

**Limitations**: N/A

## 💾 Data

**Source**: Open-sourced model checkpoints and data generated for the benchmarks.

**Size**: 450+ models

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Unlearning Evaluation
- Meta-Evaluation
- Benchmarking

**Metrics**:
- Extraction Strength
- Exact Memorization
- Truth Ratio
- Probability
- ROUGE

**Calculation**: Metrics are calculated based on evaluations conducted on various unlearned models under consistent conditions.

**Interpretation**: High scores in metrics indicate effective unlearning and retention of model utility.

**Baseline Results**: Results involve comparisons based on multiple unlearning methods with established benchmarks.

**Validation**: Model behavior is validated against standard metrics like Truth Ratio and Mean Utility.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Accuracy
- Robustness

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Robustness**: Evasion attack, Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: MIT License

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
