# LeetCodeDataset

## 📊 Benchmark Details

**Name**: LeetCodeDataset

**Overview**: We introduce LeetCodeDataset, a high-quality benchmark for evaluating and training code-generation models, addressing two key challenges in LLM research: the lack of reasoning-focused coding benchmarks and self-contained training testbeds.

**Data Type**: programming problems

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- HumanEval
- MBPP
- LiveCodeBench
- APPS
- CodeContests
- TACO

**Resources**:
- [Resource](https://huggingface.co/datasets/newfacade/LeetCodeDataset)
- [GitHub Repository](https://github.com/newfacade/LeetCodeDataset)

## 🎯 Purpose and Intended Users

**Goal**: To provide a reliable, contamination-free model evaluation and highly efficient training dataset for code-generation models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Code Generation

**Limitations**: The dataset lacks extremely complex input patterns and suffers from an imbalanced test case distribution.

## 💾 Data

**Source**: Curated from the LeetCode platform, covering over 90% of Python problems.

**Size**: 2,869 problems

**Format**: N/A

**Annotation**: Annotated with rich metadata including difficulty levels, release dates, and topic tags.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Pass Rate

**Calculation**: Metrics are calculated based on the model's performance on the LeetCodeDataset test set.

**Interpretation**: Higher pass rates indicate better performance of the model on the coding tasks.

**Baseline Results**: Comparative results of models like GPT-4o, Claude-3.7 Sonnet, and DeepSeek-R1 are provided.

**Validation**: Evaluations are done on models leveraging temporal splits of the dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Privacy**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
