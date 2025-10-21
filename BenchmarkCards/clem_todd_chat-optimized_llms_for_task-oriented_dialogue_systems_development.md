# clem:todd (chat-optimized LLMs for task-oriented dialogue systems development)

## 📊 Benchmark Details

**Name**: clem:todd (chat-optimized LLMs for task-oriented dialogue systems development)

**Overview**: clem:todd is a framework for systematically evaluating dialogue systems under consistent conditions, enabling benchmarking across user simulators and dialogue systems.

**Data Type**: conversation logs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MultiWOZ

**Resources**:
- [GitHub Repository](https://github.com/clp-research/clem-todd)

## 🎯 Purpose and Intended Users

**Goal**: Systematic evaluation of LLM-based task-oriented dialogue systems.

**Target Audience**:
- ML Researchers
- Dialogue System Developers
- Industry Practitioners

**Tasks**:
- Task-Oriented Dialogue Evaluation

**Limitations**: The user simulator may not always accurately reflect human behavior.

## 💾 Data

**Source**: MultiWOZ 2.2 dataset and synthetic datasets for unseen goals.

**Size**: 1,000 dialogues for the evaluation set (117 tasks filtered for booking actions)

**Format**: JSON

**Annotation**: Automatically extracted from dialogue interactions.

## 🔬 Methodology

**Methods**:
- Dialogue Evaluation
- Task Success Measurement
- User Simulator Assessment

**Metrics**:
- Inform
- Booking Accuracy
- Naturalness
- Coherence
- Dialogue Diversity

**Calculation**: Metrics are calculated by comparing outputs with ground-truth data in the MultiWOZ test set.

**Interpretation**: Higher scores indicate better performance on metrics like task completion and dialogue quality.

**Validation**: The framework was validated by re-evaluating existing dialogue systems.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack

**Demographic Analysis**: User simulator effectiveness varies across user models.

**Potential Harm**: Potential for low task completion rates with underperforming user simulators.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
