# SwallowCode and SwallowMath

## 📊 Benchmark Details

**Name**: SwallowCode and SwallowMath

**Overview**: SwallowCode and SwallowMath are openly licensed datasets designed to enhance large language model (LLM) capabilities in program synthesis and mathematical reasoning. SwallowCode refines Python code from The-Stack-v2 through a four-stage pipeline, while SwallowMath transforms the Finemath-4+ dataset, improving quality and performance.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/tokyotech-llm/swallow-code)
- [Resource](https://huggingface.co/datasets/tokyotech-llm/swallow-math)

## 🎯 Purpose and Intended Users

**Goal**: To significantly enhance LLM performance in code generation and mathematical reasoning through refined pre-training datasets.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Code Generation
- Mathematical Reasoning

**Limitations**: The rewriting process may preserve biases from source data.

## 💾 Data

**Source**: The datasets are constructed by rewriting public datasets, including The-Stack-v2 and Finemath-4+, enhancing quality through systematic filtering and rewriting processes.

**Size**: 16.1 billion tokens for SwallowCode, 2.3 billion tokens for SwallowMath

**Format**: N/A

**Annotation**: Data was enriched without traditional filtering, focusing on transformation and utility maximization.

## 🔬 Methodology

**Methods**:
- Data Rewriting
- Data Filtering

**Metrics**:
- pass@1

**Calculation**: Metrics are calculated by evaluating model performance on benchmarks like HumanEval and GSM8K.

**Interpretation**: Higher metrics indicate better LLM performance in generating code snippets and mathematical solutions.

**Baseline Results**: Continuous pre-training with benchmarks led to significant improvements, with +17.0 on HumanEval for SwallowCode.

**Validation**: Model performance was validated against multiple benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Llama 3.3 Community License

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
