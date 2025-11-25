# RealHumanEval (Evaluating Large Language Models’ Abilities to Support Programmers)

## 📊 Benchmark Details

**Name**: RealHumanEval (Evaluating Large Language Models’ Abilities to Support Programmers)

**Overview**: RealHumanEval is a human-centric evaluation platform for large language models (LLMs) designed to assess their effectiveness in assisting programmers through autocomplete suggestions and chat support. It was developed to facilitate user studies evaluating coding performance with LLM assistance, logging user interactions to analyze the impact on productivity.

**Data Type**: programming tasks and interactions

**Domains**:
- Computer Science

**Languages**:
- English

**Similar Benchmarks**:
- HumanEval
- MBPP

**Resources**:
- [GitHub Repository](https://github.com/clinicalml/realhumaneval)
- [Resource](https://huggingface.co/datasets/hsseinmz/realhumaneval)

## 🎯 Purpose and Intended Users

**Goal**: To provide a platform for human-centric evaluations of code-generating large language models (LLMs) and to study their impact on programmer productivity.

**Target Audience**:
- ML Researchers
- Software Developers
- Educators

**Tasks**:
- Coding Skills Assessment
- User Productivity Analysis

**Limitations**: The study's task set does not cover the full range of problems faced by professional programmers, which may limit generalizability.

## 💾 Data

**Source**: User interactions with the RealHumanEval platform during studies involving various code LLMs.

**Size**: 243 participants, 888 coding tasks

**Format**: structured datasets with logs of interactions

**Annotation**: User interactions are logged automatically during study participation.

## 🔬 Methodology

**Methods**:
- User study

**Metrics**:
- Time to Complete Task
- Number of Tasks Completed
- Acceptance Rate of Suggestions

**Calculation**: Metrics are calculated using logged interaction data from participants interacting with LLMs during coding tasks.

**Interpretation**: A lower time to complete a task indicates higher productivity, while a higher acceptance rate reflects better LLM suggestion quality.

**Validation**: Participant performance was analyzed across seven conditions with comparisons made against a control group without LLM support.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Privacy

**Atlas Risks**:
- **Fairness**
- **Accuracy**
- **Privacy**

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The study was approved by institutional IRB review, and participants provided consent to collect interaction data.

**Data Licensing**: Not Applicable

**Consent Procedures**: Participants provided informed consent and had the option to opt-out.

**Compliance With Regulations**: The study adhered to ethical guidelines for human subjects research.
