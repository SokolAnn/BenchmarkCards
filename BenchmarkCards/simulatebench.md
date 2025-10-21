# SimulateBench

## 📊 Benchmark Details

**Name**: SimulateBench

**Overview**: SimulateBench is designed to evaluate the believability of large language models (LLMs) when simulating human behaviors. It assesses LLMs based on two dimensions: consistency and robustness, utilizing 65 character profiles and 8,400 questions.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/user/repo)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the believability of LLMs in simulating human behaviors through the dimensions of consistency and robustness.

**Target Audience**:
- ML Researchers
- AI Developers

**Tasks**:
- Behavior Simulation Evaluation

**Limitations**: Some commercial models may not be included due to access restrictions.

## 💾 Data

**Source**: Profiles collected from TV dramas and character descriptions from fandoms.

**Size**: 8,400 questions

**Format**: N/A

**Annotation**: Data verified by human annotators after extensive training.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Consistency Accuracy (CA)
- Robustness Average (RA)
- Coefficient of Variation for Robustness (RCoV)

**Calculation**: Metrics are calculated based on the LLMs' responses to questions assessing consistency and robustness under perturbation.

**Interpretation**: Higher CA indicates better consistency; RA and RCoV reflect the impact of perturbations on robustness.

**Baseline Results**: Not specified

**Validation**: Data validation performed by human annotators to ensure accurate profiling.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**

**Demographic Analysis**: Believability can be influenced by demographic factors in the character profiles.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Ensured well-being of annotators during data collection.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
