# intent-detection

Dataset: BANKING-77 (https://huggingface.co/datasets/banking77)


### TODOs

- [x] Explore data
  - [x] Data validation: train-test splits, distributions
- [x] Establish a baseline
  - [x] Grid search with simple linear models (SVM, LogReg)
- [x] Experiment with transfer-learning
  - [x] Fine-tune BERT
  - [ ] GPT-3
    - [x] Prompting, classification API
    - [ ] Fine-tune GPT-3 completion
- [ ] Explore dialogue-system specific model architectures
  - [ ] DIET (Rasa)
  - [ ] ConveRT (PolyAI)
- [ ] Error analysis
  - [ ] Use-case specific test sets
    - [ ] Performance on misspelled messages
    - [ ] Performance on STT-transcribed messages
- [ ] Deployment

### Notebooks

- Data exploration: data_stats.ipynb
- Baselines: baseline.ipynb
- Fine-tuning BERT: BERT.ipynb
- GPT-3 experiments: GPT-3.ipynb