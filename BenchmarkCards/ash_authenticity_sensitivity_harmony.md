# ASH (Authenticity, Sensitivity, Harmony)

## 📊 Benchmark Details

**Name**: ASH (Authenticity, Sensitivity, Harmony)

**Overview**: The ASH benchmark evaluates LLMs’ culinary creativity in the cuisine transfer task by assessing the cultural accuracy and creativity of generated recipes.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/dmis-lab/CulinaryASH/)

## 🎯 Purpose and Intended Users

**Goal**: To assess LLMs' abilities in generating culturally adapted recipes through the cuisine transfer task.

**Target Audience**:
- ML Researchers
- Culinary Experts

**Tasks**:
- Text Generation

**Limitations**: The evaluation may not comprehensively represent all perspectives within culinary domains.

## 💾 Data

**Source**: Created standardized cuisine transfer instructions based on various cuisines and dishes.

**Size**: 4,800 recipes

**Format**: JSON

**Annotation**: Rated by LLM evaluators and human annotators for authenticity, sensitivity, and harmony.

## 🔬 Methodology

**Methods**:
- Automated evaluation
- Human evaluation

**Metrics**:
- Authenticity
- Sensitivity
- Harmony

**Calculation**: Average ratings calculated for each criterion across all generated recipes.

**Interpretation**: Higher scores indicate better adherence to the criteria of authenticity, sensitivity, and overall recipe quality.

**Baseline Results**: N/A

**Validation**: Evaluators' agreement scores calculated to assess evaluation consistency.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: ['Misrepresentation of cultural practices']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Implemented evaluation criteria to prioritize authenticity and sensitivity.

**Data Licensing**: Not Applicable

**Consent Procedures**: Participants in evaluations provided consent to participate.

**Compliance With Regulations**: Not Applicable
