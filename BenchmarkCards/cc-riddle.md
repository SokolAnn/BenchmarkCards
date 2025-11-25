# CC-Riddle

## 📊 Benchmark Details

**Name**: CC-Riddle

**Overview**: CC-Riddle is a large-scale question answering dataset of Chinese character riddles covering the majority of common simplified Chinese characters. It is constructed by web crawling human-written riddles, generating additional riddles with a fine-tuned BART model, and manual filtering, and is intended to evaluate language models' ability to solve Chinese character riddles (single-character solutions) that require glyph, meaning and pronunciation understanding.

**Data Type**: question-answering pairs (riddle description -> single-character solution)

**Domains**:
- Natural Language Processing
- Education
- Chinese Language Studies

**Languages**:
- Chinese

**Similar Benchmarks**:
- Riddlesense
- Cryptonite
- BirdQA

**Resources**:
- [GitHub Repository](https://github.com/pku0xff/CC-Riddle)
- [Resource](http://xh.5156edu.com/)
- [Resource](https://www.chnlib.com/miyuku/zimi/index.html)
- [Resource](https://www.cmy123.com/zmmy)
- [Resource](http://www.hydcd.com/baike/zimi.htm)
- [Resource](https://www.caimigu.com/zm/)
- [GitHub Repository](https://github.com/cjkvi/cjkvi-ids)
- [Resource](https://hanzicraft.com/)
- [GitHub Repository](https://github.com/pwxcoo/chinese-xinhua)
- [Resource](https://huggingface.co/fnlp/bart-base-chinese)
- [Resource](https://huggingface.co/bert-base-chinese)
- [GitHub Repository](https://github.com/fxsjy/jieba)
- [Resource](https://chat.openai.com/)

## 🎯 Purpose and Intended Users

**Goal**: To propose and release the first large-scale, high-coverage QA dataset of Chinese character riddles (CC-Riddle) to evaluate language models' ability to solve character riddles requiring glyph, commonsense and figurative language understanding, and to provide a resource for research on Chinese characters and figurative language.

**Target Audience**:
- Machine Learning Researchers
- Model Developers
- Researchers in Chinese Language Studies

**Tasks**:
- Question Answering
- Text Generation

**Limitations**: The authors note several limitations: BLEU is of limited usefulness for evaluating riddle generation because many reasonable riddle descriptions need not be lexically similar to references; some common characters are missing because generated riddles for them were rejected during filtering; pinyin/pronunciation-based riddles are rare in human-written data and were not taken into consideration in generation without special processing.

## 💾 Data

**Source**: Web-crawled human-written Chinese character riddles from multiple websites and model-generated riddles produced by a fine-tuned Chinese BART model using input glyph (from IDS dictionary and HanziCraft), pinyin and meaning (from Chinese Xinhua Dictionary); generated candidates were manually filtered by human annotators.

**Size**: 27,517 unique riddles; covers 7,279 characters. Split by characters: training 16,626 riddles (4,367 characters), validation 5,480 riddles (1,457 characters), test 5,411 riddles (1,455 characters). Generated riddles after filtering: 7,132.

**Format**: N/A

**Annotation**: Manual filtering of generated candidates by 20 native Chinese annotators (agreement ratio 83.95% on acceptance); manual riddle-solving test annotated by three annotators (closed-book).

## 🔬 Methodology

**Methods**:
- Retrieval-based Question Answering (BERT fine-tuned with multiple negatives ranking loss)
- Generative Question Answering (ChatGPT gpt-3.5-turbo-0301 and ChatGLM-6B evaluated via prompted generation and regex extraction)
- Multiple-choice Question Answering (ChatGPT and ChatGLM with distractors: random or embedding-similar)
- Human (manual) evaluation / riddle-solving annotation
- Riddle generation via fine-tuned Chinese BART model (beam search, blocked solution token)

**Metrics**:
- Accuracy
- BLEU-4
- Distinct unigrams
- Distinct bigrams

**Calculation**: Accuracy: computed as top-1 correctness for retrieval-based, generative and multiple-choice QA. Retrieval model trained with multiple negatives ranking loss; top-1 returned candidate evaluated for accuracy. Generative QA: model outputs processed with regular expressions to extract the answer; BLEU-4 and distinct n-gram counts computed on top-1 generation outputs (BLEU reported on 100 test characters for generation evaluation). Distinct unigrams and bigrams counted to assess diversity.

**Interpretation**: Higher Accuracy indicates better riddle-solving. The authors report that multiple-choice QA is the easiest, retrieval-based QA is harder, and generative QA is the most challenging (comparable to manual test). BLEU-4 is limited as reference diversity makes lexical similarity a poor proxy for quality; distinct n-gram counts measure diversity of generated riddles. Supplementary glyph and definition information improves retrieval performance, with glyphs especially useful.

**Baseline Results**: Retrieval-based QA (BERT) top-1 accuracy: Character input 0.0015 (all), Glyph supplemented 0.1133 (all), Definition supplemented 0.0381 (all). Generative QA: ChatGPT accuracy 0.0039 (all), ChatGLM accuracy 0.0013 (all). Multiple-choice QA: ChatGPT random-distractors accuracy 0.4153 (all); ChatGPT similar-distractors accuracy 0.4016 (all); ChatGLM random 0.2706, similar 0.2277 (all). Manual annotation on 100 samples: Annotator A accuracy 0.38, Annotator B 0.18, Annotator C 0.65. Generation evaluation (top-1 BLEU-4 on 100 tested characters): Ours 3.87, Template-based 4.67, Replacement-based 29.33. (Results reported separately for web-crawled vs generated subsets in the paper.)

**Validation**: Dataset split by characters into training/validation/test with ratio 6:2:2 (validation set: 98 characters, test set: 100 characters for generation experiments). Generated candidates were manually filtered with two annotators per candidate and a third annotator resolving disagreements; human evaluation conducted on 100 randomly sampled test entries with three annotators.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
