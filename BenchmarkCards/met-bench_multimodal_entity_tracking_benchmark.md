# MET-Bench (Multimodal Entity Tracking Benchmark)

## 📊 Benchmark Details

**Name**: MET-Bench (Multimodal Entity Tracking Benchmark)

**Overview**: MET-Bench is a multimodal entity tracking benchmark designed to evaluate the ability of vision-language models to track entity states across modalities using structured domains like Chess and the Shell Game.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2502.10886)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the limitations of current models in multimodal entity tracking, particularly focusing on how well they integrate textual and image-based state updates.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Entity Tracking

**Limitations**: The benchmark is restricted to two synthetic domains—Chess and the Shell Game, which may not fully capture the complexity of real-world multimodal reasoning tasks.

## 💾 Data

**Source**: Chess and Shell Game domains, using structured datasets and real game actions for evaluation.

**Size**: Varies based on game configurations and actions.

**Format**: N/A

**Annotation**: Generated sequences of states and actions based on established game rules and state representations.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on the correct tracking of entity states and actions as they are represented textually and visually.

**Interpretation**: Higher accuracy indicates better integration of visual and textual updates; poor performance implies limitations in reasoning across modalities.

**Baseline Results**: Initial performance based on game start configurations for Chess and shell position for Shell Game.

**Validation**: Results are validated through multiple experiments evaluating different models across structured test cases.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**

**Demographic Analysis**: N/A

**Potential Harm**: ['Biases in model performance across different training scenarios and modalities.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Released under the MIT License.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
