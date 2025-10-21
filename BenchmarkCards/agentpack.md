# AGENTPACK

## 📊 Benchmark Details

**Name**: AGENTPACK

**Overview**: AGENTPACK is a dataset of 1.3M code edits co-authored by Claude Code, OpenAI Codex, and Cursor Agent across public GitHub projects, aimed at enhancing fine-tuning for code editing tasks.

**Data Type**: code changes

**Domains**:
- Software Engineering

**Languages**:
- Python
- JavaScript
- TypeScript

**Similar Benchmarks**:
- HumanEvalFix
- CanItEdit

**Resources**:
- [Resource](https://huggingface.co/datasets/nuprl/AgentPack)

## 🎯 Purpose and Intended Users

**Goal**: To provide a diverse and high-quality dataset for training models on code editing tasks, facilitating research and development in software engineering.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Code Editing

**Limitations**: The dataset contains model-authored descriptions and corresponding code edits but not the original prompts that elicited them.

## 💾 Data

**Source**: Public GitHub repositories

**Size**: 60GB

**Format**: Mixed code formats (files with various programming languages)

**Annotation**: Collectively authored changes by agents and humans, including natural language descriptions.

## 🔬 Methodology

**Methods**:
- Automated collection from GitHub
- Analysis of commit messages and code changes

**Metrics**:
- Pass@1 score

**Calculation**: Metrics calculated based on evaluation of model outputs against benchmark tasks.

**Interpretation**: A higher Pass@1 score indicates better performance in generating correct code based on editing instructions.

**Baseline Results**: Models trained on AGENTPACK showed improvements over previous models trained solely on human-only commit corpora.

**Validation**: Evaluated using well-established benchmarks such as HumanEvalFix and CanItEdit.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Analysis of programming language usage shows diversity in low-resource programming languages.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
