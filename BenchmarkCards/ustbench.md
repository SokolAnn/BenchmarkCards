# USTBench

## 📊 Benchmark Details

**Name**: USTBench

**Overview**: USTBench is the first benchmark designed to evaluate the spatiotemporal reasoning abilities of LLMs as urban agents, supporting various decision-making and prediction tasks in urban environments through structured questions and answers.

**Data Type**: structured question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- STBench
- CityBench
- UrbanPlanBench

**Resources**:
- [GitHub Repository](https://github.com/usail-hkust/USTBench)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate the spatiotemporal reasoning abilities of LLMs as intelligent urban agents for diverse urban applications.

**Target Audience**:
- ML Researchers
- Urban Planners
- Data Scientists
- AI Practitioners

**Tasks**:
- Spatiotemporal Understanding
- Forecasting
- Planning
- Reflection with Feedback

**Limitations**: Intended primarily for evaluation; systematic enhancement methods for LLMs' spatiotemporal reasoning capabilities are underexplored.

## 💾 Data

**Source**: Constructed through diverse urban tasks in UAgentEnv and public datasets across geospatial and traffic data.

**Size**: 62,466 structured QA pairs

**Format**: json

**Annotation**: Automated and manually verified through urban scenario simulations.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Fine-grained evaluation
- Structured question-answering

**Metrics**:
- Accuracy
- F1 Score
- Mean Absolute Percentage Error (MAPE)
- Categorical Accuracy

**Calculation**: Metrics are calculated based on the responses of LLMs to structured QA pairs across the established tasks in a standardized urban environment.

**Interpretation**: Higher accuracy indicates better reasoning abilities in spatiotemporal tasks; specific thresholds may indicate effective adaptation to urban contexts.

**Baseline Results**: Evaluation includes comparison against 13 leading LLMs across various reasoning tasks.

**Validation**: Extensive evaluations conducted through simulations of diverse urban tasks with controlled scenarios.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Safety
- Robustness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: Analyzes urban scenario impacts across different socioeconomic and demographic backgrounds where applicable.

**Potential Harm**: Potential for biases in spatiotemporal reasoning affecting decision outcomes in urban planning and management.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All datasets used are publicly available and do not contain personally identifiable information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
