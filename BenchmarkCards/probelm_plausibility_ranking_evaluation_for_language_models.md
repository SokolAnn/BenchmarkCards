# PROBELM (Plausibility Ranking Evaluation for Language Models)

## 📊 Benchmark Details

**Name**: PROBELM (Plausibility Ranking Evaluation for Language Models)

**Overview**: PROBELM is a benchmark designed to assess language models’ ability to discern more plausible from less plausible scenarios through their parametric knowledge. It evaluates models' capabilities to prioritize plausible scenarios that leverage world knowledge over less plausible alternatives.

**Data Type**: scenario ranking

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TruthfulQA
- COPA

**Resources**:
- [Resource](https://huggingface.co/datasets/MoyYuan/PRobELM)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate language models’ ability to discern plausible scenarios and fill a gap left by benchmarks focused on factual accuracy.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Plausibility Ranking
- Scenario Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Wikidata edit histories

**Size**: 126,000 scenarios

**Format**: JSON

**Annotation**: Automatically generated less plausible scenarios based on statistical techniques.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Mean Reciprocal Rank (MRR)
- Normalized Discounted Cumulative Gain (NDCG)

**Calculation**: Metrics are calculated based on the ranking of scenarios assessed by model outputs.

**Interpretation**: Higher scores indicate better ability to discern the most plausible scenario among alternatives.

**Validation**: Evaluated models were assessed against four distinct timeframes.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
