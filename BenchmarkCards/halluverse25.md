# HalluVerse25

## 📊 Benchmark Details

**Name**: HalluVerse25

**Overview**: HalluVerse25 is a fine-grained multilingual LLM hallucination dataset that categorizes fine-grained hallucinations in English, Arabic, and Turkish, providing insight into how well proprietary models perform in detecting LLM-generated hallucinations.

**Data Type**: sentence pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Arabic
- Turkish

**Similar Benchmarks**:
- HaluEval
- Halwasa

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset that categorizes fine-grained hallucination types across multiple languages and to advance research on LLM hallucination detection.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Hallucination Detection

**Limitations**: The dataset is collected based on the availability of biographical information hosted on Wikidata and Wikipedia, which may not represent an accurate distribution of individuals in the world.

## 💾 Data

**Source**: Data was extracted from Wikidata and Wikipedia to create factual sentences which are then modified to inject hallucinations.

**Size**: 3,116 examples

**Format**: N/A

**Annotation**: Human-annotated by native speakers with a substantial annotation agreement.

## 🔬 Methodology

**Methods**:
- Automated hallucination injection via LLM
- Human evaluation for data quality

**Metrics**:
- Accuracy

**Calculation**: Models were evaluated based on their ability to correctly classify different types of hallucinations in the dataset.

**Interpretation**: Higher accuracy indicates better performance in detecting hallucinations of different types.

**Baseline Results**: GPT-4 demonstrated the highest overall accuracy, especially in identifying entity and relation hallucinations.

**Validation**: The dataset was validated through a human annotation process with substantial inter-annotator agreement.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
