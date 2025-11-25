# PERSONA MEMbenchmark

## 📊 Benchmark Details

**Name**: PERSONA MEMbenchmark

**Overview**: PERSONA MEMbenchmark features curated user profiles with over 180 simulated user-LLM interaction histories across 15 real-world tasks that require personalization. It evaluates LLM chatbots’ ability to identify suitable responses based on dynamic user profiles in multi-session interactions.

**Data Type**: multi-turn conversations

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- LONG MEMEVAL
- PREFEVAL

**Resources**:
- [GitHub Repository](https://github.com/bowen-upenn/PersonaMem)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLMs’ ability to leverage past interaction history with a user to deliver personalized responses in real-time.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Personalized Recommendations
- User Preference Tracking

**Limitations**: N/A

## 💾 Data

**Source**: Simulated interactions based on constructed user personas and histories.

**Size**: 180 interaction histories

**Format**: N/A

**Annotation**: Generated through a modular data curation pipeline minimizing irrelevant content.

## 🔬 Methodology

**Methods**:
- Automated metrics
- User response selection

**Metrics**:
- Accuracy

**Calculation**: Accuracy calculated based on the model's choice of response in simulated user queries.

**Interpretation**: Assess whether models can select the correct response that aligns with the user's profile state.

**Baseline Results**: Frontier models such as GPT-4.1, o4-mini, GPT-4.5, and others achieving around 50% accuracy overall.

**Validation**: Human evaluations for assessing quality of generated data.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
