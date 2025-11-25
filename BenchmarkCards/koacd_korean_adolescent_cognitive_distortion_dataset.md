# KoACD (Korean Adolescent Cognitive Distortion Dataset)

## 📊 Benchmark Details

**Name**: KoACD (Korean Adolescent Cognitive Distortion Dataset)

**Overview**: KoACD is a large-scale dataset of cognitive distortions in Korean adolescents, comprising 108,717 instances. It includes diverse data generated through multi-LLM negotiation methods for better context-dependent reasoning in cognitive distortion classification.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- Korean

**Resources**:
- [GitHub Repository](https://github.com/cocoboldongle/KoACD)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset for the detection and analysis of cognitive distortions among Korean adolescents, facilitating targeted interventions in mental health.

**Target Audience**:
- ML Researchers
- Mental Health Professionals
- Education Specialists

**Tasks**:
- Text Classification

**Limitations**: Potential overlaps between different cognitive distortions; some classifications may be challenging for both models and human raters.

## 💾 Data

**Source**: Collected from the NA VER Knowledge iN platform, focusing on questions relevant to adolescent mental health.

**Size**: 108,717 instances

**Format**: JSON

**Annotation**: Data was refined and annotated through multi-LLM negotiation and independent expert evaluation.

## 🔬 Methodology

**Methods**:
- Multi-LLM negotiation
- Expert evaluation

**Metrics**:
- Consistency
- Accuracy
- Fluency

**Calculation**: Metrics are calculated based on evaluations by both LLMs and human experts across various samples.

**Interpretation**: Higher scores in consistency and accuracy indicate better representation and classification of cognitive distortions.

**Baseline Results**: The dataset's performance compared to existing benchmarks was determined through expert evaluations.

**Validation**: Validated against expert review and independent LLM classifications.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Potential Harm**: ['Potential underrepresentation of certain cognitive distortions leading to biased mental health interventions.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All users' data was anonymous and publicly accessible, complying with regulatory standards.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
