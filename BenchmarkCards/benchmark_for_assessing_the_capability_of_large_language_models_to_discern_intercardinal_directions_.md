# Benchmark for Assessing the Capability of Large Language Models to Discern Intercardinal Directions Between Geographic Locations

## 📊 Benchmark Details

**Name**: Benchmark for Assessing the Capability of Large Language Models to Discern Intercardinal Directions Between Geographic Locations

**Overview**: This benchmark evaluates the capability of Large Language Models (LLMs) to discern intercardinal directions between American cities, investigating whether LLMs exhibit hierarchical spatial bias similar to humans.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Geography

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To assess the capability of Large Language Models (LLMs) in spatial reasoning and discernment of intercardinal directions influenced by hierarchical biases.

**Target Audience**:
- ML Researchers
- Geographers
- AI Practitioners

**Tasks**:
- Spatial Reasoning
- Geographic Information Processing

**Limitations**: The benchmark primarily focuses on well-known American cities, which may limit the generalizability of results to less-documented locations.

## 💾 Data

**Source**: 14 questions on intercardinal directions among well-known American cities designed for the benchmark.

**Size**: 14 questions

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Evaluating responses of LLMs to formulated questions

**Metrics**:
- Accuracy

**Calculation**: Performance metrics were calculated based on the accuracy of model responses to the direction questions.

**Interpretation**: Higher accuracy indicates better discernment of intercardinal directions and less influence from hierarchical spatial biases.

**Baseline Results**: GPT-4 achieved 55.3% overall accuracy, followed by GPT-3.5 at 47.3% and Llama-2 at 44.7%.

**Validation**: The benchmark was validated through testing on prominent models and analysis of the patterns in their responses.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential reinforcement of hierarchical spatial biases in model outputs.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
