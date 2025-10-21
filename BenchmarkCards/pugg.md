# PUGG

## 📊 Benchmark Details

**Name**: PUGG

**Overview**: We introduce the PUGG dataset, which encompasses three tasks — KBQA, MRC, and IR. This dataset features natural factoid questions in Polish and stands out as the first Polish KBQA resource.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Polish

**Similar Benchmarks**:
- N/A

**Resources**:
- [Resource](https://huggingface.co/datasets/clarin-pl/PUGG)
- [GitHub Repository](https://github.com/CLARIN-PL/PUGG)

## 🎯 Purpose and Intended Users

**Goal**: To address the significant resource gap for low-resource languages by creating a KBQA dataset for Polish, alongside datasets for MRC and IR.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Knowledge Base Question Answering
- Machine Reading Comprehension
- Information Retrieval

**Limitations**: The natural questions are open domain, focused on location and time, and are created and answered from the Polish cultural, political, and historical perspective.

## 💾 Data

**Source**: Constructed through a semi-automated pipeline utilizing Wikidata as the knowledge graph.

**Size**: 5,593 examples

**Format**: N/A

**Annotation**: Involves human verification alongside semi-automated processes.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Accuracy is calculated as the proportion of answers included in the model’s response for each question.

**Interpretation**: Higher accuracy indicates better performance in answering the questions correctly.

**Baseline Results**: Base accuracy for natural KBQA questions is 0.275 and improves with the use of knowledge graphs.

**Validation**: The datasets were validated using human verification.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: The dataset includes questions that reflect Polish culture and society.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY-SA 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
