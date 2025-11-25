# A Law Reasoning Benchmark for LLM with Tree-Organized Structures

## 📊 Benchmark Details

**Name**: A Law Reasoning Benchmark for LLM with Tree-Organized Structures

**Overview**: We propose a transparent law reasoning schema enriched with hierarchical factum probandum, evidence, and implicit experiences, along with a challenging task to create a hierarchical reasoning structure from a textual case description. We introduce the first crowd-sourced dataset for this task, enabling comprehensive evaluation.

**Data Type**: text

**Domains**:
- Law

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/cocacola-lab/LawReasoningBenchmark)

## 🎯 Purpose and Intended Users

**Goal**: To enable transparent and accountable AI-assisted law reasoning through structured evidence analysis and fact determination.

**Target Audience**:
- ML Researchers
- Legal Practitioners
- Law Schools

**Tasks**:
- Transparent Law Reasoning
- Factum Probandum Generation
- Evidence Reasoning
- Experience Generation

**Limitations**: N/A

## 💾 Data

**Source**: Crowd-sourced data from legal case descriptions available on the China Judgement Online Website.

**Size**: 453 cases

**Format**: N/A

**Annotation**: Crowdsourced via law school students and professionals, ensuring quality through two-phase methodology including automated annotation and human refinement.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- ROUGE Score
- Precision
- Recall
- F1 Score

**Calculation**: Metrics calculated based on predicted and actual outcomes related to factual and evidential reasoning.

**Interpretation**: Performance evaluated based on the accuracy of law reasoning structures generated.

**Baseline Results**: Compared with baseline models including ChatGLM-6B, LexiLaw, and others.

**Validation**: Cross-validation with multiple annotator reviews for reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data sourced from publicly available records with no personal identifiers.

**Data Licensing**: Not Applicable

**Consent Procedures**: All participants informed and consented voluntarily.

**Compliance With Regulations**: Exercise of ethical principles per Declaration of Helsinki.
