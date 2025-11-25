# DischargeSim

## 📊 Benchmark Details

**Name**: DischargeSim

**Overview**: DischargeSim is a novel benchmark that evaluates large language models (LLMs) on their ability to act as personalized discharge educators through simulated post-visit conversations.

**Data Type**: dialogue simulations

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- AgentClinic
- AMIE
- HealthBench

**Resources**:
- [GitHub Repository](https://github.com/michaels6060/DischargeSim)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and improve the discharge education capabilities of large language models in post-visit clinical education.

**Target Audience**:
- ML Researchers
- Healthcare Professionals
- Model Developers

**Tasks**:
- Patient Education
- Dialogue Generation
- Evaluation of Discharge Communication

**Limitations**: N/A

## 💾 Data

**Source**: MIMIC-IV dataset

**Size**: 49 discharge notes

**Format**: JSON

**Annotation**: Manual generation of multiple-choice questions by experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- LLM-based evaluations

**Metrics**:
- Dialogue quality
- Personalized summary generation
- Patient comprehension

**Calculation**: Metrics calculated include linguistic clarity, coherence, and factual accuracy based on human references.

**Interpretation**: Scores indicate the effectiveness of the LLMs in facilitating patient education during discharge.

**Baseline Results**: Various LLMs were benchmarked, revealing performance variation across different models.

**Validation**: Evaluated by both LLMs and clinicians against established clinical benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: Evaluation includes patient profiles based on health literacy, education, and emotional states.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data derived from de-identified public datasets with no personal information.

**Data Licensing**: CC-BY-NC 4.0 license

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
