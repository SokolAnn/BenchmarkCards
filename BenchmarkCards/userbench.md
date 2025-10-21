# UserBench

## 📊 Benchmark Details

**Name**: UserBench

**Overview**: UserBench is a user-centric benchmark designed to evaluate agents in multi-turn, preference-driven interactions in travel planning scenarios, focusing on underspecified goals and incremental preference revelation.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- User Reported Scenarios
- Intention-in-Interaction
- WildBench
- MINT
- PrefEval
- τ-Bench
- τ2-Bench

**Resources**:
- [GitHub Repository](https://github.com/SalesforceAIResearch/UserBench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and facilitate agents' ability to understand, interact with, and adapt to real-world user communication.

**Target Audience**:
- ML Researchers
- AI Practitioners
- Model Developers

**Tasks**:
- Multi-Turn Interaction

**Limitations**: N/A

## 💾 Data

**Source**: Curated travel planning scenarios designed to elicit user preferences dynamically.

**Size**: 4,000+ scenarios

**Format**: N/A

**Annotation**: Carefully curated to reflect realistic user preference expressions through simulations.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Best Exist Rate
- Correct Exist Rate
- Valid Search Attempt (%)
- Valid Action Attempt (%)
- Preference Elicited (%)

**Calculation**: Normalized score based on the quality of selected options and user alignment.

**Interpretation**: Higher scores indicate better alignment with user preferences and successful interactions.

**Validation**: Evaluated across various models to identify strengths and weaknesses in user understanding.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Privacy**: Personal information in data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
