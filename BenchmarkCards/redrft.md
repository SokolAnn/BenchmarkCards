# RedRFT

## 📊 Benchmark Details

**Name**: RedRFT

**Overview**: RedRFT is a lightweight benchmark designed to simplify and standardize the implementation and evaluation of Reinforcement Fine-Tuning (RFT)-based red teaming methods for Large Language Models (LLMs).

**Data Type**: adversarial prompt generation

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TRL (Transformer Reinforcement Learning)
- OpenRLHF
- RL4LMs

**Resources**:
- [GitHub Repository](https://github.com/x-zheng16/RedRFT.git)

## 🎯 Purpose and Intended Users

**Goal**: To standardize and advance RFT-based red teaming methodologies for LLMs by providing a unified framework and implementations.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Text Classification
- Adversarial Prompt Generation

**Limitations**: A primary limitation of this work is the lack of experiments on larger target LLMs, such as those with billions of parameters.

## 💾 Data

**Source**: Various datasets for initial prompts, including IMDB for text continuation and Alpaca for instruction following.

**Size**: 50,000 samples for initial prompts

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Reinforcement Learning
- Proximal Policy Optimization

**Metrics**:
- Cumulative Toxicity-Diversity Score
- Toxicity Score
- Diversity Score

**Calculation**: Metrics are calculated based on the performance of adversarial prompts generated through the red teaming process.

**Interpretation**: Lower scores indicate better performance in terms of balanced toxicity and diversity in generated prompts.

**Baseline Results**: Compared with five state-of-the-art RFT-based red teaming methods, using the same unified PPO backbone.

**Validation**: Performance evaluated through extensive experiments on toxicity and diversity metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Safety

**Atlas Risks**:
- **Fairness**: Output bias
- **Societal Impact**: Impact on education: plagiarism, Impact on affected communities

**Demographic Analysis**: N/A

**Potential Harm**: The process generates adversarial prompts that could elicit toxic or unsafe responses from target LLMs.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
