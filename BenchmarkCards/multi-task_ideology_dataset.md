# Multi-task Ideology Dataset

## 📊 Benchmark Details

**Name**: Multi-task Ideology Dataset

**Overview**: A multi-task dataset reflecting the nuanced differences between the ideologies of Progressive-Left, Left-Wing, Center, Right-Wing, and Conservative-Right. This dataset includes tasks of Question-Answering, Manifesto Cloze Completion, Ideological Statement Ranking, and Congress Bill Comprehension to capture diverse political viewpoints.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/dpasch01/llm-nuanced-ideologies)

## 🎯 Purpose and Intended Users

**Goal**: To assess how LLMs can adopt and express nuanced political ideologies through fine-tuning on political data.

**Target Audience**:
- ML Researchers
- Model Developers
- Political Analysts

**Tasks**:
- Question Answering
- Ideological Statement Ranking
- Manifesto Cloze Completion
- Bill Comprehension

**Limitations**: N/A

## 💾 Data

**Source**: Data was collected from publicly available sources like OnTheIssues.org for political statements and GovTrack.us for ideological mapping.

**Size**: 250,760 statements

**Format**: JSONL

**Annotation**: The dataset has been annotated based on political alignment determined using ideology scores derived from political statements.

## 🔬 Methodology

**Methods**:
- Fine-tuning LLMs
- Evaluation using statement ranking and positioning tests

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on model performance across various tasks, comparing predicted ideological positions against actual ideological scores.

**Interpretation**: Higher scores indicate better alignment of LLMs with the intended political ideology, while lower scores point to discrepancies.

**Baseline Results**: N/A

**Validation**: Validation of results performed through comparison with existing political ideology mapping frameworks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
