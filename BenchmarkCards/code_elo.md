# CODE ELO

## 📊 Benchmark Details

**Name**: CODE ELO

**Overview**: CODE ELO is a standardized competition-level code generation benchmark that tests the coding abilities of existing large language models (LLMs) using problems sourced from the CodeForces platform, providing human-comparable Elo ratings.

**Data Type**: problem statements and solutions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- APPS
- CodeContests
- LiveCodeBench
- USACO

**Resources**:
- [Resource](https://CodeElo-bench.github.io)
- [Resource](https://hf.co/datasets/Qwen/CodeElo)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation of the coding capabilities of large language models on competition-level coding problems.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Code Generation

**Limitations**: The benchmark constrains each model's submissions to eight per problem, which could slightly lower their true Elo ratings.

## 💾 Data

**Source**: Problems sourced from the CodeForces platform, including contest problems with detailed attributes.

**Size**: 387 problems

**Format**: HTML

**Annotation**: Problems classified by contest divisions, difficulty ratings, and algorithm tags.

## 🔬 Methodology

**Methods**:
- Problem submission to CodeForces
- Elo rating calculation

**Metrics**:
- Elo Rating

**Calculation**: The Elo rating system used is based on the performance of models in contests and compares them against human ratings.

**Interpretation**: Higher Elo ratings indicate better coding capabilities and performance relative to human participants.

**Baseline Results**: Elo ratings of models achieved indicate their percentile rank compared to human participants.

**Validation**: Validation through direct submission to the CodeForces platform, achieving zero false positives.

## ⚠️ Targeted Risks

**Risk Categories**:
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
