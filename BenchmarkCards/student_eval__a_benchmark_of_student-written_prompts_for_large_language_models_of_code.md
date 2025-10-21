# STUDENT EVAL: A Benchmark of Student-Written Prompts for Large Language Models of Code

## 📊 Benchmark Details

**Name**: STUDENT EVAL: A Benchmark of Student-Written Prompts for Large Language Models of Code

**Overview**: STUDENT EVAL is a new Code LLM benchmark containing 1,749 student-written prompts for 48 programming problems, written by 80 beginning Python students (one semester of CS). It measures Code LLM performance when prompts are authored by non-expert beginning programmers and provides multiple prompts per problem to study prompt variability and reliability.

**Data Type**: student-written natural language prompts paired with expert-written unit tests and reference implementations (text)

**Domains**:
- Natural Language Processing
- Education
- Software Engineering

**Languages**:
- English

**Similar Benchmarks**:
- HumanEval
- MBPP
- DS-1000
- MathQA-Python

**Resources**:
- [Resource](https://huggingface.co/datasets/wellesley-easel/StudentEval)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate Code LLMs using prompts written by beginning programmers (students with one semester of Python) and to study how prompt wording and nondeterministic model sampling affect model success and user perceptions.

**Target Audience**:
- ML Researchers
- Model Developers
- Educators

**Tasks**:
- Code Generation
- Program Synthesis

**Limitations**: Students wrote prompts interactively while using a Codex model; prompts were authored only by beginning programmers and are not representative of prompts written by experienced programmers.

## 💾 Data

**Source**: Student-written prompts collected via an IRB-approved, lab-based study (Zoom) from 80 beginning CS students at Northeastern University, Wellesley College, and Oberlin College. Each problem includes a function signature, at least three test cases, a correct function implementation, and an expert-written problem description.

**Size**: 1,749 prompts for 48 programming problems; at least 14 prompts per problem; average ~36 prompts per problem; 80 student participants

**Format**: N/A

**Annotation**: Prompts are authored by students. Each problem includes expert-written unit tests and a correct function implementation. Test suites were validated using code coverage and mutation testing (MutPy).

## 🔬 Methodology

**Methods**:
- Automated evaluation using hidden unit tests
- Pass@1 metric with sampling
- Mutation testing for test-suite validation
- Coverage testing for test-suite validation
- Statistical analysis (mixed-effects regression)
- Embedding analysis and visualization (t-SNE, TF-IDF)

**Metrics**:
- Pass@1
- Mean pass@1
- Mutation Score
- Test Coverage

**Calculation**: Pass@1 is estimated by gathering 200 samples per prompt and computing the probability that a single sample passes all hidden unit tests. Mutation scores were computed using MutPy. Test coverage was measured to ensure tests achieve 100% code coverage per problem (3–4 tests per problem).

**Interpretation**: Higher pass@1 indicates better probability that a model will produce a correct solution on a single try. The benchmark highlights both mean performance and variability across multiple student-written prompts; an ideal model maximizes pass@1 and minimizes variability/unreliability.

**Baseline Results**: Table 1 (mean pass@1 rates on four STUDENT EVAL subsets): GPT-3.5-Turbo-0301: First Failure 10.86, Last Failure 12.41, First Success 44.84, Last Success 47.40, HumanEval 48.1. Replit-Code-v1 (2.7B): First Failure 3.84, Last Failure 2.83, First Success 33.62, Last Success 18.33, HumanEval 21.09. SantaCoder (1.1B): First Failure 2.08, Last Failure 2.11, First Success 30.87, Last Success 21.71, HumanEval 17.81. StarChat-Alpha (15.5B): First Failure 10.10, Last Failure 8.78, First Success 63.58, Last Success 51.06, HumanEval 30.03. StarCoderBase (15.5B): First Failure 7.82, Last Failure 6.74, First Success 65.28, Last Success 51.74, HumanEval 30.40.

**Validation**: Problems were validated by generating Codex outputs from function signatures and measuring pass@1 for signatures (mean pass@1 for signatures without docstrings = 0.0519, variance = 0.0364) to identify signature-leaky problems. Test suites achieve 100% code coverage (3–4 tests per problem) and were evaluated using mutation testing with MutPy; mutation scores below 90 were analyzed and explained (no mutations generated or technically correct mutations).

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Governance
- Societal Impact

**Atlas Risks**:
- **Robustness**: Hallucination
- **Governance**: Unrepresentative risk testing
- **Societal Impact**: Impact on education: bypassing learning

**Demographic Analysis**: Dataset collected from 80 beginning CS students who completed one semester of Python at Northeastern University, Wellesley College, and Oberlin College. No further demographic breakdowns (e.g., age, gender, race) are provided.

**Potential Harm**: The paper states that nondeterministic LLM sampling and unreliable prompts can mislead students about the effectiveness of their prompts, with implications for teaching (risk of bypassing learning or misinforming students).

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: IRB-approved study is reported. Specific anonymization procedures or privacy protections are not detailed in the paper.

**Data Licensing**: Not Applicable

**Consent Procedures**: Study was IRB-approved and participants were compensated ($50 gift card). Specific consent procedure details are not provided in the paper.

**Compliance With Regulations**: IRB approval is stated. No explicit mention of GDPR, CCPA, or other regulatory compliance is provided.
