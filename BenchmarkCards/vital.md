# VITAL

## 📊 Benchmark Details

**Name**: VITAL

**Overview**: VITAL is a new benchmark dataset comprising 13.1K value-laden situations and 5.4K multiple-choice questions focused on health, designed to assess and benchmark pluralistic alignment methodologies.

**Data Type**: value-laden situations and multiple-choice questions

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- OPINION QA
- GLOBAL OPINION QA
- MPI

**Resources**:
- [GitHub Repository](https://github.com/anudeex/VITAL.git)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the pluralistic alignment of LLMs specifically within the health domain.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners
- AI Developers

**Tasks**:
- Health-based Question Answering
- Moral Decision Making

**Limitations**: The benchmark may not encompass all health-related perspectives and values.

## 💾 Data

**Source**: Various surveys, polls, and moral scenario datasets focused on health.

**Size**: 13,601 samples

**Format**: Multiple-choice format and qualitative text

**Annotation**: Semi-automatically filtered and confirmed with human validation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy
- Jensen-Shannon Distance
- NLI Coverage

**Calculation**: Metrics are calculated based on alignment performance comparisons using standard evaluation techniques.

**Interpretation**: Higher values indicate better performance in aligning with pluralistic values.

**Validation**: Human validation confirmed the relevance and health-related nature of 80% of analyzed samples.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: The dataset aims to reflect diverse health beliefs and values across different demographic groups.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
