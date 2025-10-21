# MANtIS (multi-domain information seeking dialogues dataset)

## 📊 Benchmark Details

**Name**: MANtIS (multi-domain information seeking dialogues dataset)

**Overview**: A large-scale dataset containing multi-domain and grounded information-seeking dialogues (extracted from Stack Exchange) that fulfills the authors' dataset desiderata. The paper introduces MANtIS and provides baseline results for conversation response ranking and user intent prediction.

**Data Type**: text (multi-turn information-seeking dialogues grounded with document hyperlinks)

**Domains**:
- apple
- askubuntu
- dba
- diy
- electronics
- english
- gaming
- gis
- physics
- scifi
- security
- stats
- travel
- worldbuilding

**Languages**:
- N/A

**Similar Benchmarks**:
- SCS
- MISC
- CCPE-M
- Frames
- KVRET
- CoQA
- MultiWOZ
- QuAC
- WoW
- ShARC
- MSDialog
- DSTC-7-SS
- UDC

**Resources**:
- [Resource](https://guzpenha.github.io/MANtIS/)

## 🎯 Purpose and Intended Users

**Goal**: Provide a large-scale, multi-domain, grounded dataset for evaluating conversational search systems and to supply baselines for conversation response ranking and user intent prediction.

**Target Audience**:
- Information Retrieval researchers
- Natural Language Processing researchers
- Dialogue Systems researchers
- Conversational search researchers

**Tasks**:
- Conversation Response Ranking
- Conversation Response Generation
- User Intent Prediction

**Limitations**: The authors applied stringent inclusion criteria: only 4.77% of all question-answering threads were included in the final dataset. Grounding via hyperlinks was manually verified on a sample and found to lead to a grounding document in 88% of sampled conversations.

## 💾 Data

**Source**: Stack Exchange question-answering threads (extracted from Stack Exchange data dump)

**Size**: 80,324 conversations

**Format**: N/A

**Annotation**: Manual annotation by two expert annotators for a sampled subset: 1,356 conversations resulting in 6,701 labeled utterances with nine user intent labels. Inter-annotator agreement (Krippendorff's alpha) = 0.71. Final-seeker positive feedback was verified via manual sampling (1,400 conversations) and VADER sentiment thresholding.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Baseline model evaluation (non-neural and neural models)
- Time-based train/dev/test split

**Metrics**:
- Mean Average Precision (MAP)
- Normalized Discounted Cumulative Gain at 10 (nDCG@10)
- Precision
- F1 Score (Micro)
- F1 Score (Macro)
- Krippendorff's alpha

**Calculation**: Conversation response ranking: create conversation contexts and treat the actual reply as ground truth; sample negative replies using BM25 from top-1K ranked replies to produce MANtISCRR10 (10 negatives) and MANtISCRR50 (50 negatives). Default time-based split: 70% oldest training, 15% development, 15% test. Ranking results averaged over 5 runs. User intent prediction: multi-label classification on manually labeled subset; evaluated with 10-fold cross-validation, reporting averages of Precision, Micro F1, Macro F1.

**Interpretation**: Authors report that fine-tuned BERT is the best performing model for both tasks. For conversation response ranking, models perform well with 10 candidate replies but degrade severely with 50 candidates, indicating challenges in realistic large-scale settings. For intent prediction, BERT substantially outperforms other baselines.

**Baseline Results**: Conversation response ranking (test set averages): MANtISCRR10 - BM25: MAP 0.317, nDCG@10 0.475; DMN: MAP 0.683 (std .02), nDCG@10 0.761 (std .015); BERT: MAP 0.733 (std .003), nDCG@10 0.799 (std .002). MANtISCRR50 - BM25: MAP 0.163, nDCG@10 0.195; DMN: MAP 0.430 (std .03), nDCG@10 0.512 (std .038); BERT: MAP 0.519 (std .005), nDCG@10 0.583 (std .005). User intent prediction (10-fold CV averages, Table 5): Logistic Regression Precision 0.486 (std .017), F1-Micro 0.469 (std .014), F1-Macro 0.348 (std .014); SVM Precision 0.532 (std .021), F1-Micro 0.534 (std .019), F1-Macro 0.455 (std .018); BiGRU Precision 0.574 (std .016), F1-Micro 0.563 (std .015), F1-Macro 0.478 (std .027); AdaBoost Precision 0.641 (std .015), F1-Micro 0.585 (std .012), F1-Macro 0.480 (std .010); GradientBoosting Precision 0.657 (std .017), F1-Micro 0.611 (std .013), F1-Macro 0.491 (std .011); BERT Precision 0.790 (std .013), F1-Micro 0.750 (std .015), F1-Macro 0.591 (std .030).

**Validation**: Grounding verification: sampled 150 conversations, 88% links led to grounding documents. Positive feedback verification: sampled 1,400 conversations and used VADER sentiment to derive site-specific thresholds; conversations below threshold discarded. Ranking baselines averaged over 5 runs. User intent prediction evaluated via 10-fold cross-validation. Time-based 70/15/15 split for main dataset.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
