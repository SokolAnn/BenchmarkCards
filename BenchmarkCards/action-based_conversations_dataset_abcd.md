# Action-Based Conversations Dataset (ABCD)

## 📊 Benchmark Details

**Name**: Action-Based Conversations Dataset (ABCD)

**Overview**: ABCD is a fully-labeled dataset with over 10K human-to-human dialogues containing 55 distinct user intents requiring unique sequences of actions constrained by policies to achieve task success. It aims to enhance the realism of task-oriented dialogue systems by incorporating procedural, dual-constrained actions.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MultiWOZ

**Resources**:
- [Resource](https://arxiv.org/abs/2104.00783)

## 🎯 Purpose and Intended Users

**Goal**: To study customer service dialogue systems in more realistic settings incorporating procedural requirements and agent guidelines.

**Target Audience**:
- ML Researchers
- Dialogue System Developers

**Tasks**:
- Action State Tracking
- Cascading Dialogue Success

**Limitations**: N/A

## 💾 Data

**Source**: Human-to-human dialogues collected through Expert Live Chat.

**Size**: 10,042 conversations

**Format**: N/A

**Annotation**: Automated annotation based on the provenance of each intent during data generation.

## 🔬 Methodology

**Methods**:
- Baseline models involving large-scale, pre-trained language models
- Expert Live Chat for real-time dialogue collection

**Metrics**:
- Accuracy

**Calculation**: Overall accuracy for Action State Tracking based on correct action reconciliation with agent guidelines.

**Interpretation**: Higher accuracy indicates better model performance in adhering to action sequences and understanding user intents under constraints.

**Baseline Results**: Human evaluation reaches 82.7% accuracy.

**Validation**: Comparison with existing dialogue datasets and progressively evaluating model performance through baseline results.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All agent workers were compensated a fair wage, and their location was determined during the vetting process.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
