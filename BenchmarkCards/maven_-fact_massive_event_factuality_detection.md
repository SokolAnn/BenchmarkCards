# MAVEN -FACT (Massive Event Factuality Detection)

## 📊 Benchmark Details

**Name**: MAVEN -FACT (Massive Event Factuality Detection)

**Overview**: MAVEN -FACT is a large-scale event factuality detection dataset containing factuality annotations for 112,276 events. It aims to provide high-quality data for assessing the factuality of textual events and incorporates supporting evidence for improved interpretability.

**Data Type**: event factuality annotations

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/THU-KEG/MAVEN-FACT)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate research in event factuality detection and improve the understanding of event knowledge.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Event Factuality Detection
- Supporting Evidence Prediction

**Limitations**: Language coverage is limited to English, and the annotation approach may introduce noise, although mitigation strategies are in place.

## 💾 Data

**Source**: MAVEN dataset

**Size**: 112,276 events

**Format**: N/A

**Annotation**: Annotated by a combination of LLM pre-annotation followed by human verification, ensuring high quality.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Macro F1 Score

**Calculation**: F1 Score calculated based on precision and recall across multiple factuality categories.

**Interpretation**: Higher F1 scores indicate better performance in distinguishing event factuality.

**Baseline Results**: Best-performing model achieves a 47.6% macro F1 score.

**Validation**: High inter-annotator agreement reported at 96.1%.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: Research indicates potential for reducing hallucination in large language models.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data is collected from public sources and anonymized, with no personal information included.

**Data Licensing**: MAVEN -FACT released under CC BY-SA 4.0 license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
