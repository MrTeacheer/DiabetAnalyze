# task 1 Импорт необходимых библиотек
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# task 2 Загрузка набора данных
data=pd.read_csv('dataset.csv')
# task 3 Первоначальный анализ данных
print(data.head(10),'\n')
print(data.tail(10),'\n')
print(data.describe(),'\n')
print(data.info(),'\n')
print(data.isnull().sum(),'\n')
# task 4 Проверка и удаление дубликатов
print(data.duplicated().sum())
data.drop_duplicates(inplace=True)
print(f'dupdrop_result: {data.duplicated().sum()}\n')
# task 5 Импутация пропусков
missing_values=data.isnull().sum()
missing_values=missing_values[missing_values>0]
print(f'{missing_values}\n')
filled_data=data
for c in missing_values.index:
    if data[c].dtype in ['int64', 'float64']:
        filled_data = data[c].fillna(data[c].mean())
    else:
        filled_data = data[c].fillna(data[c].mod()[0])
print(f'fill_result: {filled_data.isnull().sum()}\n')

male=data[data['gender']=='Male']
female=data[data['gender']=='Female']
missing_male=male.isnull().sum()[male.isnull().sum()>0]
missing_female=female.isnull().sum()[female.isnull().sum()>0]
print(f'male:\n{missing_male}\n')
print(f'female:\n{missing_female}\n')
check=data
for c in missing_values.index:
    if check[c].dtype in ['int64', 'float64']:
        mean_male=male[c].mean()
        mean_female=female[c].mean()
        check.loc[check['gender']=='Male', c]=check.loc[check['gender']=='Male', c].fillna(mean_male)
        check.loc[check['gender']=='Female', c]=check.loc[check['gender']=='Female', c].fillna(mean_female)
    else:
        mode_male=male[c].mode()[0]
        mode_female=female[c].mode()[0]
        check.loc[check['gender']== 'Male', c]=check.loc[check['gender'] == 'Male', c].fillna(mode_male)
        check.loc[check['gender']=='Female', c]=check.loc[check['gender'] == 'Female', c].fillna(mode_female)
print(check.isnull().sum(),'\n')
# task 6 Переименование столбца
data.rename(columns={'bmi':'BMI'}, inplace=True)
print(data.columns)
# task 7 Анализ категориальных данных с помощью value_counts()
value_count=data['smoking_history'].value_counts()
print(value_count,'\n')
print(value_count.idxmax(),'\n')
print(value_count.idxmin(),'\n')
# task 8 Анализ корреляции между столбцами
correlation_matrix = data.corr(numeric_only=True)
print(correlation_matrix)
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Матрица корреляции')
plt.show()
# task 9 Использование .loc и .iloc
print(data.loc[1,'smoking_history'])
print(data.iloc[4,1])
# task 10 Выборка данных по условию
print(data[data['age']>50])
print(data[(data['smoking_history']=='current') & (data['HbA1c_level']>7)])
print(data[(data['BMI']>25) & (data['diabetes']==1)])
print(data[(data['gender']=='Female') & (data['heart_disease']==1)])
print(data[(data['hypertension']==1) | (data['diabetes']==1)])
print(data[(data['age']>40)&(data['hypertension']==1) | (data['diabetes']==1) & (data['BMI']<30)])
# task 11 Создание нового столбца с помощью .apply()
data['HbA1c_level_category']=data['HbA1c_level'].apply(lambda x: 'low' if x<=4 else 'medium' if 4<x<=7 else 'high')
print(data)
# task 12 Визуализация данных с использованием matplotlib.pyplot
plt.hist(data['age'], bins=20, color='skyblue', edgecolor='black')
plt.title('Распределение возраста пациентов')
plt.xlabel('Возраст')
plt.ylabel('Частота')
plt.show()

diabetes_status_counts = data['diabetes'].value_counts()
plt.bar(diabetes_status_counts.index, diabetes_status_counts, color=['green', 'red'])
plt.title('Количество пациентов по статусу диабета')
plt.xlabel('Статус диабета')
plt.ylabel('Количество пациентов')
plt.show()

plt.scatter(data['BMI'], data['blood_glucose_level'], color='blue', alpha=0.5)
plt.title('Зависимость между BMI и уровнем глюкозы в крови')
plt.xlabel('BMI')
plt.ylabel('Уровень глюкозы в крови')
plt.show()

plt.boxplot(data['HbA1c_level'])
plt.title('Распределение уровня гликированного гемоглобина')
plt.xlabel('Уровень HbA1c')
plt.ylabel('Значения')
plt.show()

data.boxplot(column='BMI', by='diabetes', figsize=(8, 6))
plt.title('Распределение BMI в группах с положительным и отрицательным статусом диабета')
plt.xlabel('Статус диабета')
plt.ylabel('BMI')
plt.show()

data.boxplot(column='age', by='diabetes', figsize=(8, 6))
plt.title('Распределение возраста в группах с положительным и отрицательным статусом диабета')
plt.xlabel('Статус диабета')
plt.ylabel('Возраст')
plt.show()

# task 13 Визуализация данных с использованием Seaborn
sns.distplot(data['BMI'], bins=20, color='skyblue', kde=False)
plt.title('Распределение значений BMI')
plt.xlabel('BMI')
plt.ylabel('Частота')
plt.show()

sns.pairplot(data)
plt.show()

sns.boxplot(x='diabetes', y='HbA1c_level', data=data)
plt.title('Распределение HbA1c_level в группах с положительным и отрицательным статусом диабета')
plt.xlabel('Статус диабета')
plt.ylabel('HbA1c_level')
plt.show()