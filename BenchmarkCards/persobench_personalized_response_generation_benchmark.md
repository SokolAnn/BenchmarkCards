# PersoBench (Personalized Response Generation Benchmark)

## 📊 Benchmark Details

**Name**: PersoBench (Personalized Response Generation Benchmark)

**Overview**: PersoBench is a benchmark designed to evaluate the personalization ability of large language models (LLMs) in persona-aware dialogue generation within a zero-shot setting. It benchmarks LLMs across three well-known persona-aware datasets and evaluates multiple dimensions of response quality including fluency, diversity, coherence, and personalization.

**Data Type**: dialogue samples

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- RPBench-Auto
- TIMECHARA
- RoleLLM

**Resources**:
- [GitHub Repository](https://github.com/salehafzoon/PersoBench)

## 🎯 Purpose and Intended Users

**Goal**: To assess the strengths and limitations of current LLMs in generating personalized responses in persona-aware conversations.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Response Generation
- Dialogue Systems Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Three publicly available persona-aware datasets: Blended Skill Talk, Follow-up Customized conversation (FoCus), and IT-ConvAI2.

**Size**: 3,600 samples

**Format**: Raw text files

**Annotation**: Each dataset includes persona annotations and conversation context for generating responses.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Fluency
- Diversity
- Coherence
- Personalization

**Calculation**: Metrics were calculated based on various linguistic and semantic evaluations using established benchmarks.

**Interpretation**: Higher scores in fluency, diversity, coherence, and personalization indicate better model performance.

**Baseline Results**: N/A

**Validation**: Evaluated in both standard and Chain-of-Thought prompting setups.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
