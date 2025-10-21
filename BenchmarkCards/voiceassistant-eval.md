# VoiceAssistant-Eval

## 📊 Benchmark Details

**Name**: VoiceAssistant-Eval

**Overview**: VoiceAssistant-Eval is a comprehensive benchmark designed to assess AI assistants across listening, speaking, and viewing, comprising 10,497 curated examples spanning 13 task categories.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Education
- Human-Computer Interaction

**Languages**:
- English

**Similar Benchmarks**:
- VoiceBench
- VocalBench
- SOVA-Bench
- SD-Eval
- AIR-Bench
- MMM-U

**Resources**:
- [Resource](https://arxiv.org/abs/2509.22651)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the full range of capabilities of voice assistants across multiple modalities, facilitating the development of next-generation AI assistants.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Listening
- Speaking
- Viewing

**Limitations**: It may carry biases from the source data and design choices. The dataset may still be limited in diversity.

## 💾 Data

**Source**: Diverse visual and auditory inputs extracted from 47 datasets.

**Size**: 10,497 examples

**Format**: JSON

**Annotation**: Manual annotation and curation involving multi-stage processes for data quality.

## 🔬 Methodology

**Methods**:
- Evaluation using human scoring
- Automated metrics

**Metrics**:
- Content quality
- Speech quality
- Consistency between modalities

**Calculation**: Metrics are calculated based on scorer evaluations across various dimensions.

**Interpretation**: Higher scores indicate better performance in listening, speaking, and multimodal comprehension.

**Validation**: Validated through human evaluators and alignment testing.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Exposing personal information
- **Accuracy**: Poor model accuracy
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Measures are in place to anonymize sensitive data during the evaluation process.

**Data Licensing**: The dataset is under an MIT license for research purposes.

**Consent Procedures**: Strict consent and provenance procedures are followed for dataset collection.

**Compliance With Regulations**: In accordance with local data protection regulations.
