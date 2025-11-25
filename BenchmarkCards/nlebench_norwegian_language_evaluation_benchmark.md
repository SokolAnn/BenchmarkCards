# NLEBench (Norwegian Language Evaluation Benchmark)

## 📊 Benchmark Details

**Name**: NLEBench (Norwegian Language Evaluation Benchmark)

**Overview**: NLEBench is a comprehensive benchmark for evaluating natural language generation capabilities in Norwegian, encompassing various real-world NLP tasks such as translation and human annotation. It serves to assess the capabilities of generative language models (GLMs) in Norwegian, aiming to fill the existing gap in benchmarks for low-resource languages.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Norwegian

**Resources**:
- [GitHub Repository](https://github.com/Smartmedia-AI/NorGLM)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of NLEBench is to evaluate the generative language modeling capabilities specific to the Norwegian language, including tasks designed to probe the system's understanding of Norwegian culture and language nuances.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Text Generation
- Question Answering
- Summarization
- Natural Language Inference

**Limitations**: While NLEBench is the most comprehensive benchmark for Norwegian, its coverage of applications and downstream tasks remains limited. The scarcity of human-annotated samples and quality control challenges also pose constraints.

## 💾 Data

**Source**: The dataset for NLEBench includes existing datasets, machine translations, and manually annotated datasets specifically designed for Norwegian generative language tasks.

**Size**: 196GB texts

**Format**: N/A

**Annotation**: Data was manually annotated by native Norwegian speakers, with a focus on maintaining quality through a cross-validation process.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Model-based evaluation

**Metrics**:
- BLEU
- ROUGE-1
- ROUGE-L
- Accuracy
- F1 Score

**Calculation**: Metrics like BLEU and ROUGE are computed based on generated and reference texts to evaluate performance across different tasks.

**Interpretation**: Higher scores in BLEU and ROUGE indicate better performance in text generation tasks. Accuracy and F1 Score are interpreted as the measure of correct predictions in classification tasks.

**Baseline Results**: NorGPT-3B model achieves the best results across multiple evaluation metrics in conversation tasks; NB-GPT-J-6B outperforms on summarization metrics.

**Validation**: Validation procedures included evaluation against human-annotated standards and pre-defined quantitative metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Robustness**: Evasion attack, Data poisoning
- **Privacy**: Personal information in data

**Demographic Analysis**: The benchmark includes evaluations to assess biases across different demographic categories.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The resources and code are shared under a CC BY-NC 4.0 license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
