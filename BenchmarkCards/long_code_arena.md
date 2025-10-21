# Long Code Arena

## 📊 Benchmark Details

**Name**: Long Code Arena

**Overview**: Long Code Arena is a suite of six benchmarks for code processing tasks that require project-wide context, including library-based code generation, CI builds repair, project-level code completion, commit message generation, bug localization, and module summarization.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- HumanEval
- MBPP
- RepoEval
- RepoBench

**Resources**:
- [Resource](https://huggingface.co/spaces/JetBrains-Research/long-code-arena)
- [GitHub Repository](https://github.com/JetBrains-Research/lca-baselines)

## 🎯 Purpose and Intended Users

**Goal**: To stimulate research in ML-based solutions for realistic software engineering tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Library-based Code Generation
- CI Builds Repair
- Project-Level Code Completion
- Commit Message Generation
- Bug Localization
- Module Summarization

**Limitations**: N/A

## 💾 Data

**Source**: Open-source repositories from GitHub.

**Size**: 7,479 examples

**Format**: JSON

**Annotation**: Manual verification and filtering.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- ChrF
- BLEU Score
- ROUGE-L
- API Recall

**Calculation**: Metrics are calculated based on comparisons of generated outputs against the ground truth.

**Interpretation**: Higher scores indicate better performance in generating accurate and context-aware code or documentation.

**Baseline Results**: GPT-4 shows the best performance in multiple tasks, whereas models like CodeLlama-70B show poorer results.

**Validation**: Metrics are validated using manually curated datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The datasets are re-distributed under the licenses they were originally distributed with on GitHub (permissive licenses).

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
