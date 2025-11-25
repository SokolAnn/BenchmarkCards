# PowerPoint Task Completion (PPTC)

## 📊 Benchmark Details

**Name**: PowerPoint Task Completion (PPTC)

**Overview**: The PowerPoint Task Completion (PPTC) benchmark assesses LLMs' ability to create and edit PPT files based on user instructions. It contains 279 multi-turn sessions covering diverse topics and involves hundreds of instructions requiring multi-modal operations.

**Data Type**: multi-turn dialogue sessions

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/gydpku/PPTC)

## 🎯 Purpose and Intended Users

**Goal**: To measure LLMs’ task completion performance within the PowerPoint software.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Multi-turn Dialogue
- Task Completion

**Limitations**: N/A

## 💾 Data

**Source**: Crowdsourced instructions crafted by professional data science engineers familiar with PowerPoint.

**Size**: 279 multi-turn sessions

**Format**: N/A

**Annotation**: Crafted by crowd workers based on established principles and reviewed for clarity and relevance.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Turn-based accuracy
- Session-based accuracy

**Calculation**: Metrics are calculated based on the ratio of correctly completed turns to total turns and correctly completed sessions to overall sessions.

**Interpretation**: Higher accuracy indicates better performance in completing user tasks within PowerPoint.

**Validation**: The benchmark was validated by assessing instruction clarity and relevance, executing provided API sequences, and verifying goal achievement.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Robustness**: Evasion attack

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
