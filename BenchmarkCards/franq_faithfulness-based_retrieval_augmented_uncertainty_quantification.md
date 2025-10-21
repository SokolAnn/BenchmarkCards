# FRANQ (Faithfulness-based Retrieval Augmented Uncertainty Quantification)

## 📊 Benchmark Details

**Name**: FRANQ (Faithfulness-based Retrieval Augmented Uncertainty Quantification)

**Overview**: FRANQ is a novel method for hallucination detection in Retrieval-Augmented Generation (RAG) outputs, which evaluates factuality based on whether a statement is faithful to the retrieved context.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- RAGTruth

**Resources**:
- [Resource](https://arxiv.org/abs/2505.21072)

## 🎯 Purpose and Intended Users

**Goal**: To improve the detection of factual errors in Retrieval-Augmented Generation (RAG) outputs and provide a dataset for evaluating such methods.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: New long-form QA dataset annotated for both factuality and faithfulness, combining automated labeling with manual validation.

**Size**: 500 claims for training and 1282 for testing in long-form QA dataset; 200 questions for training and 1000 for testing in short-form QA dataset.

**Format**: N/A

**Annotation**: Automated annotation followed by manual validation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- ROCAUC
- PR-AUC
- PRR

**Calculation**: Metrics are calculated using binary gold-standard factuality labels compared with predicted values to evaluate model performance across multiple datasets.

**Interpretation**: Higher scores indicate better performance in identifying factual inaccuracies and recognizing claims.

**Baseline Results**: Compared against XGBoost and other UQ methods.

**Validation**: Validation was conducted using a combination of automatic annotation and manual review of claims.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
