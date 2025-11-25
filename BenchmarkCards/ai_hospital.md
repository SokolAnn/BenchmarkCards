# AI Hospital

## 📊 Benchmark Details

**Name**: AI Hospital

**Overview**: AI Hospital is a multi-agent framework simulating dynamic medical interactions between doctors and patients, developed to evaluate large language models (LLMs) in clinical diagnosis through the Multi-View Medical Evaluation (MVME) benchmark.

**Data Type**: medical records

**Domains**:
- Healthcare

**Languages**:
- Chinese

**Similar Benchmarks**:
- MedQA
- PubMedQA
- MedMCQA

**Resources**:
- [GitHub Repository](https://github.com/LibertFan/AI_Hospital)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate large language models in the context of clinical diagnosis and improve their performance in multi-turn interactions with patients.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners
- Medical Educators

**Tasks**:
- Clinical Diagnosis
- Symptom Collection
- Examination Recommendation

**Limitations**: The dataset comprises primarily Chinese medical records, which may limit generalizability to other languages and healthcare systems. The sample size of 506 cases may not fully capture complex real-world scenarios.

## 💾 Data

**Source**: Collected Chinese medical records across diverse departments, reviewed by professional physicians.

**Size**: 506 cases

**Format**: N/A

**Annotation**: Manually validated by medical professionals.

## 🔬 Methodology

**Methods**:
- Automated metrics assessment
- Human evaluation

**Metrics**:
- Diagnostic Accuracy
- Treatment Plan Consistency
- Entity Overlap

**Calculation**: Metrics are calculated by comparing the LLM-based doctor reports against expert evaluations using predefined scales and accuracy measures.

**Interpretation**: Higher scores indicate better performance in diagnostic accuracy and treatment recommendations, while lower scores reflect deficiencies in the LLM's clinical reasoning capabilities.

**Baseline Results**: Performance of existing LLMs was compared against an upper bound set by a single-step input to GPT-4.

**Validation**: The AI Hospital framework was validated through experiments using various LLMs such as GPT-3.5 and GPT-4.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The benchmark assesses LLM performance across diverse patient scenarios to identify potential biases in diagnosis.

**Potential Harm**: ['Misdiagnosis due to inadequate patient history collection']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The medical records have been de-identified to protect patient privacy.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
