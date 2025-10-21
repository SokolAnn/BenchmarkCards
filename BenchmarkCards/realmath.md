# REALMATH

## 📊 Benchmark Details

**Name**: REALMATH

**Overview**: REALMATH is a novel benchmark for evaluating the mathematical capabilities of Large Language Models (LLMs) using authentic research-level mathematics tasks sourced from research papers and forums. It assesses LLMs' performance on mathematical tasks that represent real-world scenarios, as opposed to conventional competition problems.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Mathematics

**Languages**:
- English

**Similar Benchmarks**:
- FrontierMath

**Resources**:
- [GitHub Repository](https://github.com/username/repo)
- [Resource](https://huggingface.co/datasets/REALMATH)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the mathematical capabilities of LLMs on tasks relevant to contemporary mathematical practice.

**Target Audience**:
- ML Researchers
- Mathematicians
- Industry Practitioners

**Tasks**:
- Mathematical Reasoning
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Research papers from arXiv and Mathematics Stack Exchange.

**Size**: 633 high-quality samples curated from approximately 9,000 academic papers.

**Format**: N/A

**Annotation**: Automatically generated question-answer pairs based on extracted mathematical statements.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation
- Model-based evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on the proportion of correct answers provided by LLMs against ground truth answers.

**Interpretation**: Higher accuracy indicates better performance of models on real-world mathematical tasks.

**Baseline Results**: Leading models achieved accuracy rates of 43-49% on Math.arXiv papers.

**Validation**: Models were validated using multiple datasets from Math.arXiv and Stack Exchange.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
