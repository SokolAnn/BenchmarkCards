# Counterspeech for Mitigating the Influence of Media Bias

## 📊 Benchmark Details

**Name**: Counterspeech for Mitigating the Influence of Media Bias

**Overview**: The paper introduces a manually annotated dataset linking media bias, offensive comments, and counterspeech, and establishes a benchmark for counterspeech generation.

**Data Type**: offensive comment - counterspeech reply pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- BAT (Bias And Twitter)

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To explore counterspeech generation in the context of media bias and user comments.

**Target Audience**:
- ML Researchers
- Social Media Analysts
- Media Studies Scholars

**Tasks**:
- Counterspeech Generation
- Media Bias Analysis

**Limitations**: N/A

## 💾 Data

**Source**: 853 pairs of offensive comments and their corresponding counterspeech replies manually annotated from news articles.

**Size**: 853 pairs

**Format**: N/A

**Annotation**: Manually annotated by experts and crowdsourced from Amazon Mechanical Turk.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- GLEU
- METEOR
- BERT Score
- Diversity Metrics
- Argument Quality
- Counterspeech Quality
- Toxicity

**Calculation**: Metrics are calculated to evaluate similarity to ground truth, diversity, and the effectiveness of the generated counterspeech.

**Interpretation**: Higher scores indicate greater similarity, diversity, and effectiveness of the counterspeech.

**Validation**: Inter-annotator agreement was measured with Cohen’s Kappa, achieving satisfactory levels.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
