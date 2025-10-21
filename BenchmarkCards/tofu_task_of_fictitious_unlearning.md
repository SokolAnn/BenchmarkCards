# TOFU (Task of Fictitious Unlearning)

## 📊 Benchmark Details

**Name**: TOFU (Task of Fictitious Unlearning)

**Overview**: TOFU is a benchmark aimed at helping deepen our understanding of unlearning in large language models by providing a dataset of 200 diverse synthetic author profiles, each consisting of 20 question-answer pairs, and a suite of metrics for evaluating unlearning efficacy.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/locuslab/TOFU)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to evaluate the efficacy of unlearning algorithms in large language models.

**Target Audience**:
- ML Researchers
- AI Practitioners

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Dataset of 200 diverse synthetic author profiles generated using GPT-4, each with 20 question-answer pairs focused on fictitious authors.

**Size**: 200 profiles with 4,000 question-answer pairs

**Format**: JSON

**Annotation**: Automatically generated

## 🔬 Methodology

**Methods**:
- Evaluation against baseline unlearning algorithms
- Statistical tests for forget quality

**Metrics**:
- Truth Ratio
- ROUGE-L

**Calculation**: Metrics are computed for both the forget set and the retain set to compare the performance of unlearned models to models that have never been trained on the forget set.

**Interpretation**: A high p-value in statistical tests indicates strong forgetting; ROUGE and Truth Ratio capture the performance on respective datasets.

**Baseline Results**: Existing unlearning algorithms do not show effective unlearning, suggesting a need for improved methods.

**Validation**: Ordered evaluation across metrics measuring both forget quality and model utility.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data is synthetic, minimizing risks of privacy violations.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
