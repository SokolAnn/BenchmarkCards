# This Prompt is Measuring <MASK>: Evaluating Bias Evaluation in Language Models

## 📊 Benchmark Details

**Name**: This Prompt is Measuring <MASK>: Evaluating Bias Evaluation in Language Models

**Overview**: A taxonomy-based evaluation framework that analyses the use of prompts and templates to assess bias in language models. The paper develops a taxonomy of attributes (conceptualisation and operationalisation) grounded in measurement modelling, and applies this taxonomy to annotate 90 bias tests drawn from 77 papers to reveal reporting gaps, threats to validity, and areas under-researched; it offers guidance for designing and documenting bias tests.

**Data Type**: text (prompts/templates and annotation metadata)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- StereoSet
- Crows-pairs
- Equity Evaluation Corpus (EEC)
- RealToxicityPrompts

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: Create and apply a taxonomy grounded in measurement modelling to analyse prompt/template-based bias tests for language models, identify threats to validity and gaps in current practice, and provide guidance for better design and documentation of bias tests.

**Target Audience**:
- ML Researchers
- NLP Practitioners
- Model Developers

**Tasks**:
- Bias Evaluation
- Text Generation Evaluation
- Prompt-based Evaluation

**Limitations**: Our search was conducted exclusively in English, and we may have missed relevant papers written in other languages; this may have influenced the heavy English skew in our data. Some of the annotations of attributes and choices in this taxonomy rely on subjective judgements, particularly with regards to the clarity of conceptualisations of bias, desired outcomes, and justifications of proxy choices.

**Out of Scope Uses**:
- We exclude any that have been fine-tuned for a discriminative task rather than a generative one.
- In annotation, we excluded papers focusing on other types of bias (e.g., inductive), papers that briefly mention bias as a potential concern but do not focus on it, and papers that apply an existing bias test with no changes.

## 💾 Data

**Source**: Annotations produced by the authors: 90 bias tests annotated from a final set of 77 papers identified via searches of the ACL Anthology and Semantic Scholar (initial pool of 406 papers, filtered to 77 relevant papers).

**Size**: 77 papers; 90 bias tests

**Format**: N/A

**Annotation**: Manual annotation by the paper's authors using the developed taxonomy; taxonomy refined iteratively with re-annotation on four occasions; 10% of Anthology papers assigned to multiple annotators to identify disagreements which were discussed and used to refine the taxonomy; remaining papers annotated by a single author with aggregate statistics examined for annotator skews.

## 🔬 Methodology

**Methods**:
- Manual annotation
- Taxonomy-based analysis
- Quantitative analysis of annotated attributes

**Metrics**:
- Counts and percentages of taxonomy attribute occurrences (reported across the 90 bias tests)

**Calculation**: Quantitative analysis is done at the level of individual bias tests (90); percentages and counts of taxonomy attribute selections are computed and reported.

**Interpretation**: Results are interpreted to identify common patterns, reporting gaps, threats to measurement validity (face, content, convergent, predictive, consequential, ecological), and areas under-researched; examples of mismatches between conceptualisation and operationalisation are highlighted to assess validity and reliability of bias tests.

**Validation**: 10% of Anthology papers were assigned to multiple annotators and disagreements were discussed; taxonomy was refined through iterative re-annotation (four occasions) and remaining papers were annotated by a single author; aggregate statistics by annotator were examined to address skews.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Governance
- Robustness
- Societal Impact

**Atlas Risks**:
- **Governance**: Lack of data transparency, Unrepresentative risk testing, Lack of testing diversity, Incomplete usage definition
- **Fairness**: Data bias, Output bias
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: Majority of bias tests examined English only (87%); gender is the most common demographic studied (38%), with an overwhelming focus on binary gender in many works; multilingual and low-resource language coverage is limited.

**Potential Harm**: ['stereotypes', 'toxic content generation', 'erasure bias (under-representation of marginalised groups)', 'harm to affected/marginalised communities (consequential harms from measurements or deployments)']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
