# Tomato, Tomahto, Tomate: Measuring the Role of Shared Semantics among Subwords in Multilingual Language Models

## 📊 Benchmark Details

**Name**: Tomato, Tomahto, Tomate: Measuring the Role of Shared Semantics among Subwords in Multilingual Language Models

**Overview**: This work measures the role of shared semantics among subwords in multilingual language models (mLMs) by forming 'semantic tokens' through merging semantically similar subwords and their embeddings, evaluating these updated mLMs on five downstream tasks across thirty languages.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Arabic
- Bulgarian
- German
- Greek
- Spanish
- French
- Hindi
- Indonesian
- Japanese
- Korean
- Russian
- Swahili
- Thai
- Turkish
- Ukrainian
- Vietnamese
- Hausa
- Igbo
- Kiswahili
- Luganda
- Pidgin

**Similar Benchmarks**:
- MasakhaNER
- XNLI
- TyDi QA
- MIRACL

**Resources**:
- [Resource](https://arxiv.org/abs/2411.04530)

## 🎯 Purpose and Intended Users

**Goal**: To investigate the effectiveness of shared semantics in multilingual language models through semantic tokenization and evaluate its effect on cross-lingual generalization across various tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Language Understanding Researchers

**Tasks**:
- Named Entity Recognition
- Question Answering
- Natural Language Inference
- Information Retrieval

**Limitations**: The work focuses on encoder-only models, limiting the findings to tasks that do not heavily involve pragmatics or require precise semantic understanding such as figurative language.

## 💾 Data

**Source**: Evaluated on 5 heterogeneous multilingual downstream tasks including MasakhaNER, XNLI, TyDi QA, MIRACL, with a focus on cross-lingual semantic tokenization.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Semantic Grouping (SG)
- Cross-lingual Subword Alignment (CLSA)
- Continual Pretraining

**Metrics**:
- F1 Score
- Accuracy
- nDCG@10

**Calculation**: Metrics calculated based on the effectiveness of semantic tokens across different tasks and grouping ratios.

**Interpretation**: The results suggest that using shared subword-level semantics can maintain classification effectiveness even with a significantly reduced vocabulary size.

**Baseline Results**: N/A

**Validation**: Results validated across different models (mBERT, XLM-R) to ensure generalizability of findings.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Analysis of performance is conducted across various languages to explore fairness and bias issues.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
