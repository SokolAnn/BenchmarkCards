# EXMODD (Explanatory Multimodal Open-Domain Dialogue dataset)

## 📊 Benchmark Details

**Name**: EXMODD (Explanatory Multimodal Open-Domain Dialogue dataset)

**Overview**: EXMODD is a high-quality multimodal dialogue dataset designed to improve models' ability to generate coherent responses while providing explanations for generated dialogues. It addresses the alignment between multimodal inputs and aims to enhance dialogue system performance by fostering contextually consistent responses and minimizing response toxicity.

**Data Type**: dialogue-response pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Image-Chat

**Resources**:
- [GitHub Repository](https://github.com/poplpr/EXMODD)

## 🎯 Purpose and Intended Users

**Goal**: To advance the development of open-domain multimodal dialogue tasks through data construction and improve response generation quality and safety.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Multimodal Dialogue Generation

**Limitations**: N/A

## 💾 Data

**Source**: Generated using the Multimodal Data Construction Framework (MDCF) based on the CLIP model and human dialogues from the Image-Chat dataset.

**Size**: 9,989 dialogue pairs

**Format**: JSON

**Annotation**: Automatically generated with human-designed prompts for quality control.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Coherence
- Distinct-1
- Distinct-2
- Distinct-3
- Toxicity

**Calculation**: Metrics calculated based on comparative evaluations against existing datasets and human assessments.

**Interpretation**: Higher scores in coherence and distinctness indicate superior dialogue quality, while lower scores in toxicity signify safer responses.

**Validation**: Cross-validation using human evaluators assessing diversity, relevance, and fluency of responses.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt leaking
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
