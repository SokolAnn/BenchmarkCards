# Wikipedia Ontology-Free Graph-text dataset ( WikiOFGraph )

## 📊 Benchmark Details

**Name**: Wikipedia Ontology-Free Graph-text dataset ( WikiOFGraph )

**Overview**: We introduce WikiOFGraph, a new large-scale G2T dataset generated using a novel method that leverages Large Language Model (LLM) and Data-QuestEval, containing 5.85M general-domain graph-text pairs.

**Data Type**: graph-text pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- WebNLG
- GenWiki
- TekGen
- LAGRANGE

**Resources**:
- [GitHub Repository](https://github.com/daehuikim/WikiOFGraph)

## 🎯 Purpose and Intended Users

**Goal**: The purpose of WikiOFGraph is to provide a high-quality dataset for Graph-to-Text generation tasks that improves upon existing ontology-based datasets.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Graph-to-Text Generation

**Limitations**: N/A

## 💾 Data

**Source**: Generated from source sentences extracted from English Wikipedia.

**Size**: 5.85M graph-text pairs

**Format**: N/A

**Annotation**: Automatically generated using LLM and Data-QuestEval filtering.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated filtering metrics

**Metrics**:
- BLEU
- METEOR
- ChrF++
- TER
- BLEURT
- ROUGE-L
- BERTScore-F1

**Calculation**: Evaluation metrics were calculated based on predicted text compared to human-crafted examples.

**Interpretation**: Higher scores on metrics indicate better graph-text consistency and quality of generation.

**Baseline Results**: N/A

**Validation**: The dataset's graph-text pairs were validated using Data-QuestEval to ensure high consistency.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Wikipedia is licensed under the Creative Commons Attribution-ShareAlike 3.0 Unported License.

**Consent Procedures**: Compensation for human evaluators was provided through Upwork.

**Compliance With Regulations**: Not Applicable
