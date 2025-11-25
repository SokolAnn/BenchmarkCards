# NIFTY Financial News Headlines Dataset

## 📊 Benchmark Details

**Name**: NIFTY Financial News Headlines Dataset

**Overview**: The NIFTY dataset is designed to facilitate and advance research in financial market forecasting using large language models (LLMs). It includes two versions tailored for different modeling approaches: NIFTY-LM, for supervised fine-tuning of LLMs; and NIFTY-RL, formatted for alignment methods to align LLMs via rejection sampling and reward modeling.

**Data Type**: text

**Domains**:
- Finance

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/NIFTY)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate and advance research in financial market forecasting using large language models.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Stock Movement Prediction

**Limitations**: N/A

## 💾 Data

**Source**: Aggregated high-quality news headlines and market data from various sources.

**Size**: 2,111 examples

**Format**: JSONL

**Annotation**: Headlines ranked and filtered based on their relevance to financial topics.

## 🔬 Methodology

**Methods**:
- Supervised Fine-Tuning
- Reinforcement Learning

**Metrics**:
- Accuracy
- F1 Score
- Precision
- Recall

**Calculation**: Metrics calculated based on prediction accuracy of stock movement labels (Rise, Fall, Neutral).

**Interpretation**: Higher accuracy indicates better performance in predicting stock movement.

**Baseline Results**: N/A

**Validation**: Data split into train (1,477), validation (317), and test (317) sets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness

**Atlas Risks**:
- **Fairness**
- **Robustness**

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
