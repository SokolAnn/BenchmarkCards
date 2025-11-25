# Name of Thrones: Evaluating How LLMs Rank Student Names, Race, and Gender in Status Hierarchies

## 📊 Benchmark Details

**Name**: Name of Thrones: Evaluating How LLMs Rank Student Names, Race, and Gender in Status Hierarchies

**Overview**: This study conducts a large-scale analysis with bootstrap standard errors of 45,000 name variations across 5 ethnicities to examine how AI-generated responses exhibit systemic name biases, investigating the effects of names on perceived competence, leadership, and economic potential.

**Data Type**: name variations

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- English

**Similar Benchmarks**:
- SODAPOP

**Resources**:
- [Resource](https://arxiv.org/abs/2504.10797)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate whether LLMs sort students into status positions based on ethnicity and gender associated with their names and to investigate the potential biases in AI assessments.

**Target Audience**:
- ML Researchers
- Educators
- Policy Makers

**Tasks**:
- Bias Evaluation
- Status Ranking

**Limitations**: The study includes only five ethnicities and considers only two genders.

## 💾 Data

**Source**: National delegates of academic and music competitions and frequently occurring names in population databases.

**Size**: 45,000 unique name variations

**Format**: N/A

**Annotation**: Names verified by native speakers from each cultural background.

## 🔬 Methodology

**Methods**:
- Quantitative analysis
- Ordinary least squares regression
- Bootstrap resampling

**Metrics**:
- Predicted academic scores
- Predicted leadership potential
- Predicted wages

**Calculation**: Regression analysis to quantify the model's implicit biases based on demographic attributes.

**Interpretation**: Higher predicted scores indicate perceived higher competence and leadership potential.

**Baseline Results**: LLMs showed variations in predicted scores based on names, with East Asian names often ranked highest.

**Validation**: Bootstrapping with 1,000 replications to enhance robustness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: Names associated with different racial and gender groups showed distinct biases in the predictions.

**Potential Harm**: ['Reinforcing social hierarchies', 'Discrimination based on name biases']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Anonymity of name bearers was upheld by not publishing the dataset publicly.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
