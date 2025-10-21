# MATHPILE (A Billion-Token-Scale Pre-training Corpus for Math)

## 📊 Benchmark Details

**Name**: MATHPILE (A Billion-Token-Scale Pre-training Corpus for Math)

**Overview**: MATHPILE is a diverse and high-quality math-centric corpus comprising about 9.5 billion tokens, aimed at boosting language models’ mathematical reasoning abilities.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MATH
- GSM8K
- MMLU-STEM
- AGIEval-SAT-MATH
- MathQA

**Resources**:
- [GitHub Repository](https://github.com/GAIR-NLP/MathPile/)

## 🎯 Purpose and Intended Users

**Goal**: To enhance mathematical reasoning capabilities in language models by providing a diverse, high-quality pre-training corpus focused on mathematics.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Mathematical Problem Solving
- Reasoning Tasks

**Limitations**: The dataset is primarily focused on English, which may limit its applicability in multilingual contexts.

## 💾 Data

**Source**: Generated from various sources including arXiv, textbooks, StackExchange, Wikipedia, ProofWiki, and Common Crawl.

**Size**: 9.5 billion tokens

**Format**: Raw text files

**Annotation**: Includes quality annotations like language identification scores and the ratio of symbols to words.

## 🔬 Methodology

**Methods**:
- Data collection from diverse sources
- Data preprocessing and cleaning
- Data contamination detection

**Metrics**:
- Accuracy

**Calculation**: Performed by evaluating the model's performance on various mathematical reasoning benchmarks after continual pre-training.

**Interpretation**: Improvements in model performance are indicated by increased accuracy on targeted benchmarks.

**Baseline Results**: Mistral-7B model performance improved on several metrics after pre-training.

**Validation**: Continual pre-training experiments using sourced materials demonstrated performance enhancement.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: Data mainly sourced and processed in a manner focused on English documents, lacking multilingual dataset representation.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Measures have been taken to ensure collected data comply with copyright and licensing requirements.

**Data Licensing**: MATHPILE is released under the CC BY-NC-SA 4.0 license.

**Consent Procedures**: Explicit consent not obtained from textbook authors due to the nature of open-source data collection.

**Compliance With Regulations**: Ethical review processes have been adhered to during data collection.
