# TIMECHARA

## 📊 Benchmark Details

**Name**: TIMECHARA

**Overview**: TIMECHARA is a benchmark designed to evaluate point-in-time character hallucination in role-playing LLMs, revealing significant hallucination issues in current state-of-the-art LLMs.

**Data Type**: text

**Domains**:
- role-playing
- language modeling

**Languages**:
- English

**Resources**:
- [Resource](https://ahnjaewoo.github.io/timechara)

## 🎯 Purpose and Intended Users

**Goal**: Evaluate point-in-time character hallucination in role-playing LLMs.

**Target Audience**:
- Researchers
- Practitioners in AI
- Developers of LLMs

**Tasks**:
- Assess character consistency
- Evaluate spatiotemporal reasoning
- Identify character hallucinations

**Limitations**: None

## 💾 Data

**Source**: TIMECHARA dataset compiled from popular novel series including Harry Potter, The Lord of the Rings, Twilight, and The Hunger Games.

**Size**: 10,895 instances

**Format**: text-based dialogues

**Annotation**: Spatiotemporal labels and character profiling included.

## 🔬 Methodology

**Methods**:
- Automated pipeline for dataset generation
- Structured interviews for character assessments
- Evaluation by LLM judges

**Metrics**:
- Spatiotemporal consistency
- Personality consistency

**Calculation**: Evaluation scores based on binary labels for consistency and qualitative ratings for personality.

**Interpretation**: Scores reflect the ability of LLMs to maintain character identity across specified time points.

**Baseline Results**: Baseline results indicate significant variability in character hallucination rates among different LLMs with some achieving above 90% consistency in ideal scenarios.

**Validation**: Manually annotated results confirmed via human evaluation showing alignment with outputs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Character hallucination
- Data bias
- Evaluation bias

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Explainability**: Unexplainable output
- **Transparency**: Lack of training data transparency
- **Robustness**: Prompt injection attack

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset consists primarily of publicly available texts, ensuring no private data is included.

**Data Licensing**: Utilizes excerpts from copyrighted material under fair use for educational and research purposes.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: The research complies with ethical standards for AI research involving copyrighted works.
