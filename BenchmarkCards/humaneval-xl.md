# HumanEval-XL

## 📊 Benchmark Details

**Name**: HumanEval-XL

**Overview**: HumanEval-XL is a massively multilingual code generation benchmark designed to evaluate cross-lingual natural language generalization by connecting 23 natural languages with 12 programming languages and comprising a collection of 22,080 prompts with an average of 8.33 test cases.

**Data Type**: code generation problems

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Arabic
- Hebrew
- Vietnamese
- Chinese
- Russian
- German
- Spanish
- French
- Italian
- Portuguese
- Turkish
- Indonesian
- Finnish
- Hungarian
- Greek
- Bulgarian
- Malay
- Tagalog
- Afrikaans

**Similar Benchmarks**:
- HumanEval
- Multi-lingual HumanEval

**Resources**:
- [GitHub Repository](https://github.com/FloatAI/humaneval-xl)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation platform for multilingual LLMs, facilitating the assessment of natural language understanding and their capability in generating code across multiple programming languages.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: Constructed using a translation and back-translation pipeline incorporating LLMs like GPT-4, covering multiple natural languages and programming languages.

**Size**: 22,080 prompts

**Format**: N/A

**Annotation**: Manual annotation and quality checks based on BERTScore and heuristic evaluations.

## 🔬 Methodology

**Methods**:
- Pass@k metric evaluation

**Metrics**:
- Pass@1

**Calculation**: The pass@k metric evaluates the success rate of executing test cases based on the benchmark prompts.

**Interpretation**: Higher pass@1 scores indicate better performance of the LLM in generating correct code based on the given natural language prompts.

**Baseline Results**: Results from various LLMs including CodeT5+, CodeGen2, GPT-3.5, and GPT-4.

**Validation**: Extensive experiments performed to assess performance across multiple models at different parameter scales.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack, Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: ['Questioning the understanding of code semantics across different languages']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
