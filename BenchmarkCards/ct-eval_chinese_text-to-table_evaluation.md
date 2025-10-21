# CT-Eval (Chinese Text-to-Table Evaluation)

## 📊 Benchmark Details

**Name**: CT-Eval (Chinese Text-to-Table Evaluation)

**Overview**: CT-Eval is a Chinese text-to-table dataset designed to benchmark large language models (LLMs) on the task of generating structured tables from unstructured documents, ensuring data diversity and minimizing hallucination issues.

**Data Type**: text-table pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Resources**:
- [Resource](https://huggingface.co/THUDM/chatglm3-6b-32k)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark large language models on Chinese text-to-table tasks and improve their performance.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Text-to-Table

**Limitations**: While human cleaning is applied in validation and test sets, the training set still contains hallucination issues.

## 💾 Data

**Source**: Baidu Baike (a popular Chinese multidisciplinary online encyclopedia)

**Size**: 88,603 examples

**Format**: N/A

**Annotation**: Human annotation combined with LLM hallucination judging to clean the data.

## 🔬 Methodology

**Methods**:
- Zero-shot evaluation
- Fine-tuning

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated based on the number of correct non-header cells in the predicted tables compared to the ground truth.

**Interpretation**: Higher precision and recall indicate a better ability in extracting and structuring the information.

**Baseline Results**: GPT-4 serves as a baseline, achieving the best zero-shot performance.

**Validation**: Traditional metrics evaluation against human judgment and LLM-generated outputs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Data from Baidu Baike is authorized for academic usage.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
