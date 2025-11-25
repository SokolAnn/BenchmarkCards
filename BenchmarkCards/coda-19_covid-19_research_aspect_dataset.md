# CODA-19 (COVID-19 Research Aspect Dataset)

## 📊 Benchmark Details

**Name**: CODA-19 (COVID-19 Research Aspect Dataset)

**Overview**: This paper introduces CODA-19, a human-annotated dataset that codes the Background, Purpose, Method, Finding/Contribution, and Other sections of 10,966 English abstracts in the COVID-19 Open Research Dataset.

**Data Type**: text (clause-level sentence fragments / text segments labeled with research aspects)

**Domains**:
- Natural Language Processing
- Medical/Biomedical Research

**Languages**:
- English

**Similar Benchmarks**:
- SOLVENT
- CORD-19

**Resources**:
- [Resource](http://CODA-19.org)
- [Resource](https://arxiv.org/abs/2005.02367)
- [Resource](https://covidseer.ist.psu.edu/)

## 🎯 Purpose and Intended Users

**Goal**: To create CODA-19, a human-annotated dataset that codes the Background, Purpose, Method, Finding/Contribution, and Other sections of 10,966 English abstracts in the COVID-19 Open Research Dataset.

**Target Audience**:
- Scientists
- AI and Natural Language Processing researchers
- Machine Learning and model developers

**Tasks**:
- Text Classification
- Sentence-level / Clause-level Research Aspect Classification

**Limitations**: Authors note ambiguity between Purpose and Background leading to mislabeling in some cases. The corpus excludes non-English abstracts, single-sentence abstracts, and abstracts with more than 1,200 tokens (these were filtered out).

## 💾 Data

**Source**: 10,966 abstracts randomly selected from the COVID-19 Open Research Dataset (CORD-19). Each abstract was segmented into sentences and further split into shorter text fragments.

**Size**: 10,966 abstracts; 2,703,174 tokens; 103,978 sentences; 168,286 text segments; released as an 80/10/10 train/validation/test split.

**Format**: N/A

**Annotation**: Crowdsourced via Amazon Mechanical Turk by 248 workers; each abstract annotated by nine different workers; final labels aggregated via majority vote (excluding blocked workers); five-class annotation scheme: Background, Purpose, Method, Finding/Contribution, Other.

## 🔬 Methodology

**Methods**:
- Expert comparison (biomedical expert and computer scientist annotations on a held-out set)
- Inter-annotator agreement measurement (Cohen's kappa via scikit-learn)
- Majority vote aggregation for crowd labels
- Automated baseline evaluation using machine learning models (Linear SVM, Random Forest, Multinomial Naive Bayes, CNN, LSTM, BERT, SciBERT)

**Metrics**:
- Accuracy
- Cohen's kappa
- Precision
- Recall
- F1 Score

**Calculation**: Cohen's kappa computed using scikit-learn. Final crowd labels obtained via majority vote (ties resolved by pre-specified tiebreaker order). Accuracy, precision, recall, and F1 computed by comparing aggregated crowd labels to expert labels. Baseline models trained and validated on the provided 80/10/10 split; model with highest validation score kept for testing.

**Interpretation**: Aggregated crowd labels are considered comparable to expert labels: crowd vs expert label accuracy reported as 82.2% with Cohen's kappa 0.741, while inter-expert accuracy was 85.0% with kappa 0.788. Baseline automatic classifiers show potential (SciBERT performed best), but there remains room for improvement when compared to expert labels.

**Baseline Results**: Aggregated crowd labels: accuracy 82.2% vs expert labels; Cohen's kappa crowd vs expert = 0.741; inter-expert accuracy = 85.0%, inter-expert kappa = 0.788. Baseline model SciBERT achieved 0.749 accuracy (against crowd labels) in Table 5; authors report SciBERT achieved accuracy 0.774 and Cohen's kappa 0.667 when evaluated against the biomedical expert's labels.

**Validation**: Label quality validated by two experts (a biomedical expert and a computer scientist) who annotated the same 129 abstracts; inter-annotator agreement and accuracy metrics computed. Worker quality was monitored in batches; feedback provided and low-quality workers were blocked; ties in majority voting resolved by a specified tiebreaker order.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Workers were required to watch a five-minute training video, complete an interactive tutorial, and sign a consent form as part of the qualification HIT before annotating.

**Compliance With Regulations**: Not Applicable
