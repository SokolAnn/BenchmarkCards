# ALIGN X

## 📊 Benchmark Details

**Name**: ALIGN X

**Overview**: ALIGN X is a large-scale dataset containing over 1.3 million personalized preference examples for scalable personalized alignment of large language models, capturing a diverse range of human preferences through user-generated content and behavior.

**Data Type**: preference examples

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- UF-P-4
- PRISM
- P-SOUPS

**Resources**:
- [GitHub Repository](https://github.com/JinaLeejnl/AlignX)

## 🎯 Purpose and Intended Users

**Goal**: To improve the alignment of large language models with diverse human preferences through personalized alignment techniques.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Preference Alignment

**Limitations**: N/A

## 💾 Data

**Source**: User-generated content from large-scale forums, primarily Reddit, along with existing alignment datasets.

**Size**: 1,311,622 examples

**Format**: N/A

**Annotation**: Annotated using a systematic pipeline involving intensity annotation and clustering.

## 🔬 Methodology

**Methods**:
- In-Context Alignment
- Preference-Bridged Alignment

**Metrics**:
- Alignment Accuracy
- GPT-4 Win Rate

**Calculation**: Metrics are calculated based on comparing the log-probability margin of preferred versus less preferred responses.

**Interpretation**: Higher alignment accuracy indicates better adaptation to user preferences.

**Baseline Results**: Outperformed existing LLMs with an average accuracy gain of 17.06%.

**Validation**: Extensive experiments across multiple benchmarks demonstrate robustness and adaptability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data, Data privacy rights alignment

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset was constructed with awareness of privacy concerns, ensuring that user identities remain anonymous.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
