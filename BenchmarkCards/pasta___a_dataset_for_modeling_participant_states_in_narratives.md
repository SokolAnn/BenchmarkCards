# PASTA : A Dataset for Modeling PArticipant STAtes in Narratives

## 📊 Benchmark Details

**Name**: PASTA : A Dataset for Modeling PArticipant STAtes in Narratives

**Overview**: This dataset contains inferable participant states; a counterfactual perturbation to each state; and the changes to the story that would be necessary if the counterfactual were true. We introduce three state-based reasoning tasks that test for the ability to infer when a state is entailed by a story, to revise a story conditioned on a counterfactual state, and to explain the most likely state change given a revised story.

**Data Type**: text (story / inferred state / counterfactual state / revised story 4-tuples)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TIME-TRAVEL
- GLUCOSE
- PROPARA
- WIQA

**Resources**:
- [GitHub Repository](https://github.com/StonyBrookNLP/pasta)
- [Resource](https://arxiv.org/abs/2208.00329)

## 🎯 Purpose and Intended Users

**Goal**: Enable modeling of unstated participant states in narratives and evaluate models' ability to (1) infer unstated participant states, (2) revise stories so a counterfactual state becomes inferable, and (3) generate the state change explaining differences between original and revised stories.

**Tasks**:
- Story State Inference (classification)
- Story Revision for Counterfactual States (generative story revision)
- State Change Generation (generative state-pair generation)

**Limitations**: N/A

## 💾 Data

**Source**: Stories from the extended ROCStories corpus (Mostafazadeh et al., 2016); annotations collected via crowdsourcing on Amazon Mechanical Turk with expert review.

**Size**: 10,743 examples (8,476 train, 1,350 validation, 917 test); 5,028 unique stories

**Format**: N/A

**Annotation**: Crowdsourced via Amazon Mechanical Turk (each story annotated by three workers), followed by a two-stage quality control: worker selection criteria and expert review to identify proficient workers; final dataset composed of accepted annotations from proficient workers and expert-accepted responses.

## 🔬 Methodology

**Methods**:
- Automated metrics (BERTScore, GLEU, ROUGE-L)
- Human evaluation (Likert scales thresholded to binary for inferability and other binary judgments)
- Model-based evaluation (fine-tuning T5, BERT, RoBERTa; few-shot GPT-3 prompting)

**Metrics**:
- Accuracy
- Contrastive Accuracy
- BERTScore
- GLEU
- ROUGE-L
- Gwet's Agreement Coefficient (inter-annotator agreement)

**Calculation**: Accuracy = percent of correct predictions. Contrastive Accuracy = model receives credit only if it correctly predicts inferability for both the inferred and counterfactual states for a story. BERTScore/GLEU/ROUGE-L are computed between model outputs and references for generative tasks. Human evaluations use 5-point Likert scales thresholded to binary labels for inferability; acceptability for revision requires both 'Inferable' and 'Logical' criteria to be satisfied. Inter-annotator agreement measured using Gwet's coefficient.

**Interpretation**: Higher Accuracy and Contrastive Accuracy indicate better performance on Story State Inference (closer to human performance is better). For generative tasks, higher human-evaluated acceptability (both inferable and logical) indicates better outputs; automatic metrics (BERTScore, GLEU, ROUGE-L) provide auxiliary signals but BERTScore correlates best with human judgments and automatic metrics have limited correlation, so human evaluation is recommended.

**Baseline Results**: Story State Inference: RoBERTa-large achieved 89.1% Accuracy and 83.7% Contrastive Accuracy; T5-large 83.1% / 75.3%; BERT-base 73.8% / 64.0%; Human performance reported as 96.9% Accuracy and 94.2% Contrastive Accuracy (Table 3). Story Revision for Counterfactual States (human acceptability): T5-large (fine-tuned) overall acceptability ~54% (generations satisfying inferable and logical criteria); GPT-3 few-shot acceptability lower (see Table 6). State Change Generation (human acceptability): T5-large (fine-tuned) ALL = 55.5%; GPT-3 few-shot ALL = 47.7% (Table 7). Automatic metrics for Story Revision (BERTScore/GLEU/ROUGE-L): T5-large BERTScore 82.1, GLEU 73.5, ROUGE-Lsum 81.7 (Table 8a). For State Change Generation: T5-large BERTScore 56.9, GLEU 13.4, ROUGE-L 32.4 (Table 8b).

**Validation**: Train/validation/test splits provided (8,476/1,350/917) with no story overlap between splits. Expert-reviewed subset used to create the test set. Human evaluation conducted on random samples (e.g., 200 4-tuples -> 800 inference instances); inter-annotator agreement measured using Gwet's coefficient. Two-stage MTurk worker filtering plus expert review to ensure annotation quality.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Annotators were required to reside in USA or Canada to help prevent language-based artifacts (explicitly stated in data collection/quality control).

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: The project was reviewed and approved by the local IRB for human subjects research.
