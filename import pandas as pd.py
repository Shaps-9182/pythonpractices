import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
data=pd.read_csv(r"C:\Users\leisi\OneDrive\Pictures\Desktop\ultimate_student_productivity_dataset_5000.csv")
print(data.columns)
print(data.dtypes)
data['internet_quality']=data['internet_quality'].map({'poor':0,'Average':1,'Good':2})
data['exam_score']=data['exam_score'].apply(lambda x:1 if x >=50 else 0)
x=data[['study_hours','self_study_hours','online_classes_hours','mental_health_score']]
y=data['exam_score']
scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)
X_train,X_test,y_test=train_test_split(X_scaled,y,train_size=0.2,random_state=42)
model=LogisticRegression()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)
print(f"model accuracy:"{accuracy*100:.2f}%)
print("confusion matrix.")
print(confusion_matrix(y_test,y_pred))
print("classificatio report.")
print(classification_report(y_test,y_pred))
importance=pd.DataFrame({'feature':x.columns,'coefficient':model.coef_[0]})
print(importance)
print("\nenter your daily data below:")
study_hours=float(input("Enter hours studied today:"))
self_study_hours=float(input("Hour you self_studied today:"))
online_hour=float(input("Hours spent in social media today"))
social_media=float(input("Hours spent in social media today:"))
gaming_hours=float(input("Hour spent in gaming today:"))
sleep_hours=float(input("Hour spent in sleep today:"))
screen_time=float(input("Hour spent in screen time:"))
exercise_minutes=int(input("Minutes spent in exercing today:"))
caffeine_intake_mg=int(input("Mg of caffeine taken today:"))
part_time_job=int(input("How part time job did you do today:"))
upcoming_deadline=int(input("upcoming deadline today:"))
internet_quality_input=input(input("Internet quality(poor\average\good):")).strip().lower()
internet_quality_map={'Poor:0,average:1,good:2'}
internet_quality=internet_quality_map.get(internet_quality_input, 1)
mental_health_score=int(input("Mental Health today"))
focus_index=float(input("focus index today:"))
burnout_level=float(input("burn out level today:"))
productivity_score=float(input("productivity score today:"))
student_today=np.array[study_hours,self_study_hours,online_classes_hours,mental_health_score]
student_scaled=scaler.transform(student_today)
exam_score_prob=model.predict_proba(student_scaled)[0][1]
print(f"\exam_score_probability:{exam_score_prob*100:.2f}%")
print(f"raw input:{student_today}")
print(f"scaled input:{student_scaled}")
print(f"model probability:{model.predict_proba(student_scaled)}")
fail_prob=1-exam_score_prob
print(f"fail prob:{fail_prob}")
alerts=[]
if study_hours==0:
    alerts.append("you havent studied today.\n Try to study to increase your exam scores.")
if sleep_hours<6:
    alerts.append("you slept less than 6 hours.\n proper sleep improves focus and exam scores")
if gaming_hours<5:
    alerts.append("high gaming detected .\n reduce gaming to increase productivity")
if mental_health_score<5:
    alerts.append("Your mental health is not good .\n relax a little bit or seek help to improve your mental wellness and exam scores")
if exam_score_prob<0.7:
    alerts.append("Your exam scores probability is only{exam_score_prob*100:.2f}%.\n consider improving your study habits today")
print("\nAlert:")

