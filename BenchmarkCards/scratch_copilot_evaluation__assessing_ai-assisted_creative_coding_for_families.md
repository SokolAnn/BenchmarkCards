# Scratch Copilot Evaluation: Assessing AI-Assisted Creative Coding for Families

## 📊 Benchmark Details

**Name**: Scratch Copilot Evaluation: Assessing AI-Assisted Creative Coding for Families

**Overview**: This study explores the potential of large language models (LLMs) in helping families with creative coding using Scratch. The authors devised three evaluation scenarios (code explanation, debugging, ideation), used 22 Scratch projects per scenario, generated responses from LLMs with and without practice tasks resulting in 120 creative coding support scenarios, and had the authors independently evaluate precision, pedagogical value, and age-appropriate language. The evaluation framework and labeled evaluation data are publicly available.

**Data Type**: text (Scratch project code inputs and model-generated explanatory/debugging/ideation responses)

**Domains**:
- Computer Science Education
- Human-Computer Interaction

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/stefania11/ScratchCopilot-Evaluation)
- [Resource](https://arxiv.org/abs/2305.10417)

## 🎯 Purpose and Intended Users

**Goal**: To determine how well large-language models support explaining, ideating, and debugging Scratch projects for middle school families.

**Target Audience**:
- Middle school families
- Model developers and designers of AI-supported coding tools
- Computing education researchers

**Tasks**:
- Code Explanation
- Code Debugging
- Code Ideation

**Limitations**: The set of input programs is not exhaustive; the 22 Scratch projects are a representative sample and may not capture the full diversity of Scratch projects. Evaluation scenarios focused on code explanation, debugging, and ideation and do not cover other possible support scenarios (e.g., program design, structuring code, clones and lists).

## 💾 Data

**Source**: A curated collection of 22 Scratch projects selected from the Scratch public repository and popular Scratch community projects and salient examples from a previous study.

**Size**: 22 Scratch projects; 120 creative coding support scenarios (generated model responses with and without practice tasks).

**Format**: N/A

**Annotation**: The first two authors independently evaluated each scenario on precision, pedagogical value, and age-appropriate language; disagreements were resolved through discussion until consensus.

## 🔬 Methodology

**Methods**:
- Automated LLM generation using OpenAI GPT-4 (prompted with Scratch program and task-specific instructions, with and without practice tasks)
- Human evaluation by the authors (independent judgments and consensus discussions)

**Metrics**:
- Success rate (percentage of scenarios meeting task criteria)
- Accuracy
- Pedagogical value (human judgment)
- Age-appropriate language (human judgment)

**Calculation**: Percentages reported (e.g., proportion of evaluated scenarios meeting criteria) were computed based on the authors' judgments of whether model outputs met the evaluation criteria (e.g., correct bug identification, completeness of explanations).

**Interpretation**: Higher percentages indicate better support by LLMs; the authors report an overall success rate of more than 80% across tasks and interpret this as substantial potential for LLMs to support family creative coding, while noting areas for improvement.

**Baseline Results**: Reported GPT-4 evaluation results (from Table 1 and text): Explain code: 100% (noting tone issues); Explain code with learning: 100%; Debug code: 80%; Debug code with learning: 90%; Code ideas: 100%; Code ideas with learning: 100%. Additionally, text notes: of 40 code explanations, 90% explained all parts of the code; of 40 debugging examples, 80% correctly identified introduced bugs.

**Validation**: Validation consisted of independent evaluations by the first two authors focusing on precision, pedagogical value, and age-appropriate language; disagreements were resolved via discussion to reach consensus.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness
- Transparency
- Societal Impact

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Hallucination
- **Transparency**: Uncertain data provenance
- **Societal Impact**: Impact on education: bypassing learning

**Potential Harm**: ['Young learners may become dependent on tools, impairing their ability to create similar code independently.', 'Pre-trained LLMs can reflect and perpetuate societal stereotypes and biases, potentially influencing user perspectives.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
