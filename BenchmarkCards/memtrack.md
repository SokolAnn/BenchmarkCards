# MEMTRACK

## 📊 Benchmark Details

**Name**: MEMTRACK

**Overview**: MEMTRACK is a benchmark designed to evaluate long-term memory and state tracking in multi-platform agent environments. It models realistic organizational workflows by integrating asynchronous events across multiple communication and productivity platforms such as Slack, Linear, and Git.

**Data Type**: event timelines and question-answer pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- LoCoMo
- LongMemEval

**Resources**:
- [Resource](https://drive.google.com/file/d/1ymMXmOIhCUcwC1WKOW8kioZgeYyrt-qe/view?usp=sharing)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the memory capabilities of AI agents in dynamic environments and to promote research on multi-agent, multi-platform memory benchmarking.

**Target Audience**:
- ML Researchers
- Agent Developers
- AI Practitioners

**Tasks**:
- Contextual Memory Evaluation
- Multi-Platform Agent Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Curated through manual expert-driven design and scalable agent-based synthesis.

**Size**: 47 instances

**Format**: JSON

**Annotation**: Manual annotation and verification by in-house experts.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Correctness
- Efficiency
- Redundancy

**Calculation**: Metrics are calculated based on the accuracy of agent responses to the questions posed during evaluations.

**Interpretation**: Performance is evaluated on the basis of how well agents can reason over task-relevant information across multiple platforms.

**Validation**: Validated through experiments across state-of-the-art LLMs and memory backends.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
