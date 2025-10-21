# CONVERSATION CHRONICLES

## 📊 Benchmark Details

**Name**: CONVERSATION CHRONICLES

**Overview**: CONVERSATION CHRONICLES is a new high-quality long-term conversation dataset, implementing chronological dynamics by integrating time intervals and speaker relationships into multi-session dialogues. It consists of 1M dialogues across 200K episodes.

**Data Type**: multi-session dialogues

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MSC (Multi-Session Conversations)

**Resources**:
- [Resource](https://conversation-chronicles.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To enhance conversational AI systems by providing a dataset that captures long-term dialogue dynamics through enhanced temporal and relational understanding.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Dialogue Generation

**Limitations**: The research was conducted with a limited number of specific time intervals and speaker relationships, which could limit the generalizability of the findings.

## 💾 Data

**Source**: Constructed using refined prompts to LLMs based on an event graph linking related events.

**Size**: 1,000,000 dialogues

**Format**: N/A

**Annotation**: Automated generation using large language models, specifically ChatGPT.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated generation using LLMs

**Metrics**:
- Engagingness
- Humanness
- Memorability

**Calculation**: Metrics are calculated based on human evaluator ratings on the quality of dialogues.

**Interpretation**: Higher scores indicate more engaging and human-like dialogue.

**Baseline Results**: Compared against existing datasets like MSC.

**Validation**: Extensive human evaluations to ensure dialogue coherence and relevance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Safety

**Atlas Risks**:
- **Fairness**: Output bias
- **Privacy**: Personal information in data
- **Societal Impact**: Impact on education: plagiarism

**Demographic Analysis**: N/A

**Potential Harm**: Potential generation of harmful or biased dialogue outputs.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Care taken to filter potential toxic data; however, the model may still generate undesirable responses.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
