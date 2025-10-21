# X-WebAgentBench: A Multilingual Interactive Web Benchmark for Evaluating Global Agentic System

## 📊 Benchmark Details

**Name**: X-WebAgentBench: A Multilingual Interactive Web Benchmark for Evaluating Global Agentic System

**Overview**: X-WebAgentBench is a novel multilingual agent benchmark in an interactive web environment, which evaluates the planning and interaction performance of language agents across multiple languages, thereby contributing to the advancement of global agent intelligence.

**Data Type**: text instructions

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese
- French
- Spanish
- German
- Greek
- Bulgarian
- Russian
- Turkish
- Arabic
- Vietnamese
- Thai
- Hindi
- Swahili
- Urdu

**Resources**:
- [GitHub Repository](https://github.com/WPENGxs/X-WebAgentBench)

## 🎯 Purpose and Intended Users

**Goal**: To fill the gap in evaluating language agents in multilingual contexts and provide actionable insights and recommendations to enhance language model performance in these settings.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Interactive Agent Evaluation

**Limitations**: The quality cannot be completely equivalent to that of experienced translators.

## 💾 Data

**Source**: WebShop Dataset

**Size**: 2,800 multilingual instructions and 589,946 product entries

**Format**: JSON

**Annotation**: Manual translation and quality checks by multilingual experts

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Task Score

**Calculation**: Task scores are computed based on performance on interactive tasks.

**Interpretation**: Higher task scores indicate better interactive performance of language agents in multilingual contexts.

**Validation**: Quality checks through manual rechecks and assessments using LLM metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: The benchmark includes diverse demographics across 14 languages.

**Potential Harm**: ['Misrepresentation of multilingual capabilities']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data is sourced from open-access WebShop and does not violate privacy regulations.

**Data Licensing**: Data is open-source and freely accessible for academic research.

**Consent Procedures**: Informed consent obtained from all participating annotators.

**Compliance With Regulations**: Not Applicable
