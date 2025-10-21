# Human Centered AI for Indian Legal Text Analytics

## 📊 Benchmark Details

**Name**: Human Centered AI for Indian Legal Text Analytics

**Overview**: This paper introduces a novel dataset for Human Centered AI (HCAI) in Legal Text Analytics (LTA), focusing on integrating human expertise to enhance the performance of Large Language Models (LLMs) in legal tasks.

**Data Type**: question-answering pairs, text

**Domains**:
- Natural Language Processing
- Legal

**Languages**:
- English

**Similar Benchmarks**:
- LegalBench

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To enhance the performance of legal text analytics by leveraging human inputs alongside Large Language Models.

**Target Audience**:
- Legal Professionals
- Law Students
- Researchers

**Tasks**:
- Question Answering
- Judgment Summarization
- Petition Drafting
- Case Similarity

**Limitations**: N/A

## 💾 Data

**Source**: Created from scraping the web for court cases, judgements, and other legal documents. Includes human annotations.

**Size**: 2,286 documents, 895,398 sentences, 801,604 triples

**Format**: JSON

**Annotation**: Manually annotated using curated dictionaries.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- ROC-AUC

**Calculation**: Calculating the ROC-AUC score to evaluate model performance on tasks.

**Interpretation**: Higher ROC-AUC scores indicate better predictive performance.

**Baseline Results**: LLaMA-2-70B-Chat yielded a ROC-AUC score of 0.566 on the Case Similarity task.

**Validation**: The performance of models is compared against existing baselines on standard legal tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
