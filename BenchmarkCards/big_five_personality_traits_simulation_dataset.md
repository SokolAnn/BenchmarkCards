# Big Five Personality Traits Simulation Dataset

## 📊 Benchmark Details

**Name**: Big Five Personality Traits Simulation Dataset

**Overview**: The paper presents a dataset of generated texts reflecting the Big Five personality traits. It also develops an analytical framework for testing large language models in simulating personality skills.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/mary-silence/simulating_personality)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for evaluating the ability of LLMs to simulate personality traits using the Big Five model.

**Target Audience**:
- ML Researchers
- AI Developers
- Psychologists

**Tasks**:
- Text Generation
- Personality Simulation

**Limitations**: The study is limited by the usage of the Big Five personality model and the impact of LLM size and training data.

## 💾 Data

**Source**: Generated texts based on prompts aligned with the Big Five personality model.

**Size**: 1,015,342 questionnaire answers

**Format**: JSON

**Annotation**: Manually annotated by human evaluators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automatic evaluation
- Linguistic analysis

**Metrics**:
- Cronbach's alpha
- Weighted Precision
- Weighted Recall
- F1 Score

**Calculation**: Metrics calculated using human annotations and automatic evaluations based on classifier performance.

**Interpretation**: Higher scores indicate better simulation of personality traits based on LLM responses.

**Baseline Results**: Results showed varied performance across different LLMs in simulating personality traits based on the Big Five model.

**Validation**: Validation of results included reliability tests and comparisons between human annotators and classifier outputs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: The paper does not provide demographic breakdowns for the dataset.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
