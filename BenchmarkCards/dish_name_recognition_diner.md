# DIsh NamE Recognition (DINER)

## 📊 Benchmark Details

**Name**: DIsh NamE Recognition (DINER)

**Overview**: DINER is a compositional generalization task involving dish name recognition from recipes, aimed at evaluating the capacity to comprehend and create new combinations of observed components, leveraging a large-scale realistic dataset of Chinese recipes.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/Jumpy-pku/DiNeR)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate natural language understanding ability under compositional generalization settings through the Dish Name Recognition task.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Dish Name Recognition

**Limitations**: N/A

## 💾 Data

**Source**: Based on the XIACHUFANG Recipe Dataset consisting of 1,550,151 real-world recipes

**Size**: 223,581 recipes

**Format**: N/A

**Annotation**: Manual parsing and cleaning of dish names and recipes.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Exact Match Accuracy

**Calculation**: The F1 score is calculated based on the micro F1-score of predicted components against the golden components, allowing for partial credit depending on component recognition contributions.

**Interpretation**: Higher F1 scores indicate better performance, especially in identifying correct components of dish names.

**Baseline Results**: T5 + Continual Pretraining: F1 score of 59.2% on TMCD splits; GPT-3.5: F1 score of 52.9% on annotated test set.

**Validation**: Validation is conducted through TMCD splits against training data.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: ['Risk of model bias towards certain dish types due to uneven representation in recipe data.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
