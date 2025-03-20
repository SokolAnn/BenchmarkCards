# WILDHALLUCINATIONS

## 📊 Benchmark Details

**Name**: WILDHALLUCINATIONS

**Overview**: WILDHALLUCINATIONS evaluates the factuality of large language models (LLMs) using entities mined from real-world user-chatbot conversations. It automatically fact-checks the generation of information about these entities using a curated knowledge source.

**Data Type**: Entities and text generations

**Domains**:
- computing
- culture
- finance
- geography
- science
- people
- personal attributes

**Languages**:
- English

**Similar Benchmarks**:
- ExpertQA
- HaluEval-Wild
- FACTSCORE

**Resources**:
- [Resource](https://huggingface.co/datasets/wentingzhao/WildHallucinations)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the factual accuracy of LLMs in generating information about real-world entities.

**Target Audience**:
- Researchers
- Model developers
- Practitioners

**Tasks**:
- Evaluating LLM factuality
- Understanding LLM hallucination behaviors

**Limitations**: Focuses only on English entities and cannot cover multilingual contexts.

**Out of Scope Uses**:
- Evaluating LLMs in languages other than English
- Using for non-factual tasks

## 💾 Data

**Source**: WildChat dataset

**Size**: 7,917 entities

**Format**: Web documents and text

**Annotation**: Automatically fact-checked using FACTSCORE.

## 🔬 Methodology

**Methods**:
- Entity extraction using GPT-3.5 and GPT-4o
- Knowledge source building using Google Custom Search
- Automatic fact-checking with FACTSCORE

**Metrics**:
- WILDFACTSCORE
- WILDFACTSCORE-STRICT

**Calculation**: WILDFACTSCORE computes the percentage of atomic facts supported by a knowledge source.

**Interpretation**: Higher WILDFACTSCORE indicates better factual accuracy.

**Baseline Results**: Not available

**Validation**: Validation performed on a sampled dataset for accuracy.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Transparency

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Transparency**: Lack of training data transparency

**Demographic Analysis**: Analysis based on the distribution of entities from user queries.

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Compliance with data privacy regulations of user-generated content.

**Data Licensing**: Entities extracted from WildChat, which is released under ODC-By license.

**Consent Procedures**: User interactions are sourced from the WildChat dataset.

**Compliance With Regulations**: Not Applicable
