# CulturalRecipes

## 📊 Benchmark Details

**Name**: CulturalRecipes

**Overview**: CulturalRecipes is a unique dataset comprised of automatically paired recipes written in Mandarin Chinese and English, introduced to support the task of cultural adaptation of recipes between these two languages.

**Data Type**: recipe pairs

**Domains**:
- Culinary Arts

**Languages**:
- Chinese
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2310.17353)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate cross-cultural recipe adaptation through a dataset that pairs recipes in Chinese and English, enabling the training and evaluation of language models for this task.

**Target Audience**:
- ML Researchers
- Culinary Experts
- Language Scientists

**Tasks**:
- Recipe Adaptation
- Machine Translation

**Limitations**: N/A

## 💾 Data

**Source**: RecipeNLG and XiaChuFang datasets, paired recipes matched from these sources.

**Size**: 44,500 training examples and 82 silver test examples

**Format**: N/A

**Annotation**: Automatically paired with a human-curated test set.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- BLEU
- ROUGE-L
- ChrF
- BERTScore

**Calculation**: Metrics are calculated based on overlap and representation between generated and reference recipes.

**Interpretation**: Higher scores on metrics indicate better adaptation quality.

**Baseline Results**: N/A

**Validation**: The dataset is evaluated on both automatic metrics and through human judgment.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Quality

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
