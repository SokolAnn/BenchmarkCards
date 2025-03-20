# 3D-GRAND

## 📊 Benchmark Details

**Name**: 3D-GRAND

**Overview**: A large-scale, densely-grounded 3D-text dataset designed for grounded 3D instruction tuning, consisting of 40,087 scenes paired with 6.2 million densely-grounded scene-language instructions.

**Data Type**: 3D text data

**Domains**:
- household scenes

**Languages**:
- English

**Similar Benchmarks**:
- 3D-POPE

**Resources**:
- [Resource](https://3d-grand.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To provide essential resources and insights for advancing research in embodied AI through improved 3D language learning models.

**Target Audience**:
- AI researchers
- robotics developers
- ML practitioners

**Tasks**:
- grounded object reference
- 3D grounded scene description
- 3D grounded question answering

**Limitations**: N/A

**Out of Scope Uses**:
- N/A

## 💾 Data

**Source**: 3D-FRONT and Structured3D datasets.

**Size**: 40,087 scenes and 6.2 million instructions.

**Format**: N/A

**Annotation**: Densely-grounded scene-language instructions.

## 🔬 Methodology

**Methods**:
- LLM-based annotation
- Crowdsourced validation

**Metrics**:
- accuracy
- precision
- recall
- F1 score

**Calculation**: Performance evaluated using metrics such as accuracy and F1 score on the 3D-POPE benchmark.

**Interpretation**: Higher scores indicate better grounding and lower hallucination rates.

**Baseline Results**: 3D-GRAND achieved 93.34% precision and 89.12% accuracy in 3D-POPE.

**Validation**: Human validation conducted through crowdsourcing.

## ⚠️ Targeted Risks

**Risk Categories**:
- Data contamination
- Hallucination
- Grounding errors

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
