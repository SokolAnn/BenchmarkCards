# ProfileBench

## 📊 Benchmark Details

**Name**: ProfileBench

**Overview**: ProfileBench is an industry-derived benchmark from a large-scale video platform, encompassing heterogeneous user data and a systematic profiling taxonomy, enabling standardized evaluation for user profiling tasks.

**Data Type**: user profiling data

**Domains**:
- Natural Language Processing

**Languages**:
- N/A

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standardized benchmark for evaluating label-free user profiling approaches using heterogeneous user data.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- User Profiling

**Limitations**: Limited to six core dimensions; currently lacks fine-grained user attribute capture.

## 💾 Data

**Source**: Derived from a large-scale video platform, includes user-generated behavioral and demographic cues.

**Size**: 1,000 samples

**Format**: Structured data

**Annotation**: Human-annotated through standardized questionnaires.

## 🔬 Methodology

**Methods**:
- Confidence-weighted voting
- Unsupervised reinforcement learning

**Metrics**:
- F1 Score
- Precision
- Recall

**Calculation**: Metrics are calculated based on multi-dimensional predictions against the curated gold standard.

**Interpretation**: Higher values in F1 Score indicate better overall performance in user profiling.

**Baseline Results**: CONF-PROFILE achieves an average F1 of 73.03, outperforming several SOTA models.

**Validation**: Extensive experiments validated the effectiveness of the CONF-PROFILE framework.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data collected were from users who explicitly consented to their information being used for research. Personally identifiable information was anonymized prior to processing.

**Data Licensing**: Not Applicable

**Consent Procedures**: User consent obtained prior to data collection.

**Compliance With Regulations**: The study followed ethical research guidelines and ensured compliance with privacy standards.
