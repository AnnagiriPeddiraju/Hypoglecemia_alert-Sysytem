# Hypoglycemia Prediction & Smart Alert System Architecture

```mermaid
flowchart TD
  subgraph Data Sources
    CGM[Continuous Glucose Monitor]
    Wearables[Wearable Sensors]
    Manual[Manual Entries]
  end

  subgraph Processing
    Preproc[Data Preprocessing & Feature Engineering]
    Model[Deep Learning Model (LSTM/Transformer)]
    Prediction[Real-Time Prediction]
  end

  subgraph Alert
    SmartAlert[Smart Alert Engine]
    UI[User/Caregiver Interface]
    Escalation[Escalation Policy]
  end

  CGM --> Preproc
  Wearables --> Preproc
  Manual --> Preproc
  Preproc --> Model
  Model --> Prediction
  Prediction --> SmartAlert
  SmartAlert --> UI
  SmartAlert --> Escalation
```