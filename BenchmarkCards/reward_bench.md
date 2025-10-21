# REWARD BENCH

## 📊 Benchmark Details

**Name**: REWARD BENCH

**Overview**: REWARD BENCH is the first toolkit for benchmarking reward models, providing a dataset of prompt-chosen-rejected trios spanning chat, reasoning, and safety, to evaluate how reward models perform on challenging, structured, and out-of-distribution queries.

**Data Type**: prompt-chosen-rejected pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Anthropic Helpful
- MT-Bench
- SHP (Stanford Human Preferences)

**Resources**:
- [Resource](https://hf.co/datasets/allenai/reward-bench)
- [GitHub Repository](https://github.com/allenai/reward-bench)
- [Resource](https://hf.co/spaces/allenai/reward-bench)

## 🎯 Purpose and Intended Users

**Goal**: To enhance scientific understanding of reward models through structured evaluation.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Evaluation of Reward Models

**Limitations**: N/A

## 💾 Data

**Source**: Curated prompt-chosen-rejected trios from various datasets and custom selections.

**Size**: 2,958 examples

**Format**: JSONL

**Annotation**: Manual verification by researchers.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Scores are calculated based on the winning counts of chosen vs rejected pairs.

**Interpretation**: A win is defined as the chosen completion receiving a higher score than the rejected completion for a given prompt.

**Baseline Results**: N/A

**Validation**: Models are evaluated based on their performance on the REWARD BENCH leaderboard.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Privacy**: Personal information in data
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset does not contain personally identifiable information but does address potentially offensive content.

**Data Licensing**: The REWARD BENCH dataset is released under the ODC-BY license and code is under Apache 2.0.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
