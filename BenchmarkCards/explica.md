# ExpliCa

## 📊 Benchmark Details

**Name**: ExpliCa

**Overview**: ExpliCa is a dataset designed to evaluate Large Language Models (LLMs) on explicit causal reasoning through pairwise causal discovery (PCD) tasks. It comprises sentence pairs annotated with causal and temporal relations expressed via linguistic connectives, along with human acceptability ratings for each connective.

**Data Type**: sentence pairs with causal and temporal relations

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- COPA
- Causal TimeBank
- CaTeRS
- Event Story Line
- BeCause Corpus

**Resources**:
- [GitHub Repository](https://github.com/Unipisa/explica)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLMs' capabilities in commonsense causal reasoning through explicit causal and temporal relations.

**Target Audience**:
- ML Researchers
- Natural Language Processing Practitioners
- Model Developers

**Tasks**:
- Pairwise Causal Discovery
- Acceptability Rating
- Cloze Test
- Multiple-Choice Task

**Limitations**: The dataset design excludes certain cues, focusing evaluation on deeper understanding, rather than superficial linguistic correlations.

## 💾 Data

**Source**: Annotated by native English speakers via crowdsourcing.

**Size**: 4,800 sentence pairs

**Format**: N/A

**Annotation**: Crowdsourced human acceptability ratings

## 🔬 Methodology

**Methods**:
- Human evaluation
- Prompting tasks
- Perplexity evaluation

**Metrics**:
- Accuracy
- Perplexity

**Calculation**: Accuracy is calculated based on model responses compared to human acceptability ratings.

**Interpretation**: Higher accuracy indicates better causal reasoning capabilities among models.

**Baseline Results**: Top-performing LLMs struggled to reach 0.80 accuracy.

**Validation**: The dataset was validated to ensure uniform statistical relations across categories.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)

**Consent Procedures**: Participants provided formal consent to take part in the study.

**Compliance With Regulations**: Not Applicable
