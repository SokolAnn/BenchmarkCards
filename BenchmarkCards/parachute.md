# Parachute

## 📊 Benchmark Details

**Name**: Parachute

**Overview**: We propose a human-centered evaluation framework, Parachute, for interactive co-writing systems. Parachute showcases an integrative view of interaction evaluation, where each evaluation aspect consists of categorized practical metrics. We present Parachute with a use case to demonstrate how to evaluate and compare co-writing systems using Parachute.

**Data Type**: text (writing artifacts and interaction logs)

**Domains**:
- Human-Computer Interaction
- Natural Language Processing

**Similar Benchmarks**:
- Wordcraft
- Integrative Leaps
- Beyond Text Generation
- Dramatron
- STORIUM

**Resources**:
- [Resource](https://arxiv.org/abs/2303.06333)

## 🎯 Purpose and Intended Users

**Goal**: Provide a human-centered evaluation framework to evaluate and analyze interactive human-LM co-writing systems more comprehensively and fairly.

**Target Audience**:
- Researchers

**Tasks**:
- Human-Language Model Interaction Evaluation
- Interaction Trace Analysis (dynamic interaction trace)
- Writing Artifact Evaluation

**Limitations**: We do not aim to build enumerated lists of evaluation metrics; instead, we focus on introducing the motivation and process of creating evaluation aspects and subgroups.

## 💾 Data

**Source**: N/A

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Coding users' think-aloud transcripts
- Coding researchers' observation notes
- Coding (semi-)structured interview transcripts
- Questionnaires or Surveys (e.g., five-point Likert ratings, single/multiple choice)
- Interaction data logs analysis
- Assessment on the written artifacts (automatic metrics comparing with ground truth, artifact properties, external expert evaluation)

**Metrics**:
- enjoyment
- preference
- cognitive load
- usability
- repetition
- helpful
- variety
- uniqueness
- novelty
- coherence
- latency
- incorporation rate
- request count
- accepted suggestions
- time to complete
- word edit distance
- lemma-based Jaccard similarity
- document length difference
- external expert evaluation
- word count
- satisfaction
- ownership
- learning curve
- consistency

**Calculation**: Iterative interaction change measured by comparing metric_state(i) vs. metric_state(j) (diff from prior knowledge / diff from previous interaction states); latency measured as elapsed time from human request to AI response; incorporation rate measured as rate of incorporating AI suggestions; word edit distance measured between prior- and post- articles; lemma-based Jaccard similarity measured between ground truth and outcome article; subjective metrics collected via surveys/interviews.

**Interpretation**: Assess users' dynamic interaction improvements (relative quality change between iterated articles from the same user) to indicate system capability, rather than relying solely on final article quality. Compare systems using the same group of users and consistent metrics for fair evaluation.

**Validation**: Authors recommend applying all measurements to both the evaluated system and baselines, ideally with the same group of users. Validation approaches include user studies, expert review, and interaction log analysis as summarized in Appendix A.2. No formal quantitative validation of Parachute as a benchmark is reported.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness

**Atlas Risks**:
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: ['stereotypical suggestions']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
