from functools import total_ordering
import pandas as pd 
import matplotlib.pylab as plt

#read excel file 
datasheet=pd.read_excel('Dataset.xls')
print(datasheet)

#Get Age , Gender , Education , Hours , News , Teledrama , Movies , Political , Educational , Doc , Sport   
age = datasheet[['Age']]
gender = datasheet[['Gender']]
education = datasheet[['Education']]
hours = datasheet[['Hours']]
news = datasheet[['News']]
teledrama = datasheet[['Teledrama']]
movies = datasheet[['Movies']]
political = datasheet[['Political']]
educational = datasheet[['Educational']]
document = datasheet[['Documentry']]
sport = datasheet[['Sport']]

    #--------- Data Analysis --------

#--Sport
countOfSport =(sport.value_counts())
print(countOfSport)

#--Documentry
countOfDocumentry =(document.value_counts())
print(countOfDocumentry)

#--Educational
countOfEducational =(educational.value_counts())
print(countOfEducational)

#--Political
countOfPolitical =(political.value_counts())
print(countOfPolitical)

#--Movies
countOfMovies =(movies.value_counts())
print(countOfMovies)

#--Teledrama
countOfTeledrama =(teledrama.value_counts())
print(countOfTeledrama)

#--News
countOfNews =(news.value_counts())
print(countOfNews)

#--Hours
countOfHours =(hours.value_counts())
print(countOfHours)

#--Education
countOfEducation =(education.value_counts())
print(countOfEducation)

#--Gender
countOfGender =(gender.value_counts())
print(countOfGender)

#--Age
countOfAge =(age.value_counts())
print(countOfAge)


#--- **Generate chart** ---

PieLable = ['Do not watch','Rarely watch','Averagly watch','Freqently watch','Very freqently watch'] 
barLable = ['Do not watch','Rarely watch','Averagly watch','Freqently watch']

#*****pie_chart*****

#Gender----pie_chart ---
genderPieValues= [countOfGender[2],countOfGender[1]] 
genderPieLable =['Male','Female']
plt.pie(genderPieValues,labels=genderPieLable,autopct='%f%%')
plt.title('Gender',fontsize=20,fontname='Times New Roman',color='red')
plt.show()

#Sport----pie_chart ---
sportPieValue = [countOfSport[1],countOfSport[2],countOfSport[3],countOfSport[4],0]
plt.pie(sportPieValue,labels=PieLable,autopct='%f%%')
plt.title('Sport',fontsize=20,fontname='Times New Roman',color='red')
plt.show()


#*****bar_chart*****

#Sport----bar_chart ---
sportBarValue = [countOfSport[1],countOfSport[2],countOfSport[3],countOfSport[4]]
plt.bar(barLable,sportBarValue)
plt.title('Sport Bar chart',fontsize=20,fontname='Times New Roman',color='red')
plt.show()


#Documentry----bar_chart ---
documentBarValue = [countOfDocumentry[1],countOfDocumentry[2],countOfDocumentry[3],countOfDocumentry[4]]
plt.bar(barLable,documentBarValue)
plt.title('Documentry Bar chart',fontsize=20,fontname='Times New Roman',color='green')
plt.show()





