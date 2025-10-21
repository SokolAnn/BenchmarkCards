# Multimodal dataset for bias detection

## 📊 Benchmark Details

**Name**: Multimodal dataset for bias detection

**Overview**: This research introduces a new, manually-annotated multi-modal dataset compiled from Reddit, X (formerly Twitter), news articles, and city council meeting minutes across 10 U.S. cities to identify and track social biases against people experiencing homelessness.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- OATH-Frames

**Resources**:
- [GitHub Repository](https://github.com/Homelessness-Project/Multimodal-PEH-Classification)
- [Resource](https://zenodo.org/records/16877412)

## 🎯 Purpose and Intended Users

**Goal**: To alleviate homelessness by acting on public opinion, raising awareness about the pervasive bias against people experiencing homelessness, and developing new indicators to inform policy.

**Target Audience**:
- ML Researchers
- Policy Makers
- Social Scientists

**Tasks**:
- Bias Detection

**Limitations**: The geographic scope is confined to 10 U.S. cities and may not encompass all available dialogue on homelessness.

## 💾 Data

**Source**: Data collected from Reddit, X (formerly Twitter), news articles, and city council meeting minutes.

**Size**: over 40,000 entities

**Format**: N/A

**Annotation**: Manually annotated by three human annotators using defined categories, with a high agreement rate averaging 78.38%.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score

**Calculation**: Macro- and micro-average F1 scores calculated for various categories.

**Interpretation**: Findings indicate differences in bias prevalence across cities and media types.

**Baseline Results**: Humans achieved an agreement rate averaging 78.38% per category.

**Validation**: Models were validated against a gold standard dataset created through manual annotation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Societal Impact

**Atlas Risks**:
- **Fairness**: Data bias
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: The dataset does not specifically include demographic breakdowns.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data anonymized using spaCy to remove personally identifiable information.

**Data Licensing**: Not Applicable

**Consent Procedures**: IRB approval was obtained for scraping public data.

**Compliance With Regulations**: Not Applicable
