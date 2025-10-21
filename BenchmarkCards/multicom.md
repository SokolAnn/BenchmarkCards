# MULTICOM

## 📊 Benchmark Details

**Name**: MULTICOM

**Overview**: MULTICOM is a benchmark dataset for commonsense generation that extends the COCOTEROS dataset to encompass four different languages: English, Spanish, Dutch, and Valencian. The task involves generating a commonsensical sentence that includes a given triplet of words.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Spanish
- Dutch
- Valencian

**Similar Benchmarks**:
- CommonGen
- COCOTEROS

**Resources**:
- [Resource](https://huggingface.co/datasets/gplsi/MULTICOM)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the multilingual commonsense generation capabilities of Large Language Models (LLMs).

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Commonsense Generation

**Limitations**: N/A

## 💾 Data

**Source**: Extended existing COCOTEROS dataset, translated into multiple languages.

**Size**: 15,500 examples in total across four languages (3,875 training examples, 3,876 test examples).

**Format**: N/A

**Annotation**: Generated and manually reviewed for commonsense logic.

## 🔬 Methodology

**Methods**:
- Automatic metrics
- LLM-as-a-judge evaluations
- Human evaluation

**Metrics**:
- BERTScore
- Cosine Similarity
- Dependency Parsing with Levenshtein Distance
- Human rating

**Calculation**: Metrics calculated based on similarities between generated sentences and reference sentences.

**Interpretation**: Higher scores indicate better commonsense reasoning capabilities.

**Baseline Results**: Results for LLaMA model reported; other models also evaluated.

**Validation**: Tested on multiple language models to ensure reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
