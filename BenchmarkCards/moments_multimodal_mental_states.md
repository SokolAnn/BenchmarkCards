# MOMENTS (Multimodal Mental States)

## 📊 Benchmark Details

**Name**: MOMENTS (Multimodal Mental States)

**Overview**: MOMENTS is a comprehensive benchmark designed to assess the Theory of Mind capabilities of multimodal large language models through realistic, narrative-rich scenarios presented in short films. The benchmark includes over 2,300 multiple-choice questions spanning seven distinct Theory of Mind categories.

**Data Type**: multiple-choice questions

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Russian
- Spanish
- French
- Persian
- Italian
- Arabic
- Swedish
- Korean
- Danish
- Hindi
- Japanese

**Resources**:
- [GitHub Repository](https://github.com/villacu/MoMentS)
- [Resource](https://arxiv.org/abs/2507.04415)

## 🎯 Purpose and Intended Users

**Goal**: To support the development of socially intelligent multimodal agents and assess current models’ Theory of Mind in realistic, socially grounded scenarios.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Social Scientists

**Tasks**:
- Question Answering

**Limitations**: The benchmark uses a multiple-choice QA format, limiting analysis of lower-level behavioral cues. Additionally, it relies on static video data which does not account for dynamic interactions.

## 💾 Data

**Source**: Short films sourced from the SF20K dataset (YouTube channel Omeleto).

**Size**: 2,335 questions across 168 short films

**Format**: JSON

**Annotation**: Human-annotated with multiple-choice questions.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on the percentage of correctly answered questions out of the total questions.

**Interpretation**: Higher accuracy indicates better performance in understanding Theory of Mind through context.

**Validation**: Piloted with multiple rounds of quality checks and peer reviews.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Societal Impact**: Impact on affected communities

**Potential Harm**: Ensuring the dataset is used ethically to mitigate risks related to manipulation and deception.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Questions do not contain personally identifying information.

**Data Licensing**: CC BY-NC-SA 4.0 license for academic research purposes only.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
