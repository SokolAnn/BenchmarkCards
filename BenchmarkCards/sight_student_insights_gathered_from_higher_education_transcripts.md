# SIGHT (Student Insights Gathered from Higher Education Transcripts)

## 📊 Benchmark Details

**Name**: SIGHT (Student Insights Gathered from Higher Education Transcripts)

**Overview**: SIGHT is a large dataset of 288 math lecture transcripts and 15,784 comments collected from the Massachusetts Institute of Technology OpenCourseWare (MIT OCW) YouTube channel. The paper also develops a 9-category annotation rubric for student feedback and presents best practices for using large language models to scale annotation.

**Data Type**: text (lecture transcripts and user comments)

**Domains**:
- Education
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Multi-modal lecture presentations dataset
- Setsum

**Resources**:
- [GitHub Repository](https://github.com/rosewang2008/sight)
- [Resource](https://arxiv.org/abs/2306.09343)
- [Resource](https://ocw.mit.edu/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large dataset of lecture transcripts and annotated YouTube comments (SIGHT) to study student feedback and to develop / evaluate scalable annotation methods (using LLMs) for qualitative feedback classification to improve pedagogy.

**Target Audience**:
- Education researchers
- Natural Language Processing researchers
- Educators
- Qualitative researchers

**Tasks**:
- Text Classification
- Multi-label Classification
- Qualitative Analysis

**Limitations**: Comments may not reflect real student feedback (public YouTube posters); selection bias in lecture sources (most successful offerings); only English comments analyzed; only a small subsample of comments was manually annotated (~280 comments / approximately 2% diagnostic subset); rubric may not capture non-English feedback.

**Out of Scope Uses**:
- The dataset should not be used for commercial purposes.
- Unacceptable use cases include any attempts to identify users or use the data for commercial gain.

## 💾 Data

**Source**: 288 math lecture transcripts and 15,784 user comments collected from the Massachusetts Institute of Technology OpenCourseWare (MIT OCW) YouTube channel using the Google YouTube API and YouTube Data API V3. Lecture audio was transcribed with OpenAI's Whisper large-v2 model. Comments are top-level comments; user IDs are not tracked and usernames mentioned with '@' are anonymized to '[USERNAME]'.

**Size**: 10 courses, 288 lectures, and 15,784 comments

**Format**: N/A

**Annotation**: Manual annotation by two co-authors on a sample dataset (reported as 280 comments in main text) using a 9-category rubric; full dataset annotations were produced automatically using GPT-3.5 (gpt-3.5-turbo) with binary per-category prompts (zero-shot, 3-shot, and 3-shot with reasoning).

## 🔬 Methodology

**Methods**:
- Human evaluation (two human annotators on a sample dataset)
- Automated metrics (Cohen's kappa for inter-rater reliability / IRR)
- Qualitative analysis (grounded theory for rubric development)
- Model-based evaluation (LLM annotation using GPT-3.5; zero-shot, k-shot, k-shot with reasoning prompting)

**Metrics**:
- Cohen's kappa
- Inter-rater reliability (IRR)
- Human-model agreement (Cohen's kappa)
- Category percentage distribution
- Annotation cost per comment (reported cost: $0.002 per comment for scaled annotation)

**Calculation**: Cohen's kappa was computed to measure inter-rater reliability within human annotators and between human-model pairs for each rubric category. Human IRR (reference) and average human-model IRR are reported for 0-shot, 3-shot, and 3-shot with reasoning settings (Table 3).

**Interpretation**: Human IRR reached substantial to perfect agreement (>= 0.70) across categories. Categories with higher human agreement (> 0.9 IRR) also display higher human-model agreement (> 0.7), while categories with lower human agreement (0.7-0.8 IRR) correspond to lower human-model agreement (~0.3-0.5). Higher kappa indicates better agreement; lower values indicate poorer agreement and more model failure modes.

**Baseline Results**: Human IRR (Cohen's kappa) by category (human row in Table 3): general 0.75, confusion 0.91, pedagogy 0.79, setup 0.95, personal 0.74, clarification 0.83, gratitude 0.92, nonenglish 0.94, na 0.74. GPT-3.5 (gpt-3.5-turbo) 0-shot human-model Cohen's kappa by category (0-shot row in Table 3): general 0.48, confusion 0.72, pedagogy 0.35, setup 0.85, personal 0.32, clarification 0.48, gratitude 0.92, nonenglish 0.87, na 0.65. The paper also reports 3-shot and 3-shot with reasoning results in Table 3.

**Validation**: Validation included dual human annotation of a sample dataset (reported as 280 comments) with computation of Cohen's kappa for human IRR. The authors conducted a diagnostic study on a small, randomly selected subset of the dataset comprising approximately 2% of the comments and manually inspected model errors to analyze failure modes.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Bias
- Legal
- Misuse
- Governance

**Atlas Risks**:
- **Privacy**: Personal information in data, Exposing personal information
- **Accuracy**: Unrepresentative data
- **Data Laws**: Data usage restrictions
- **Misuse**: Nonconsensual use, Improper usage
- **Intellectual Property**: Data usage rights restrictions
- **Governance**: Unrepresentative risk testing

**Demographic Analysis**: N/A

**Potential Harm**: ['Identify student confusion and pedagogical weaknesses in lecture content', 'Privacy violations from attempts to identify commenters or expose personal information', 'Improper or commercial use of data (authors explicitly prohibit commercial use)']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The authors do not track user IDs and anonymize usernames mentioned with '@' by replacing them with '[USERNAME]'. The authors state they are committed to protecting the privacy and confidentiality of individuals who contributed comments and recommend researchers take steps to mitigate risks or harms.

**Data Licensing**: The dataset is released under MIT's Creative Commons License and is intended for research purposes only; the dataset should not be used for commercial purposes.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
