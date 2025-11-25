# AraDiCE

## 📊 Benchmark Details

**Name**: AraDiCE

**Overview**: AraDiCE is a benchmark for Arabic Dialect and Cultural Evaluation, consisting of seven synthetic datasets in dialects and Modern Standard Arabic (MSA) to evaluate LLMs on dialect comprehension and generation.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Arabic

**Similar Benchmarks**:
- ArabicMMLU

**Resources**:
- [Resource](https://huggingface.co/datasets/QCRI/AraDiCE)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark Arabic LLMs on their understanding of dialectal Arabic and cultural knowledge across the Gulf, Egyptian, and Levant regions.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Dialect Identification
- Dialect Generation
- Cultural Understanding
- Cognitive Abilities Assessment

**Limitations**: Limited coverage of Arabic dialects; primarily focused on Levant, Gulf, and Egyptian dialects.

## 💾 Data

**Source**: Synthetic datasets generated using Machine Translation and human post-editing.

**Size**: ≈45,000 post-edited samples

**Format**: JSON

**Annotation**: Manual annotation by expert native speakers.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Accuracy
- SacreBLEU

**Calculation**: Metrics calculated based on human evaluation and established NLP benchmarks.

**Interpretation**: Higher scores indicate better performance in dialect comprehension and generation tasks.

**Baseline Results**: Compared against existing Arabic LLMs such as Jais and AceGPT.

**Validation**: Results validated through testing on multiple Arabic dialect benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
