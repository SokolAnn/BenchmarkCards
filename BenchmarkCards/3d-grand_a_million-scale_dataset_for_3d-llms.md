# 3D-GRAND (A Million-Scale Dataset for 3D-LLMs)

## 📊 Benchmark Details

**Name**: 3D-GRAND (A Million-Scale Dataset for 3D-LLMs)

**Overview**: 3D-GRAND is a pioneering large-scale dataset comprising 40,087 household scenes paired with 6.2 million densely-grounded scene-language instructions designed for grounded 3D instruction tuning.

**Data Type**: scene-language instruction pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- SceneVerse

**Resources**:
- [Resource](https://3d-grand.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large-scale, densely-grounded 3D-text dataset for improving the performance of 3D language models in understanding and interacting with the physical world.

**Target Audience**:
- Researchers in Embodied AI
- ML Researchers
- Model Developers

**Tasks**:
- Object Reference
- Scene Description
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Curated from synthetic 3D scenes including 3D-FRONT and Structured3D datasets.

**Size**: 40,087 scenes and 6.2 million annotations

**Format**: N/A

**Annotation**: Densely-grounded text annotations generated using a hallucination filter and validated by humans.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated based on the responses of 3D-LLMs to questions about the presence of objects in 3D scenes.

**Interpretation**: Higher precision and accuracy indicate better performance in grounding.

**Baseline Results**: 3D-LLM, LEO, and 3D-VisTA were compared as baseline models.

**Validation**: Validated through extensive human quality checks with a sample size of 5,100 annotations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
