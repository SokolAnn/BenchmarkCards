# POLYMATH (A Challenging Multi-Modal Mathematical Reasoning Benchmark)

## 📊 Benchmark Details

**Name**: POLYMATH (A Challenging Multi-Modal Mathematical Reasoning Benchmark)

**Overview**: POLYMATH is a benchmark specifically crafted to evaluate the complex multi-modal cognitive reasoning capabilities of Multi-modal Large Language Models (MLLMs) through a dataset of visual and textual challenges.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision
- Education

**Languages**:
- English

**Similar Benchmarks**:
- GeoQA
- MathVista
- MMMU

**Resources**:
- [GitHub Repository](https://github.com/kevinscaria/PolyMATH)
- [Resource](https://huggingface.co/datasets/him1411/polymath)

## 🎯 Purpose and Intended Users

**Goal**: To systematically analyze the mathematical reasoning capabilities of state-of-the-art models in visually complex scenarios.

**Target Audience**:
- ML Researchers
- Model Developers
- Educators

**Tasks**:
- Mathematical Reasoning
- Visual Question Answering
- Cognitive Reasoning

**Limitations**: Although POLYMATH covers a wide range of tasks, some mathematical problems and visual types may be underrepresented.

## 💾 Data

**Source**: Curated from questions directed at students taking the National Talent Search Examination in India.

**Size**: 5,000 questions

**Format**: JSON

**Annotation**: Manually collected and rigorously reviewed by expert annotators.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Metrics are derived based on exact match for answer comparison after applying prompting methods.

**Interpretation**: Higher accuracy indicates better performance of models on the benchmark tasks.

**Baseline Results**: Human performance reached 66.3% accuracy.

**Validation**: Extensive evaluation of various MLLMs across multiple prompting strategies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Fairness

**Atlas Risks**:
- **Accuracy**
- **Robustness**: Evasion attack
- **Fairness**: Output bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
