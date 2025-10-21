# LLMSecEval: A Dataset of Natural Language Prompts for Security Evaluations

## 📊 Benchmark Details

**Name**: LLMSecEval: A Dataset of Natural Language Prompts for Security Evaluations

**Overview**: LLMSecEval is a dataset containing 150 natural language (NL) prompts for assessing the security of code produced by large language models. The prompts describe code snippets prone to vulnerabilities listed in MITRE's Top 25 Common Weakness Enumeration (CWE) ranking and each prompt includes a secure implementation example to facilitate comparative evaluations against code produced by LLMs.

**Data Type**: text (natural language prompts and source code examples)

**Domains**:
- Natural Language Processing
- Software Security

**Languages**:
- English

**Similar Benchmarks**:
- HumanEval
- Dataset of Pearce et al. (code scenarios for GitHub Copilot)

**Resources**:
- [GitHub Repository](https://github.com/tuhh-softsec/LLMSecEval/)
- [Resource](https://doi.org/10.5281/zenodo.7565964)
- [Resource](https://arxiv.org/abs/2303.09384)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate research on the security of automatic code-generation models by providing 150 NL prompts covering 18 of the Top 25 CWE scenarios (2021) together with secure code examples, enabling assessment of whether LLMs introduce security vulnerabilities and supporting prompt engineering for secure code generation.

**Target Audience**:
- ML Researchers
- Software Developers
- Security Researchers

**Tasks**:
- Code Generation
- Security Evaluation
- Vulnerability Detection
- Prompt Engineering

**Limitations**: Currently covers only 18 out of the Top 25 CWEs (2021); prompts are language-agnostic which may make some CWE-specific prompts unsuitable across different programming languages; unit tests for security are not yet provided (planned future work).

## 💾 Data

**Source**: Derived from C and Python snippets in the dataset of Pearce et al. [12]; NL prompts were generated using OpenAI Codex (code-davinci-002) and then manually curated by the authors.

**Size**: 150 prompts (83 prompts generated from Python programs and 67 from C programs)

**Format**: CSV and JSON

**Annotation**: Manual curation by two of the authors using inclusion/exclusion criteria and formatting rules; prompts labeled with CWE name, source code filepath, vulnerable flag (as reported in [12]), language of origin, quality metric scores; quality metrics (Naturalness, Expressiveness, Adequacy, Conciseness) were assigned manually by two authors following the criteria of Hu et al.; secure code examples were created mostly manually and their security was checked using CodeQL.

## 🔬 Methodology

**Methods**:
- Human evaluation (manual scoring of prompt quality by two authors)
- Model-based generation using GPT-3 and Codex to generate code from prompts
- Automated code analysis using CodeQL to detect CWEs

**Metrics**:
- Naturalness (1-5)
- Expressiveness (1-5)
- Adequacy (1-5)
- Conciseness (1-5)
- CWE detection via CodeQL (built-in QL queries)
- Inter-rater agreement: Weighted Cohen's Kappa

**Calculation**: Quality metric scores (Naturalness, Expressiveness, Adequacy, Conciseness) were assigned manually by two authors following the criteria of Hu et al. Scores range from 1 to 5. Inter-rater reliability was measured using a weighted Cohen's Kappa coefficient. CodeQL built-in QL queries were used to detect 18 of the Top 25 CWEs in generated code.

**Interpretation**: Higher metric scores (closer to 5) indicate better prompt quality (fluency, readability, adequacy, conciseness). A weighted Cohen's Kappa value greater than 0.79 indicates strong agreement among raters; the authors report kappa values demonstrating high agreement.

**Validation**: Inter-rater reliability assessed via weighted Cohen's Kappa (reported kappa values: 0.98 for Naturalness, 0.83 for Expressiveness, 0.80 for Adequacy, 0.88 for Conciseness). Secure code examples were checked using CodeQL.

## ⚠️ Targeted Risks

**Risk Categories**:
- Security

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
