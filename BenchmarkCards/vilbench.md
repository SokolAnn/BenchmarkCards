# VILBENCH

## 📊 Benchmark Details

**Name**: VILBENCH

**Overview**: VILBENCH is a vision-language benchmark designed to require intensive step-wise reward signals, addressing the need for fine-grained feedback in vision-language tasks.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- VLRewardBench
- URSA
- VisualPRM

**Resources**:
- [Resource](https://ucsc-vlaa.github.io/ViLBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a deeper understanding of the effectiveness of current vision-language reward models and to pave the way for future improvements in multimodal step-wise evaluation techniques.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Vision-Language Reward Modeling

**Limitations**: Tasks requiring purely visual understanding may not perform well within VILBENCH.

## 💾 Data

**Source**: Multiple vision-language datasets curated for fine-grained step-wise reward evaluation.

**Size**: 600 examples

**Format**: N/A

**Annotation**: Manually filtered using six open-weight vision language models to ensure examples require fine-grained rewards.

## 🔬 Methodology

**Methods**:
- Evaluation on multiple vision-language tasks
- Benchmarking using feedback from vision-language large language models

**Metrics**:
- Accuracy

**Calculation**: Accuracy calculations are based on predicted answers aligned with ground truth.

**Interpretation**: A higher accuracy score indicates better performance of models on tasks requiring fine-grained feedback.

**Baseline Results**: Current VLLMs struggle to achieve above 27.3% accuracy on the benchmark.

**Validation**: Comparison across various models and approaches in terms of accuracy on the benchmark.

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
