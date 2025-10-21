# LC-QuAD 3.0

## 📊 Benchmark Details

**Name**: LC-QuAD 3.0

**Overview**: LC-QuAD 3.0 is a new dataset derived from LC-QuAD 2.0, enriched with frame-based annotations using the FRASE method for SPARQL query generation from natural language questions, aimed at enhancing the generalization capabilities of language models.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- LC-QuAD 2.0

**Resources**:
- [Resource](https://arxiv.org/abs/2503.22144)

## 🎯 Purpose and Intended Users

**Goal**: To improve the generalization capabilities of large language models in the task of SPARQL query generation by providing structured semantic representations of natural language questions.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- SPARQL Query Generation

**Limitations**: The best F1 score remains low (50 F1-score), and the method's effectiveness on knowledge bases beyond Wikidata is unvalidated.

## 💾 Data

**Source**: Derived from LC-QuAD 2.0, augmented with frame-based annotations using the FRASE method.

**Size**: 30,225 entries

**Format**: JSON

**Annotation**: Automatically annotated with frame and argument mappings.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- BLEU Score
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated by comparing generated SPARQL queries against gold-standard references and executing them against the knowledge base for execution-based metrics.

**Interpretation**: Higher BLEU scores indicate better surface-level output quality, while execution-based metrics assess the correctness of the generated SPARQL queries.

**Baseline Results**: Various Large Language Models including Phi-4 14B show performance on LC-QUAD datasets, with the best results serving as a baseline.

**Validation**: Various training configurations assessed the impact of incorporating frame-based structured representations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
