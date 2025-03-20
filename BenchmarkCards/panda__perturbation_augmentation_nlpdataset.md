# PANDA: Perturbation Augmentation NLPDataset

## 📊 Benchmark Details

**Name**: PANDA: Perturbation Augmentation NLPDataset

**Overview**: PANDA is a large-scale dataset of 98,583 human-annotated demographic text perturbations aimed at training neural models to mitigate bias in NLP.

**Data Type**: text

**Domains**:
- NLP
- Natural Language Understanding

**Languages**:
- English

**Similar Benchmarks**:
- CrowS-Pairs
- WEAT
- SEAT

**Resources**:
- [Resource](Dataset available upon request)
- [Resource](PANDA framework model)

## 🎯 Purpose and Intended Users

**Goal**: To explore and evaluate the efficacy of demographic perturbation in NLP for creating fairer language models.

**Target Audience**:
- Researchers in NLP
- AI ethicists
- Developers of language models

**Tasks**:
- Bias measurement in NLP models
- Training fairer language models

**Limitations**: Results may vary across demographics and tasks.

**Out of Scope Uses**:
- Misinformation detection datasets
- Tasks requiring strict factual accuracy

## 💾 Data

**Source**: Sourced from multiple datasets including BookCorpus, SQuAD, and Wikipedia.

**Size**: 98,583 examples

**Format**: Annotated text pairs

**Annotation**: Human-annotated demographic term perturbations

## 🔬 Methodology

**Methods**:
- Neural demographic perturbation
- Controlled text generation

**Metrics**:
- Accuracy on GLUE benchmark tasks
- Fairscore for measuring demographic robustness

**Calculation**: Fairscore is calculated based on changes in model predictions between original and perturbed inputs.

**Interpretation**: A lower fairscore indicates a fairer model.

**Baseline Results**: FairBERTa matched RoBERTa performance with improved fairness scores.

**Validation**: Pilot validation of 125 perturbed instances showed high agreement with original labels.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias in training data
- Misrepresentation of demographic attributes
- Potential for generating counterfactuals

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Data contamination
- **Transparency**: Lack of training data transparency

**Demographic Analysis**: Demographic attributes in PANDA are balanced across axes, with significant attention given to the representation of gender, race/ethnicity, and age.

**Potential Harm**: May generate counterfactual content that does not reflect real individuals accurately.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data does not include personally identifiable information of individuals.

**Data Licensing**: Data sources are selected based on permissive licenses.

**Consent Procedures**: Crowdworkers were compensated fairly and participated voluntarily.

**Compliance With Regulations**: Data collection adheres to relevant labor laws and ethical guidelines.
