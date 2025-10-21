# Biased Tales

## 📊 Benchmark Details

**Name**: Biased Tales

**Overview**: Biased Tales is a comprehensive dataset designed to analyze how biases influence protagonists’ attributes and story elements in LLM-generated children's stories, particularly examining cultural and gender stereotypes.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MirrorStories

**Resources**:
- [GitHub Repository](https://github.com/donya-rooein/biased_tales)

## 🎯 Purpose and Intended Users

**Goal**: To analyze and measure biases in LLM-generated children's stories incorporating various sociocultural factors.

**Target Audience**:
- Research Community
- Parents
- Educators

**Tasks**:
- Bias Analysis
- Narrative Analysis

**Limitations**: The Biased Tales dataset focuses only on English stories and a limited number of sociocultural factors.

## 💾 Data

**Source**: Stories were generated from various prompts incorporating different sociocultural factors using three LLMs.

**Size**: 5,531 stories

**Format**: JSON

**Annotation**: Manual annotation by human experts and automated annotation using GPT-4.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Toxicity Score
- Lexical Complexity

**Calculation**: Calculating average scores for toxicity and complexity based on established methodologies.

**Interpretation**: Lower scores in toxicity and higher scores in readability indicate a more suitable story for children.

**Baseline Results**: Toxicity Score: 0.06; Average lexical complexity metrics suggest suitability for children.

**Validation**: Sample validation conducted through human annotation and automated checks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Analysis of protagonist attributes and contextual settings based on sociocultural factors.

**Potential Harm**: ['Reinforcing harmful stereotypes', "Limitations on children's understanding of diversity"]

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
