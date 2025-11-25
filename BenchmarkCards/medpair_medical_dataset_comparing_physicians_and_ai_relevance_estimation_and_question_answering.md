# MedPAIR (Medical Dataset Comparing Physicians and AI Relevance Estimation and Question Answering)

## 📊 Benchmark Details

**Name**: MedPAIR (Medical Dataset Comparing Physicians and AI Relevance Estimation and Question Answering)

**Overview**: MedPAIR is a dataset designed to evaluate how physician trainees and large language models prioritize relevant information when answering medical question-answering (QA) questions. It includes 1,300 QA pairs with sentence-level relevance annotations from 36 physician trainees, allowing comparison between human and model relevance assessments.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- MMLU (Massive Multitask Language Understanding)
- MedQ (Medical Question Answering)

**Resources**:
- [Resource](http://medpair.csail.mit.edu/)

## 🎯 Purpose and Intended Users

**Goal**: To establish a rigorous pre-reasoning evaluation by quantifying sentence-level relevance alignment between LLMs and physician trainees in medical QA tasks.

**Target Audience**:
- Medical Researchers
- AI/ML Researchers
- Healthcare Practitioners

**Tasks**:
- Question Answering

**Limitations**: The dataset is limited to the medical domain and requires expert labels for relevance, which may not be feasible for all clinical scenarios.

## 💾 Data

**Source**: The data is sourced from four existing QA benchmark datasets: MMLU (Precision Medicine), JAMA Clinical Challenge, MedBullets, and MedXpertQA, with additional annotations from physician trainees.

**Size**: 2,000 question-answer pairs

**Format**: JSON

**Annotation**: Annotations were performed by 36 physician trainees who labeled each sentence as 'High Relevance', 'Low Relevance', or 'Irrelevant'.

## 🔬 Methodology

**Methods**:
- Manual evaluation by experts
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Calculating sentence relevance labels through majority voting among annotators and assessing model performance before and after pruning contexts based on relevance.

**Interpretation**: Performance is measured by the degree of accuracy improvements when irrelevant and low-relevance context is removed based on human annotations.

**Baseline Results**: The baseline accuracy for LLMs before filtering contextual information ranged from 30% to 95.6%, with significant improvements observed after applying relevance filtering.

**Validation**: Validation was conducted through comparison of annotated relevance with model-assigned relevance labels.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Societal Impact

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: Analysis includes the breakdown of participants by demographics, providing insights into the expertise level of the annotators.

**Potential Harm**: ['Potential disparities in model performance across different demographic groups.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The dataset is publicly available under an open access license, details of which are provided alongside resource links.

**Consent Procedures**: Consent was obtained from all human annotators involved in the study.

**Compliance With Regulations**: The study received IRB approval (IRB2411001474) exempting it from further review based on specified criteria.
