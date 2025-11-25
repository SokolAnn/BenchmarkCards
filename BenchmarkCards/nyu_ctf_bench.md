# NYU CTF Bench

## 📊 Benchmark Details

**Name**: NYU CTF Bench

**Overview**: The NYU CTF Bench is a scalable, open-source benchmark dataset specifically designed for evaluating large language models (LLMs) in solving Capture the Flag (CTF) challenges in cybersecurity. It comprises 200 diverse CTF challenges from various competitions, offering a comprehensive framework for LLM evaluation and tool integration.

**Data Type**: CTF challenges

**Domains**:
- Cybersecurity

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- GPQA

**Resources**:
- [GitHub Repository](https://github.com/NYU-LLM-CTF/NYU_CTF_Bench)
- [GitHub Repository](https://github.com/NYU-LLM-CTF/llm_ctf_automation)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark dataset for evaluating the performance of large language models in solving cybersecurity CTF challenges.

**Target Audience**:
- ML Researchers
- Cybersecurity Professionals
- Model Developers

**Tasks**:
- Vulnerability Detection
- Automated Task Solving

**Limitations**: Some categories are underrepresented in the current dataset, and future improvements aim to enhance tool/platform support.

## 💾 Data

**Source**: 200 CTF challenges sourced from the annual NYU Cybersecurity Awareness Week (CSAW) competitions.

**Size**: 200 challenges

**Format**: JSON

**Annotation**: Challenges are manually validated for setup and solvability.

## 🔬 Methodology

**Methods**:
- Automated evaluation using LLMs
- Manual validation of challenges

**Metrics**:
- Accuracy of flag retrieval
- Number of solved challenges

**Calculation**: Metrics calculated based on the number of challenges solved by each LLM during evaluations.

**Interpretation**: A higher percentage of solved challenges indicates better performance of the LLMs.

**Baseline Results**: GPT-4 and Claude 3 showed the highest performance among evaluated models.

**Validation**: Challenges validated to ensure proper functioning and manual verification for solvability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Ethical Use
- Security

**Atlas Risks**:
- **Fairness**: Output bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: N/A - Not discussed in context.

**Data Licensing**: Open-source availability, specific licenses not detailed.

**Consent Procedures**: N/A - Not discussed.

**Compliance With Regulations**: N/A - Not discussed.
