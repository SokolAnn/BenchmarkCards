# CoLoTa (Commonsense reasoning over Long-Tail entities)

## 📊 Benchmark Details

**Name**: CoLoTa (Commonsense reasoning over Long-Tail entities)

**Overview**: CoLoTa is a dataset consisting of 3,300 queries for commonsense reasoning over long-tail entities, aimed at evaluating both LLM commonsense reasoning capabilities and KGQA methods.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- StrategyQA
- CREAK

**Resources**:
- [GitHub Repository](https://github.com/D3Mlab/CoLoTa)
- [Resource](https://arxiv.org/abs/2504.14462)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the entity-based commonsense reasoning capabilities of LLMs in long-tail settings and improve KGQA methodologies.

**Target Audience**:
- ML Researchers
- KGQA Developers
- NLP Practitioners

**Tasks**:
- Commonsense Reasoning
- Knowledge Graph Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Queries formulated from existing entity-based commonsense reasoning datasets, specifically StrategyQA and CREAK.

**Size**: 3,300 examples

**Format**: N/A

**Annotation**: Annotated with reasoning steps and knowledge graph facts.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy
- FActScore
- Reasoning Score

**Calculation**: FActScore measures the percentage of atomic facts supported by a knowledge source. Reasoning Score assesses the validity of logical reasoning in the LLM responses.

**Interpretation**: Higher scores indicate better performance in commonsense reasoning and factual accuracy.

**Baseline Results**: N/A

**Validation**: Queries validated for factual knowledge supported by Wikidata.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
