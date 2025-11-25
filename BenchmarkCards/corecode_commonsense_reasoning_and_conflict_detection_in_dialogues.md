# CORECODE (Commonsense Reasoning and Conflict Detection in dialogues)

## 📊 Benchmark Details

**Name**: CORECODE (Commonsense Reasoning and Conflict Detection in dialogues)

**Overview**: CORECODE is a dataset that contains abundant commonsense knowledge manually annotated on dyadic dialogues, aimed to evaluate the commonsense reasoning and commonsense conflict detection capabilities of Chinese LLMs through a series of benchmark tasks.

**Data Type**: commonsense knowledge annotations

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- ATOMIC
- CICERO
- Social IQA

**Resources**:
- [GitHub Repository](https://github.com/danshi777/CORECODE)

## 🎯 Purpose and Intended Users

**Goal**: To assess the capability of LLMs in learning and applying commonsense knowledge through a well-annotated dialogue dataset.

**Target Audience**:
- ML Researchers
- Model Developers
- Educational Institutes

**Tasks**:
- Commonsense Knowledge Filling
- Commonsense Knowledge Generation
- Commonsense Conflict Phrase Detection
- Domain Identification
- Slot Identification
- Event Causal Inference

**Limitations**: N/A

## 💾 Data

**Source**: Annotated from NaturalConv and DuLeMon datasets, encompassing multi-turn dialogues.

**Size**: 76,787 annotations from 19,700 dialogues

**Format**: N/A

**Annotation**: Manual annotation by crowdsourced workers following a standardized procedure.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- BLEU Score
- ROUGE-L

**Calculation**: Scoring based on model predictions against annotated ground truth.

**Interpretation**: Higher performance indicates better commonsense reasoning capabilities of LLMs.

**Baseline Results**: Models like ChatGLM2-6B, BLOOMZ-7.1B performed best in evaluated tasks.

**Validation**: Extensive experiments conducted to assess model performance pre- and post-fine-tuning on CORECODE.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
