# EarthSE (Earth Scientific Exploration)

## 📊 Benchmark Details

**Name**: EarthSE (Earth Scientific Exploration)

**Overview**: EarthSE is a comprehensive benchmark for evaluating the capabilities of LLMs in Earth sciences, constructed from 100,000 research papers. It includes two QA datasets, Earth-Iron and Earth-Silver, and an open-ended dialogue dataset, Earth-Gold, covering fundamental and advanced evaluation tasks across five Earth spheres.

**Data Type**: question-answering pairs, open-ended dialogues

**Domains**:
- Natural Language Processing
- Earth Sciences

**Languages**:
- English

**Similar Benchmarks**:
- ScienceQA
- SciBench
- OceanBench

**Resources**:
- [Resource](https://huggingface.co/datasets/earthse)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate the performance of LLMs in Earth science tasks, particularly their capabilities in scientific exploration and reasoning.

**Target Audience**:
- ML Researchers
- Earth Science Researchers
- Model Developers

**Tasks**:
- Question Answering
- Open-ended Dialogue

**Limitations**: No integration of the 11 tasks into a complex task chain.

## 💾 Data

**Source**: Curated from 100,000 Earth science academic papers.

**Size**: 100,000 papers, 4,133 QA questions in Earth-Iron, and multiple dialogue exchanges in Earth-Gold.

**Format**: JSON, structured question-answer pairs, open-ended dialogue format.

**Annotation**: Automated generation with human verification.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Win Rate
- Semantic Similarity
- Retention Rate
- Diversity

**Calculation**: Metrics like win rate are computed by comparing model outputs with reference answers based on relevance, scientific rigor, and specificity.

**Interpretation**: Higher scores in retention and diversity indicate better performance and scientific exploration capabilities.

**Baseline Results**: Models underperformed significantly in complex Earth science reasoning tasks.

**Validation**: Rigorously evaluated by domain experts and through automated cleaning protocols.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
