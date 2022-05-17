# intent-detection

**Goal**: Develop an intent detection model that serves as part on an NLU component in a dialogue system

**Dataset**: [BANKING-77](https://huggingface.co/datasets/banking77)


### Project plan

- [x] Define, explore and validate data
  - [x] Data validation: train-test splits, distributions
  - [ ] Data validation: look for wrong labels and anomalies in annotation
    - Consider using [cleanlab](https://github.com/cleanlab/cleanlab) or [doublab](https://github.com/koaning/doubtlab)
  - [ ] Consider extending the current intents with
    - Out-of-scope intents
    - Smalltalk/Chitchat intents
- [x] Establish a baseline
  - [x] Grid search with simple linear models (SVM, LogReg)
- [x] Experiment with transfer-learning
  - [ ] BERT
    - [x] Fine-tune BERT
    - [ ] Consider other BERT-based architectures (DistillBERT, RoBERTa, etc.)
  - [x] GPT-3
    - [x] Prompting, classification API
    - [x] Fine-tune GPT-3 completion
- [ ] Explore dialogue-system specific model architectures
  - [ ] DIET (Rasa)
  - [ ] ConveRT (PolyAI)
- [ ] Error analysis
  - [ ] Use-case specific test sets
    - [ ] Performance on misspelled messages
      - At the moment the training data is clean and doesn't contain common errors in spoken/written text, this could make the training data out of distribution compared to live user messages
      - Consider using [NLPAUG](https://github.com/makcedward/nlpaug) to generate test set with misspelled messages
      - Use keyboard policy to produce common misspellings based on keyboard layout
    - [ ] Performance on STT-transcribed messages 
      - STT engines sometimes transcribe the wrong word based on user utterance, measure how likely it is that an intent is misclassified due to the error in STT
      - Generate a test set where random words are swapped to similar words (ie.: ones that are close in edit distance), mesure model performance
  - [x] Reporting and documentation of experiments
- [ ] Modeling improvements, model analysis
  - [ ] Fine-tuning based on use-case specific test set findings
    - Include misspelled word, common errors based on STT engine used in production
  - [ ] Establish the probability threshold when the predictions are likely to be wrong and the system should default to a fallback intent
  - [ ] Validate that the model behaves as intended and can't be fooled with malicious inputs
    - Consider performing a model attack with [TextAttack](https://github.com/QData/TextAttack) or similar library to understand weaknesses of the model
- [ ] Deployment
  - [ ] Measure model performance
    - Consider things like inference time, architectural requirements for the model to be deployed, estimated cost, scalability, etc.
  - [x] "Deployment" to Google Colab
  - [ ] Serverless deployment (ie.: Google Cloud Run) for testing with off-the-shelf UIs internally
  - [ ] MLOps considerations
    - Establish the possibility to continously measure the model performance
    - Detect data shift and concept shifts automatically
    - Discuss the frequency or criteria that indicates that the model needs to be retrained and redeployed

### Notebooks

- Data exploration: `data_stats.ipynb`
- Baselines: `baseline.ipynb`
- Fine-tuning BERT: `BERT.ipynb`
- GPT-3 experiments: `GPT-3.ipynb`
- Interact with models: `infer_models.ipynb`

### Report

[Report on Wandb](https://wandb.ai/nsoma/intent-detection/reports/Intent-detection-model-comparison--VmlldzoyMDI2NDMx)