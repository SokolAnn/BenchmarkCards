# BIRD (BIg Bench for Large-Scale Database Grounded Text-to-SQLs)

## 📊 Benchmark Details

**Name**: BIRD (BIg Bench for Large-Scale Database Grounded Text-to-SQLs)

**Overview**: BIRD is a large-scale cross-domain text-to-SQL benchmark emphasizing database values. It contains 12,751 text-to-SQL pairs over 95 databases (total size 33.4 GB) spanning 37 professional domains. BIRD highlights challenges of noisy/dirty database values, external knowledge grounding between natural language questions and database values, and SQL execution efficiency, and introduces a Valid Efficiency Score (VES) metric to evaluate efficiency of generated SQLs.

**Data Type**: text-to-SQL pairs (natural language questions and SQL queries) and tabular (relational database) files

**Domains**:
- Natural Language Processing
- Database Systems
- Healthcare
- Sports
- Politics
- Blockchain

**Languages**:
- English

**Similar Benchmarks**:
- SPIDER
- WikiSQL
- KaggleDBQA
- EHRSQL
- SEDE
- MIMICSQL

**Resources**:
- [Resource](https://bird-bench.github.io/)
- [GitHub Repository](https://github.com/AlibabaResearch/DAMO-ConvAI/tree/main/bird)
- [Resource](https://www.kaggle.com/)
- [Resource](https://relational.fit.cvut.cz/)
- [Resource](https://arxiv.org/abs/2305.03111)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large-scale, cross-domain text-to-SQL benchmark that better reflects real-world settings by focusing on large and noisy database values, external knowledge grounding, and SQL execution efficiency, thereby narrowing the gap between academic study and practical applications.

**Target Audience**:
- Natural Language Processing researchers
- Database Systems researchers
- Model developers
- Industry practitioners

**Tasks**:
- Text-to-SQL (Semantic Parsing)
- Question Answering over relational databases
- SQL efficiency/optimization evaluation

**Limitations**: Double-blind annotation is resource-intensive. SQLite is chosen as the primary SQL codebase, which presents difficulties in fetching Query Execution Plans (QEP) for precise efficiency computation and adapting to different SQL syntaxes; future work will include PostgreSQL and MySQL versions.

## 💾 Data

**Source**: Databases collected and processed from three sources: 32% from Kaggle, 48% from CTU Prague Relational Learning Repository (https://relational.fit.cvut.cz/), and 20% created by acquiring open tables, synthesizing and standardizing schemas. Total: 95 databases (69 train, 11 dev, 15 test). Questions and SQLs collected via crowdsourcing with expert supervision.

**Size**: 12,751 examples; 95 databases; total size 33.4 GB; recommended splits: 9,428 training instances, 1,534 development instances, 1,789 hidden test instances

**Format**: SQLite databases, database description CSV files, and paired natural language question / SQL annotations (provided as dataset files)

**Annotation**: Crowdsourced annotation with double-blind SQL annotation; question annotators (11 native English speakers) and SQL annotators (database engineers and DB students); expert examination for SQL validness and text-knowledge-SQL alignment; external knowledge evidence sentences collected and recorded for each SQL; annotation platform: Alibaba-Appen (internal)

## 🔬 Methodology

**Methods**:
- Fine-tuning (FT) with T5 family
- In-context learning (ICL) with large language models (e.g., Codex, ChatGPT (gpt-3.5-turbo), Claude-2, GPT-4, Palm-2)
- Two-stage optimization (semantic parsing followed by SQL optimization) for efficiency analysis

**Metrics**:
- Execution Accuracy (EX)
- Valid Efficiency Score (VES)

**Calculation**: Execution Accuracy (EX) is the proportion of examples where the executed results of predicted and ground-truth SQLs are identical: EX = (1/N) * Σ 1(Vn = V̂n). Valid Efficiency Score (VES) measures efficiency of valid SQLs: VES = (1/N) * Σ 1(Vn = V̂n) * R(Yn, Ŷn), where R(Yn, Ŷn) = sqrt(E(Yn) / E(Ŷn)); E(·) measures absolute execution efficiency (in BIRD primarily running time). VES is computed using average runtimes after running each SQL 100 times and dropping outliers.

**Interpretation**: Higher EX indicates more accurate SQL generation (matching execution results). VES combines correctness and relative execution efficiency: only valid (correct-execution) SQLs contribute, and higher VES indicates both correct and more efficient queries relative to ground truth.

**Baseline Results**: Selected results reported in the paper: Execution Accuracy (Testing w/ knowledge): GPT-4 = 54.89% (GPT-4 + DIN-SQL = 55.90%); Human performance (Testing w/ knowledge) EX = 92.96%. Valid Efficiency Score (Testing w/ knowledge): GPT-4 = 60.77; GPT-4 + DIN-SQL = 59.44; Human VES = 90.27. (Full tables provided in the paper: Table 2 and Table 3.)

**Validation**: Double-blind annotation: two independent SQL annotators produce SQLs for the same question, executed and compared; mismatches resolved with experts until consensus. Experts verify SQL executability (non-NULL results) and text-knowledge-SQL alignment. A hidden test set of 15 curated databases is used to avoid data leakage; runtime-based efficiency metrics use 100 runs per SQL and outlier removal.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Privacy
- Intellectual Property
- Data Laws
- Misuse

**Atlas Risks**:
- **Accuracy**: Data contamination
- **Data Laws**: Data usage restrictions
- **Intellectual Property**: Data usage rights restrictions
- **Misuse**: Improper usage

**Demographic Analysis**: Some questions mention ages and genders for capability testing; no demographic performance breakdown is provided.

**Potential Harm**: ['Potential improper commercial use of ample database values (authors state concern about abuse and therefore release under CC BY-NC 4.0)', 'Data leakage / contamination (authors explicitly avoid leakage via hidden test set)']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Authors state that the dataset contains no confidential data, sensitive data has been processed, individuals are not identifiable, and annotators were notified and consented; an ethical review process was conducted (no specific regulations such as GDPR or CCPA are named).

**Data Licensing**: CC BY-NC 4.0 (authors state the dataset is distributed under CC BY-NC 4.0).

**Consent Procedures**: Annotators were notified, consented to participation, and were compensated (question annotators $0.6 per validated question, SQL annotators $1 per SQL); no mechanism to revoke consent is provided (authors state 'No').

**Compliance With Regulations**: Ethical review processes were conducted and concerns about sensitive or political content were addressed during review; no specific legal/regulatory frameworks (e.g., GDPR, CCPA) are explicitly cited.
