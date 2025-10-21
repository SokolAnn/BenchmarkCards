# Shopping MMLU (Massive Multi-task Online Shopping Benchmark for Large Language Models)

## 📊 Benchmark Details

**Name**: Shopping MMLU (Massive Multi-task Online Shopping Benchmark for Large Language Models)

**Overview**: Shopping MMLU is a diverse multi-task online shopping benchmark derived from real-world Amazon data, consisting of 57 tasks that evaluate large language models on their abilities as shop assistants across various shopping skills.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- German
- Spanish
- French
- Italian
- Japanese

**Similar Benchmarks**:
- EComInstruct
- ECInstruct

**Resources**:
- [GitHub Repository](https://github.com/KL4805/ShoppingMMLU)
- [Resource](https://amazon-kddcup24.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of Shopping MMLU is to facilitate the development of LLM-based solutions for comprehensive multi-task modeling of online shopping.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- User Behavior Alignment
- Shopping Knowledge Reasoning
- Shopping Concept Understanding
- Multi-lingual Abilities

**Limitations**: N/A

## 💾 Data

**Source**: Derived from real-world Amazon data, including product catalogs, reviews, browse sessions, and queries, with some tasks synthesized using Claude 2.

**Size**: 20,799 questions

**Format**: N/A

**Annotation**: Data has been manually inspected for quality control to ensure validity.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Hit rate@3
- Normalized Discounted Cumulative Gain (NDCG)
- Micro F1
- ROUGE-L
- BLEU Score

**Calculation**: Various metrics calculated based on task type, e.g. accuracy for multiple choice, hit rate for retrieval tasks, and ROUGE-L for generation tasks.

**Interpretation**: Higher scores indicate better performance on corresponding tasks.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All identifiers have been removed to ensure anonymity.

**Data Licensing**: Apache 2.0.

**Consent Procedures**: Data usage approved by the Amazon legal team.

**Compliance With Regulations**: Not Applicable
