# MIRAI (Multi-Information Fo Recasting Agent Interface)

## 📊 Benchmark Details

**Name**: MIRAI (Multi-Information Fo Recasting Agent Interface)

**Overview**: MIRAI is a novel benchmark designed to systematically evaluate LLM agents as temporal forecasters in the context of international events, assessing their abilities to source and integrate critical information, write codes for tool-use, and predict future events.

**Data Type**: event forecasting records

**Domains**:
- Natural Language Processing
- International Relations

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/yecchen/MIRAI)
- [Resource](https://drive.google.com/file/d/1xmSEHZ_wqtBu1AwLpJ8wCDYmT-jRpfrN/view?usp=sharing)

## 🎯 Purpose and Intended Users

**Goal**: To establish a reliable framework for assessing the capabilities of LLM agents in forecasting international events.

**Target Audience**:
- Researchers in Natural Language Processing
- Political Analysts
- Data Scientists

**Tasks**:
- Event Forecasting
- Temporal Reasoning

**Limitations**: The current study is limited by the small number of tested LLMs and basic API functionality. Future iterations could enhance the API and incorporate more models.

## 💾 Data

**Source**: GDELT event database curated through extensive cleaning and parsing to form relational prediction tasks.

**Size**: 991,759 examples

**Format**: CSV

**Annotation**: Textual information extracted from news articles and events processed to eliminate noise.

## 🔬 Methodology

**Methods**:
- LLM agent performance evaluation
- Code generation for API interaction

**Metrics**:
- F1 Score
- Precision
- Recall

**Calculation**: Metrics are calculated by comparing predicted relation codes against ground truth relation codes.

**Interpretation**: Higher F1 Scores indicate better predictive accuracy, with precision and recall providing insights into model reliability.

**Validation**: Results validated through comprehensive benchmarking across various LLM agents using real-world political event data.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Safety

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY-NC 4.0 license for non-commercial use with attribution.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
