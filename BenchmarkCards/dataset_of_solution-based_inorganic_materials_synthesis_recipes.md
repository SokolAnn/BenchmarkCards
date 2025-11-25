# Dataset of Solution-based Inorganic Materials Synthesis Recipes

## 📊 Benchmark Details

**Name**: Dataset of Solution-based Inorganic Materials Synthesis Recipes

**Overview**: This paper presents the first large-scale dataset of 35,675 solution-based synthesis 'recipes' extracted from the scientific literature, containing essential synthesis information including the precursors, target materials, their quantities, and the synthesis actions and corresponding attributes.

**Data Type**: synthesis recipes

**Domains**:
- Materials Science

**Languages**:
- English

**Resources**:
- [Resource](https://doi.org/10.6084/m9.figshare.16583387.v1)
- [GitHub Repository](https://github.com/CederGroupHub/text-mined-solution-synthesis_public)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset of solution-based inorganic materials synthesis recipes to enhance data-driven approaches in materials synthesis.

**Target Audience**:
- Materials Scientists
- Data Scientists
- Researchers in Inorganic Chemistry

**Tasks**:
- Materials Synthesis Analysis
- Data-Driven Materials Discovery

**Limitations**: N/A

## 💾 Data

**Source**: Scientific literature, specifically articles downloaded from major publishers after the year 2000.

**Size**: 35,675 recipes

**Format**: JSON

**Annotation**: Manual and automatic extraction techniques using advanced NLP and ML models.

## 🔬 Methodology

**Methods**:
- Information extraction pipeline
- NLP techniques for material entity recognition
- Machine learning for synthesis action extraction

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics were calculated based on the accuracy of extraction against a manually curated validation set.

**Interpretation**: Higher scores indicate better performance of the data extraction methods.

**Baseline Results**: F1 scores for key fields exceed 90%

**Validation**: Validation through manual inspection of 100 entries.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
