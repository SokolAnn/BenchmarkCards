# Linguistic reasoning benchmark for humans and language models

## 📊 Benchmark Details

**Name**: Linguistic reasoning benchmark for humans and language models

**Overview**: We contribute a new challenge benchmark for comparing humans and distributional large language models (LLMs). Our benchmark contains two problem-solving domains (planning and explanation generation) and is designed to require generalization to new, out-of-distribution problems expressed in language.

**Data Type**: text (prompt-response pairs: goal/scenario prompts and generated plans/explanations)

**Domains**:
- Natural Language Processing
- Planning
- Causal Explanation

**Languages**:
- English

**Similar Benchmarks**:
- PIQA

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for comparing humans and distributional LLMs on out-of-distribution reasoning tasks (planning and explanation generation) and to assess robustness and the extent to which predictive language models capture human-like reasoning.

**Tasks**:
- Planning
- Explanation Generation

**Limitations**: The benchmark and demonstration models are limited in coverage: Part II uses a simplified synthetic planning setting and the demonstration hybrid model is highly restricted. The authors note further work is needed to more systematically characterize regimes where predictive language approximates human reasoning and to extend to more realistic reasoning domains.

## 💾 Data

**Source**: Human responses collected from Prolific participants; LLM-generated responses from GPT-3 (Part I) and GPT-Neo / Codex (Part II); synthetic planning data generated from a synthetic grammar over an object-stacking domain.

**Size**: 240 human participants (2 domains x 3 conditions x 40 participants); 28 planning prompts and 28 explanation prompts; 10 unique human responses per prompt/condition; 20 LLM-generated responses collected per prompt/condition after prescreening (initially collected up to 30 per prompt); 100 synthetic planning test configurations in Part II.

**Format**: N/A

**Annotation**: Constraints constructed by an expert human tagger extracting and lemmatizing concrete nouns; human annotators rated "humanness" and overall goodness on 7-point Likert scales; LLM generations prescreened by human annotators; plan success in simulation coded binary (1 = success, 0 = fail).

## 🔬 Methodology

**Methods**:
- Human evaluation (blind comparative ratings on 7-point Likert scale)
- Few-shot prompting of LLMs (GPT-3, GPT-Neo, Codex)
- Simulated plan execution for synthetic planning (binary success evaluation)
- Statistical analysis using linear mixed effects regression (LMER)

**Metrics**:
- Mean human-evaluation score (7-point Likert)
- Accuracy (binary plan success in simulated environment)
- p-values for statistical tests (LMER / likelihood ratio tests)

**Calculation**: Human and LLM generations were rated on a 7-point Likert scale; mean scores compared using linear mixed effects regression (LMER) with random effects for rater and prompt. In the simulated planning domain, generated plans are executed in the environment and success is coded as 1 if the goal state is reached and 0 otherwise.

**Interpretation**: Higher mean human-evaluation scores indicate better-quality plans/explanations. Binary success=1 indicates the plan achieved the goal in simulation. Statistical significance (reported p-values from LMER and likelihood ratio tests) indicates whether differences between sources or conditions are unlikely under the null.

**Validation**: LLM outputs were prescreened by human annotators for plausibility; blind comparative human evaluation used separate annotators to rate mixed human and LLM outputs; simulated execution in the synthetic planning environment provided exact success/failure validation for Part II.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy
- Value Alignment

**Atlas Risks**:
- **Robustness**: Hallucination
- **Accuracy**: Poor model accuracy
- **Value Alignment**: Toxic output

**Potential Harm**: ['Toxic output']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
