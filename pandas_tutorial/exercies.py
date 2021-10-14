import numpy as np
import pandas as pd

sal = pd.read_csv('Salaries.csv')

sal.head()

#sal.info()

sal['BasePay'].mean()

sal['OvertimePay'].max()

sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']

sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']

sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]['EmployeeName']

sal.iloc[sal['TotalPayBenefits'].argmax()]

sal.iloc[sal['TotalPayBenefits'].argmin()]

sal.groupby('Year').mean()['BasePay']

sal['JobTitle'].nunique()

sal['JobTitle'].value_counts().head(5)

sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1)

def chief_string(title):
    if 'chief' in title.lower().split():
        return True
    else:
        return False

sum(sal['JobTitle'].apply(lambda x: chief_string(x)))

sal['title_len'] = sal['JobTitle'].apply(len)

sal['title_len']

sal[['TotalPayBenefits', 'title_len']].corr()

ecom = pd.read_csv('Ecommerce Purchases')

ecom.head()

#ecom.info()

ecom['Purchase Price'].mean()

ecom['Purchase Price'].min()

ecom['Purchase Price'].max()

ecom[ecom['Language'] == 'en'].count()

#ecom[ecom['Job'] == 'Lawyer'].info()

ecom['AM or PM'].value_counts()

ecom['Job'].value_counts().head(5)

ecom[ecom['Lot'] == '90 WT']['Purchase Price']

ecom[ecom['Credit Card'] == 4926535242672853]['Email']

#ecom[ (ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95) ].info()

ecom[ecom['CC Exp Date'].apply(lambda exp: exp[3:] == '25')].count()

ecom['Email'].apply(lambda email: email.split('@')[1]).value_counts().head(5)
