# Atypical Aspect-based Recommender System (ATARS)

## 📊 Benchmark Details

**Name**: Atypical Aspect-based Recommender System (ATARS)

**Overview**: This paper introduces a new task of engineering serendipity in recommendations by promoting items with atypical aspects that match user interests. It presents an LLM-based system that extracts atypical aspects from reviews, estimates their user-specific utility, and ranks items to enhance user satisfaction through surprise and relevance.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU (Massive Multitask Language Understanding)
- SQuAD
- GLUE

**Resources**:
- [GitHub Repository](https://github.com/ramituncc49er/ATARS)

## 🎯 Purpose and Intended Users

**Goal**: To develop a recommender system that enhances user satisfaction by promoting items with atypical aspects that generate serendipitous experiences.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Recommendation Systems
- Information Extraction

**Limitations**: N/A

## 💾 Data

**Source**: Yelp reviews dataset containing approximately 5 million restaurant reviews, 190k hotel reviews, and 115k hair salon reviews.

**Size**: 5 million reviews

**Format**: JSON

**Annotation**: Manual annotation by experts and crowd-sourced utility value annotations.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- F1 Score
- Recall
- Precision

**Calculation**: Metrics were calculated based on the correlation between system-generated rankings and ground truth rankings for serendipity-based recommendations.

**Interpretation**: Higher scores indicate better alignment with user preferences and expectations, while lower scores suggest a mismatch between recommendations and user interests.

**Baseline Results**: Baseline models were evaluated against standard rankings without atypical aspect considerations.

**Validation**: Validation procedures involved assessing the correlation of the developed recommendation metrics against established benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Fairness

**Atlas Risks**:
- **Fairness**: Output bias
- **Privacy**: Data privacy rights alignment

**Demographic Analysis**: None

**Potential Harm**: ['Exposing personal information', 'Spreading disinformation', 'Ethical risks related to user-specific data manipulation']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: User data is handled according to community guidelines; specific privacy policies were not disclosed in the paper.

**Data Licensing**: The datasets are publicly available but specific licensing details were not mentioned.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
