# CliniKnote

## 📊 Benchmark Details

**Name**: CliniKnote

**Overview**: CliniKnote is a comprehensive dataset consisting of 1,200 complex doctor-patient conversations paired with their clinical notes, created and curated by medical experts. It aims to provide a valuable resource for training and evaluating models in clinical note generation tasks.

**Data Type**: text

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- MTS-DIALOG
- ACI-BENCH

**Resources**:
- [GitHub Repository](https://github.com/catalwaysright/K-SOAP-GOODLABS.git)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective is to improve clinical note generation efficiency and accuracy using large language models.

**Target Audience**:
- Healthcare Professionals
- ML Researchers

**Tasks**:
- Clinical Note Generation
- Keyword Extraction

**Limitations**: N/A

## 💾 Data

**Source**: Doctor-patient conversations simulated and recorded by medical experts, with clinical notes written by the same experts.

**Size**: 1,200 dialogues

**Format**: JSON

**Annotation**: Curated by medical experts using automatic speech recognition and validated manually with a low word error rate.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- BLEU Score
- ROUGE-L
- BERTScore
- BLEURT
- QuestEval

**Calculation**: Metrics are calculated based on the alignment of generated notes with reference notes using various key performance indicators.

**Interpretation**: Higher scores in metrics indicate better alignment with quality clinical notes.

**Baseline Results**: Results from models like qCammel-13b and GPT-4 were found to achieve significant improvements in generating K-SOAP notes compared to standard methods.

**Validation**: Various evaluations were conducted to assess the quality of generated notes and their applicability in clinical settings.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data is synthesized and does not contain personal health information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
