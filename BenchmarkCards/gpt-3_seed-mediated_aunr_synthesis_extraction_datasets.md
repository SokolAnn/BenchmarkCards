# GPT-3 seed-mediated AuNR synthesis extraction datasets

## 📊 Benchmark Details

**Name**: GPT-3 seed-mediated AuNR synthesis extraction datasets

**Overview**: An approach using the GPT-3 language model to extract structured multi-step seed-mediated growth procedures and outcomes for gold nanorods from unstructured scientific text. GPT-3 prompt completions are fine-tuned to predict JSON-formatted synthesis templates from input paragraphs; the final dataset consists of 11,644 extracted entities from 1,137 papers, yielding 268 papers with at least one complete seed-mediated gold nanorod growth procedure and a total of 332 complete procedures.

**Data Type**: text (scientific article paragraphs) mapped to structured JSON synthesis templates (paragraph-to-JSON template pairs)

**Domains**:
- Materials Science
- Chemistry
- Natural Language Processing

**Similar Benchmarks**:
- Text-mined dataset of gold nanoparticle synthesis procedures, morphologies, and size entities
- Text-mined dataset of inorganic materials synthesis recipes

**Resources**:
- [Resource](https://doi.org/10.6084/m9.figshare.19719310.v3)
- [Resource](https://arxiv.org/abs/2304.13846)

## 🎯 Purpose and Intended Users

**Goal**: Automatically extract fully-structured seed-mediated gold nanorod synthesis procedures (seed solution, growth solution) and outcomes (nanorod measurements) from unstructured scientific text to produce a reusable JSON-formatted dataset for downstream analysis, search, and modeling.

**Target Audience**:
- Materials Scientists
- Chemists
- Data Scientists
- Machine Learning Researchers

**Tasks**:
- Named Entity Recognition
- Relation Extraction
- Information Extraction
- Question Answering
- Template Filling

**Limitations**: Dataset focuses specifically on seed-mediated gold nanorod growth, sacrificing generality to achieve specificity. The model struggles to identify precursors not present in the training set. Conflicts and repetitions can arise when merging paragraph-level templates by article due to lack of cross-paragraph context. Some complex synthesis methods (e.g., three-step overgrowth procedures) cause extraction errors and require new templates or additional annotation.

## 💾 Data

**Source**: Derived from the gold nanoparticle synthesis protocol and outcome database developed by Cruse et al., themselves built from the full-text database developed by Kononova et al., accessed via text- and data-mining agreements with scientific journal publishers.

**Size**: 11,644 extracted entities; 1,137 papers; 2,969 paragraphs processed; 268 papers with at least one complete seed-mediated gold nanorod growth procedure; 332 complete procedures. (Training annotations: 240 papers / 661 paragraphs; Testing set: 40 papers / 117 paragraphs.)

**Format**: JSON (list with one element per article; paragraph-level templates merged by article; post-processed JSON with list-of-dictionaries structure for values)

**Annotation**: Manual annotation with machine assistance: initial zero-shot GPT-3 question-answering completions were corrected by annotators to produce training templates. A single annotator (with machine assistance) produced the training annotations; three additional researchers were consulted for consensus on ambiguous cases. Iterative prediction-correction-fine-tuning cycles expanded the annotated set.

## 🔬 Methodology

**Methods**:
- Fine-tuned GPT-3 (OpenAI Davinci, 175B) for sequence-to-sequence template generation
- Zero-shot question-answering completions for initial template field population
- Iterative fine-tuning with corrected template examples
- Manual correction and annotation of model outputs

**Metrics**:
- Precision
- Recall
- F1 Score
- Transcription Accuracy
- Combined Accuracy (product of placement F1 and transcription accuracy)
- Adjusted F1

**Calculation**: Information placement evaluated by presence/absence of values in template fields (true positive, false positive, false negative, true negative) to compute precision, recall, and F1. Transcription accuracy computed only for true positive placements; numerical transcription scored with s(p;q) = 2 * min(p,q) / (p+q) (derived from absolute proportional difference), units must match exactly; modifiers (e.g., ">3 h") partially credited (half-correct) if modifier missed. Combined accuracy is the product of placement F1 and transcription accuracy.

**Interpretation**: High placement F1 (0.90) indicates reliable identification of which template fields should contain information; high transcription accuracy (0.96) indicates accurately extracted values when placement is correct. The combined adjusted F1 of 0.86 reflects overall simultaneous entity recognition and relation extraction performance. Primary source of error is incorrect placement of information rather than transcription of correctly placed information.

**Baseline Results**: Fine-tuned model achieved overall adjusted F1 (combined) of 86% on the testing dataset (40 papers, 117 paragraphs). Placement F1 overall 0.90; transcription accuracy 0.96. Prior work reported overall accuracy of 51% for extracting all recipe items in solid-state synthesis extraction. Prior BiLSTM-based NER (Cruse et al.) precursor detection F1 was 90% (without distinguishing seed/growth solutions). MatBERT NER reported morphology and size extraction F1-scores of 70%, 69%, and 91% (for different measurements) in prior work.

**Validation**: Evaluated on a corrected testing dataset of 40 papers (117 paragraphs). Metrics computed as described (placement and transcription). Post-processing applied for evaluation (splitting lists, resolving repetitions). Outlier detection (elliptic envelope) followed by manual verification used in dataset analyses.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
