# ISO-B ENCH (Image-State Ordering Benchmark)

## 📊 Benchmark Details

**Name**: ISO-B ENCH (Image-State Ordering Benchmark)

**Overview**: ISO-B ENCH is a benchmark for evaluating whether models can infer causal dependencies between visual observations and procedural text, constructed to test multimodal causal reasoning abilities in vision-language models.

**Data Type**: text-image pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- RecipeQA
- TOMATO
- VCOPA

**Resources**:
- [Resource](https://huggingface.co/datasets/StonyBrookNLP/ISO-Bench)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective is to test the ability of multimodal models to reason about causal relationships across visual and textual steps in procedural plans.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Causal Reasoning

**Limitations**: The benchmark only investigates English-language documents, limiting generalizability. It currently lacks a development set for few-shot experiments.

## 💾 Data

**Source**: Constructed from two instructional video datasets: YouCook2 and CrossTask.

**Size**: 764 examples

**Format**: JSON

**Annotation**: Manually annotated with binary labels indicating causal dependencies.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- F1 Score
- Precision
- Recall

**Calculation**: Evaluation based on per-class precision, recall, and F1 score.

**Interpretation**: Higher F1 scores indicate better performance in causal reasoning tasks.

**Baseline Results**: Human performance achieves an F1 Score of 0.98 on the benchmark.

**Validation**: Results validated through testing various multimodal models on the benchmark.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
