# MANGO: A Benchmark for Evaluating Mapping and Navigation Abilities of Large Language Models

## 📊 Benchmark Details

**Name**: MANGO: A Benchmark for Evaluating Mapping and Navigation Abilities of Large Language Models

**Overview**: MANGO is a benchmark designed to evaluate the mapping and navigation capabilities of large language models through a set of mazes paired with questions about navigation and routes.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://mango.ttic.edu)
- [GitHub Repository](https://github.com/oaklight/mango/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and improve the mapping and navigation capabilities of large language models in text-based adventure games.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: The dataset consists of mazes derived from a suite of text-based adventure games (Jericho game suite) with corresponding walkthroughs and a variety of destination-finding and route-finding questions.

**Size**: 3 million destination-finding questions and 200,000 route-finding questions

**Format**: JSON

**Annotation**: Annotated by human annotators identifying locations and generating questions based on maze structures.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Success Rate

**Calculation**: Success rate is calculated as the fraction of questions correctly answered by the model, allowing for partial matches for destination-finding questions and executing moves for route-finding questions.

**Interpretation**: A higher success rate indicates better navigation and mapping capabilities of the LLMs on the benchmark.

**Validation**: Validation conducted through human evaluations on a subset of questions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
