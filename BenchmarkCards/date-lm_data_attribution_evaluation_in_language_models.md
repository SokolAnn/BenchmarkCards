# DATE-LM (Data Attribution Evaluation in Language Models)

## 📊 Benchmark Details

**Name**: DATE-LM (Data Attribution Evaluation in Language Models)

**Overview**: DATE-LM is a unified benchmark for evaluating data attribution methods through real-world LLM applications. It measures attribution quality through training data selection, toxicity/bias filtering, and factual attribution.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/DataAttributionEval/DATE-LM)
- [Resource](https://huggingface.co/DataAttributionEval)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic and scalable evaluation framework for data attribution methods in language models.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Training Data Selection
- Toxicity and Bias Filtering
- Factual Attribution

**Limitations**: N/A

## 💾 Data

**Source**: A diverse set of datasets including UltraChat, ToxicChat, and LAMBADA.

**Size**: 10,000 examples for benign set with <100 examples for unsafe data.

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- AUPRC (Area Under Precision-Recall Curve)
- Recall@50
- Mean Reciprocal Rank (MRR)

**Calculation**: Metrics are calculated based on the results obtained from the evaluation tasks.

**Interpretation**: Higher scores indicate better performance in detecting and filtering data.

**Baseline Results**: N/A

**Validation**: Evaluation across multiple tasks and methods with consistent sampling and evaluation strategies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
