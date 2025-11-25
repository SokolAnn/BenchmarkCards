# MIXCUBE (Mixed Culture Benchmark)

## 📊 Benchmark Details

**Name**: MIXCUBE (Mixed Culture Benchmark)

**Overview**: MIXCUBE is a Mixed Culture Benchmark dataset of 2.5k images of food, festivals, and clothing, labeled with the culture of origin, designed to evaluate cultural bias in multi-modal large language models (MLLMs).

**Data Type**: image

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Azerbaijani
- Korean
- Myanmar

**Similar Benchmarks**:
- Culturally-diverse multilingual visual question answering benchmark

**Resources**:
- [Resource](https://huggingface.co/datasets/kyawyethu/MixCuBe)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the robustness of multi-modal large language models (MLLMs) and their cultural awareness and bias with cross-cultural perturbed data across five cultures.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Country Identification
- Cultural Marker Identification

**Limitations**: N/A

## 💾 Data

**Source**: Images collected via web scraping and manual searches, ensuring cultural markers' authenticity.

**Size**: 2,500 images

**Format**: N/A

**Annotation**: Images are labeled with culture of origin and food names, with generated images vetted through automated and manual checks.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy is quantified based on the model's correctness in identifying the country or cultural markers.

**Interpretation**: Higher accuracy indicates better cultural recognition by the model.

**Baseline Results**: N/A

**Validation**: Models evaluated using both original and synthesized images to assess bias.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: ['Reinforcement of stereotypes', 'Cultural misrepresentation']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
