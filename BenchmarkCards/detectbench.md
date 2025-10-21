# DetectBench

## 📊 Benchmark Details

**Name**: DetectBench

**Overview**: DetectBench, a reading comprehension dataset designed to assess a model’s ability to jointly ability in key information detection and multi-hop reasoning when facing complex and implicit information.

**Data Type**: text (multiple-choice question-answering pairs with paragraph context)

**Domains**:
- Natural Language Processing
- Information Retrieval
- Commonsense Reasoning

**Languages**:
- Chinese

**Similar Benchmarks**:
- HotPotQA
- FEVER
- RECLOR
- HellaSwag

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate model proficiency in identifying and reasoning from clues within a complex context to answer questions (joint abilities in key information detection and multi-hop reasoning).

**Tasks**:
- Question Answering
- Machine Reading Comprehension
- Information Extraction (Key information detection)
- Multi-hop Reasoning

**Limitations**: When juxtaposed with the complexity and breadth of information encountered in real-world scenarios, the data encompassed within detective reasoning puzzles appears markedly condensed.

**Out of Scope Uses**:
- Questions that are not ethical or have sensitive matters.
- Questions requiring visual or auditory information for support.
- Questions that are anti-logical, have unreasonable answers, or are overly diverse.
- Questions requiring extensive symbolic logic or domain knowledge.
- Questions with overly obvious key information.

## 💾 Data

**Source**: Collected detective puzzles from open-source platforms and rewritten into DetectBench; initial processing (question selection and rewriting) assisted by GPT-4-turbo-1106-preview; manual verification by annotators.

**Size**: 3,928 examples (396 train + 1,928 dev + 1,604 test); average paragraph length 190 tokens

**Format**: JSON (fields: Context, Question, Options, Answer, Clue Graph)

**Annotation**: Manual annotation and verification by five annotators (authors of the paper); GPT-4-turbo-1106-preview assisted in selection and rewriting; manual screening, adjustment, and creation of "Clue Graph" and "Key Information from Context".

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation
- Prompt engineering experiments
- Fine-tuning experiments

**Metrics**:
- Accuracy
- ROUGE-L

**Calculation**: Accuracy assesses correctness in multiple-choice answer selection (denoted as Acc). ROUGE-L is used to measure overlap for generated key information extraction (KeyInfo) when requiring models to generate content snippets directly from context.

**Interpretation**: Higher Accuracy indicates better answer selection performance; higher ROUGE-L indicates better key information extraction. The paper reports human average Accuracy as a reference (Average Accuracy 74.1%, Top Accuracy 93.3%, Lowest Accuracy 53.3%) and states that performance in clue detection correlates with performance in answering questions.

**Baseline Results**: Baselines include GPT4-turbo, GPT3.5-turbo, Llama2-7b variants, GLM4, ChatGLM3 variants. Example reported results: GPT4-Turbo KeyInfo average accuracy around 40% (paper states "GPT4-Turbo’s average accuracy standing at 40%" for key information detection); Detective Thinking Prompt improved GPT4 Accuracy to 61.5% (Table 4 shows GPT4 Acc 61.5 with Detective Thinking Prompt).

**Validation**: Validation via manual verification: all GPT-4-processed questions underwent manual verification by five annotators to ensure uniqueness, reasonableness, and correctness; initial screening eliminated unreasonable or ambiguous questions; detail adjustments were performed to refine options, answers, and Clue Graphs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Ethical concerns
- Security

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: ['A benchmark concentrating on detective deduction puzzles is predisposed to encompass a multitude of sensitive subjects, including but not limited to homicides and thefts.', 'Models that undergo fine-tuning using benchmark data may inadvertently amplify security vulnerabilities.', 'There exists a risk that models might refuse responding to sensitive questions for security purposes, consequently disadvantaging models that prioritize higher security standards.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
