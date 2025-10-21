# UHG Eval (Unconstrained Hallucination Generation Evaluation)

## 📊 Benchmark Details

**Name**: UHG Eval (Unconstrained Hallucination Generation Evaluation)

**Overview**: The benchmark assesses hallucinations produced by Chinese large language models (LLMs) through an unconstrained generation methodology, allowing for the evaluation of freely generated hallucinations in line with real-world applications.

**Data Type**: hallucination text

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- TruthfulQA
- HaluEval
- HaDes

**Resources**:
- [Resource](https://iaar-shanghai.github.io/UHGEval/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the reliability and hallucination capabilities of Chinese large language models by providing a comprehensive and unconstrained benchmark.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Hallucination Detection

**Limitations**: The dataset may contain labeling errors due to the human annotation process.

## 💾 Data

**Source**: Historical news articles from leading Chinese news websites collected for constructing the dataset.

**Size**: 5,141 hallucinated continuations

**Format**: JSON

**Annotation**: Initial automatic labeling followed by human rechecking to ensure accuracy.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Discriminative evaluation
- Selective evaluation
- Generative evaluation

**Metrics**:
- Accuracy
- BLEU Score
- ROUGE-L
- kwPrec
- BERTScore

**Calculation**: Metrics are calculated using lexical and semantic evaluations based on text similarity to reference information.

**Interpretation**: Higher scores in accuracy metrics indicate better model performance in detecting hallucinations.

**Baseline Results**: Comparative evaluation results across multiple LLMs provided in the experimental section.

**Validation**: Results validated against human annotations and through various evaluative methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: The dataset includes a diverse set of news categories aimed at enhancing generalizability.

**Potential Harm**: The benchmark aims to prevent misinformation propagation through improved model outputs.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collected from publicly available news sources with respectful handling of sensitive information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
