# FIXEVAL

## 📊 Benchmark Details

**Name**: FIXEVAL

**Overview**: FIXEVAL is a benchmark comprising of buggy code submissions to competitive programming problems and their corresponding fixes. FIXEVAL offers an extensive collection of unit tests to evaluate the correctness of model-generated program fixes and assess further information regarding time, memory constraints, and acceptance based on a verdict.

**Data Type**: text (buggy and fixed program pairs with unit test input-output files and verdicts)

**Domains**:
- Software Engineering

**Similar Benchmarks**:
- DeepFix
- Review4Repair
- Bug2Fix
- GitHub-Python
- IntroClass
- Refactory
- QuixBugs
- Defects4J

**Resources**:
- [GitHub Repository](https://github.com/FixEval/FixEval)
- [GitHub Repository](https://github.com/c2nes/javalang)
- [Resource](https://docs.python.org/3/library/tokenize.html)
- [Resource](https://docs.python.org/3/library/py_compile.html)
- [Resource](https://www.dropbox.com/sh/nx3tnilzqz7df8a/AAAYlTq2tiEHl5hsESw6-yfLa?dl=0)
- [Resource](https://atcoder.jp/posts/21)

## 🎯 Purpose and Intended Users

**Goal**: We introduce FIXEVAL, a context-aware program repair dataset that, along with unit tests, incorporates additional considerations—namely time and space complexity—to assess the functional correctness of repaired programs.

**Target Audience**:
- Machine Learning Researchers
- Program Repair Researchers
- Model Developers

**Tasks**:
- Program Repair
- Verdict-conditioned Program Repair
- Code Completion
- Code Editing
- Code Search
- Verdict Prediction
- Chain Edit Suggestion

**Limitations**: We acknowledge that fixing programming problem solutions does not reflect real-world software bugs from professional developers. We also acknowledge the potential threat to validity as all the unit tests weren’t manually validated.

**Out of Scope Uses**:
- Problems with many combinatorial equivalently valid outputs (constraint satisfaction problems) were removed and thus such problems are out-of-scope for FIXEVAL.

## 💾 Data

**Source**: Collected from CodeNet (programs solving AtCoder and Aizu Online Judge problems). Unit tests downloaded from AtCoder; submission paths grouped by user_id to form submission paths and pairs of unaccepted and accepted submissions form examples.

**Size**: Java: 2,718 problems (156k train, 44k valid, 43k test = 245k examples); Python: 2,439 problems (567k train, 301k valid, 243k test = 1,111k examples). FIXEVAL: 54M lines of code in Java and 61M lines of code in Python. Derived from 712,000 Java and 3,280,000 Python program submissions. From CodeNet, 6.5M submission paths were extracted. (All numbers stated in the paper.)

**Format**: Raw source code files and unit test input/output files organized per problem; programs tokenized using javalang for Java and the Python standard tokenize library.

**Annotation**: Paired each unaccepted submission (buggy code) with the user's accepted submission (fixed code). Unit tests are the publicly available AtCoder test cases manually created by problem setters (domain experts).

## 🔬 Methodology

**Methods**:
- Automated n-gram-based metrics
- Execution-based evaluation (unit-test execution over test suites)

**Metrics**:
- Exact Match
- BLEU
- Syntax Match
- Dataflow Match
- CodeBLEU
- Compilation Accuracy
- Pass@k
- Test Case Average (TCA@k)

**Calculation**: N-gram metrics: corpus-level BLEU, Exact Match, Syntax Match, Dataflow Match, CodeBLEU, and Compilation Accuracy using javac and py_compile. Execution-based: pass@k computed using the unbiased estimator following equation (1) with n=10 and k<=10; TCA@k computed as the average number of test cases passed per problem as defined in equation (2).

**Interpretation**: Pass@k is a strict measure where a problem is considered solved only if a generated sample passes all unit tests. TCA@k reports average test cases passed and allows partial credit for solutions that pass a subset of tests.

**Baseline Results**: Baseline experiments finetuned PLBART and CodeT5 on FIXEVAL. Example execution-based results (from Table IV): CodeT5 Java (verdict conditioned): pass@1=10.94, pass@3=18.77, pass@5=22.66, pass@10=27.96. CodeT5 Python (verdict conditioned): pass@1=7.32, pass@3=13.94, pass@5=17.47, pass@10=22.63. N-gram results and compilation accuracy reported in Table III (see paper tables for full numbers).

**Validation**: Stratified dataset splits based on problems (80-10-10 train/validation/test) with no overlapping problems or submissions across splits. All test and validation examples include test cases. For execution evaluation, two program pairs per problem from the test split were randomly selected and evaluated on all available test cases.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Governance

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Governance**: Incomplete usage definition

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
