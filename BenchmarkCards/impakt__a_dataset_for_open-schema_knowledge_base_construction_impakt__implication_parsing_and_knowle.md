# ImPaKT: A Dataset for Open-Schema Knowledge Base Construction (ImPaKT: Implication Parsing and Knowledge Extraction)

## 📊 Benchmark Details

**Name**: ImPaKT: A Dataset for Open-Schema Knowledge Base Construction (ImPaKT: Implication Parsing and Knowledge Extraction)

**Overview**: A dataset for open-schema information extraction consisting of around 2,500 text snippets from the C4 corpus in the shopping domain (product buying guides), professionally annotated with extracted attributes, types, attribute summaries (attribute schema discovery), many-to-one relations between compound and atomic attributes, and implication relations. Released to support training semantic parsers for information extraction and open-schema semistructured automated knowledge base construction.

**Data Type**: text (annotated text snippets with coarse attributes, atomic attributes, attribute summaries, types, and implication relations)

**Domains**:
- Natural Language Processing
- E-commerce (Shopping/Retail)

**Similar Benchmarks**:
- MA VE
- MAE
- ConceptNet
- OpenIE
- Universal Schema

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: Provide training data for semantic parsers to perform open-schema information extraction and semistructured automated knowledge base construction, emphasizing attribute extraction, attribute summarization/schema discovery, and implication relation annotation in the shopping domain.

**Target Audience**:
- Researchers
- Model developers
- Practitioners building knowledge bases or semantic parsers

**Tasks**:
- Attribute Discovery
- Implication Parsing

**Limitations**: Experiments in the paper are restricted to atomic implications; the dataset is drawn from the shopping domain (buying guides), which may limit generality to other domains.

## 💾 Data

**Source**: 2,489 text snippets sampled from the C4 corpus (shopping domain / product buying guides). Candidate buying guide URLs were drawn from a non-public corpus annotated with Google Product Category taxonomy and filtered to create the buying guide corpus.

**Size**: 2,489 snippets; 5,655 coarse attributes; 6,117 atomic attributes; 3,719 implications; 3,587 atomic implications

**Format**: N/A

**Annotation**: Manual annotation by a team of 5-10 professional annotators over multiple rounds with correction cycles. Annotation includes coarse (possibly compound) attributes with summaries, splitting into atomic attributes with types and summaries, mapping of compound-to-atomic attributes, and implication relations grounded in snippet text. Annotator instructions and examples provided (see appendices).

## 🔬 Methodology

**Methods**:
- Manual human annotation (coarse attributes, atomic attribute splitting/typing, summaries, implications)
- Automated candidate generation using a T5-like classifier (trained on initial 500 labeled sentences) to select sentences likely containing implications
- Model fine-tuning: UL2 20B parameter model fine-tuned on seq2seq tasks (attribute discovery and implication parsing) using a seq2seq encoding
- Knowledge base aggregation (counts as confidence) and Pointwise Mutual Information (PMI) for associations
- Human evaluation: Likert-scale rater judgments of implication precision/directionality

**Metrics**:
- Precision (human-rated implication precision)
- Pointwise Mutual Information (PMI) for attribute co-occurrence
- Likert-scale rater judgments (1-5) for implication quality and directionality

**Calculation**: Parsed implications aggregated across the corpus; the count of occurrences of an implication treated as a confidence score and top 100 most confident implications selected for evaluation. PMI calculated between attribute pairs across parsed attributes. Human raters judged each candidate implication on a 1-5 Likert scale; examples were duplicated and multiple raters used; final evaluation used selected raters based on control questions.

**Interpretation**: Likert ratings interpret implication strength/directionality: 1 = Given A, B must necessarily be true; 2 = Given A, B is likely to be true; 3 = A and B usually not related; 4 = Given A, B is not likely to be true; 5 = Not enough information. Good performance is reflected by higher counts of ratings 1 or 2 in the model-indicated direction versus the reverse.

**Baseline Results**: Base model: publicly available UL2 20B fine-tuned on task mixture; no standard numeric baseline metrics like Accuracy/F1 are reported in the paper (evaluation reported via human rater judgments and comparative PMI results).

**Validation**: Human evaluation by multiple raters: 9 raters initially provided annotations (examples duplicated 3x), then 4 raters were selected based on control question performance for final evaluation. IID evaluation set used during finetuning convergence. Aggregated counts and human judgments used to validate precision and directionality of extracted implications.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
