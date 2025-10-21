# Stated Preference for Interaction and Continued Engagement (SPICE)

## 📊 Benchmark Details

**Name**: Stated Preference for Interaction and Continued Engagement (SPICE)

**Overview**: SPICE is a diagnostic signal elicited by asking a Large Language Model a YES/NO question about its willingness to re-engage with a user’s behavior after reviewing a short transcript. It differentiates responses based on user tone and offers insights into the model's disposition toward interactions.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/wooohoooo/SPICE)

## 🎯 Purpose and Intended Users

**Goal**: To provide a reproducible diagnostic for evaluating a model's willingness to re-engage in conversation, helping in auditing and comparative analysis of models.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Interactive Evaluation

**Limitations**: The scope of this work is constrained by the limited stimulus set, model selection, and deterministic decoding.

## 💾 Data

**Source**: Created from 30 unique interactions across three user tones: abusive, unclear, and friendly, provided to four models.

**Size**: 480 trials

**Format**: CSV

**Annotation**: Responses were parsed as 'YES' or 'NO'; additional analysis was based on model outputs.

## 🔬 Methodology

**Methods**:
- Dependence-aware statistical tests including Rao-Scott adjustment and cluster permutation tests

**Metrics**:
- Proportion of YES responses (P(SPICE = YES))

**Calculation**: SPICE responses were calculated based on the ratio of YES to total responses for each tone.

**Interpretation**: Higher SPICE values indicate a stronger preference for continuing interactions.

**Validation**: Robustness of results confirmed through multiple dependence-aware statistical tests.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Decision bias

**Demographic Analysis**: Exploratory analysis revealed significant user tone effects.

**Potential Harm**: ['Misinterpretation of abusive vs. non-abusive tones may lead to harmful interactions.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Interactions include abusive user messages curated by authors; no human participants were involved.

**Data Licensing**: Available under Creative Commons Attribution 4.0 International (CC BY 4.0)

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
