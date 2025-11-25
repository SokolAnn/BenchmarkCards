# GermanPartiesQA

## 📊 Benchmark Details

**Name**: GermanPartiesQA

**Overview**: GermanPartiesQA is a benchmark dataset developed to evaluate political biases and sycophancy in large language models by assessing their alignment with the positions of major German political parties based on data from the Voting Advice Application Wahl-o-Mat.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- German

**Resources**:
- [GitHub Repository](https://github.com/Weizenbaum-Institut/GermanPartiesQA)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and compare the alignment of large language models with German party positions and to assess their sycophancy.

**Target Audience**:
- ML Researchers
- Policy Makers
- Political Analysts

**Tasks**:
- Political Bias Evaluation
- Sycophancy Assessment

**Limitations**: N/A

## 💾 Data

**Source**: Data was collected from the Voting Advice Application Wahl-o-Mat covering 10 state and 1 national elections in Germany between 2021 and 2023.

**Size**: 418 political statements

**Format**: CSV

**Annotation**: Automatically generated based on official responses from political parties.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Prompt experiments

**Metrics**:
- Alignment Score

**Calculation**: Alignment scores are calculated based on the responses of the LLMs to the political statements compared to official party responses.

**Interpretation**: Higher alignment scores indicate closer alignment with the respective political party positions.

**Validation**: The benchmark is validated by testing responses against known party positions and conducting prompt experiments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The dataset includes sociodemographic data of parliament members to assess context-specific biases.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset uses publicly available information about parliament members.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
