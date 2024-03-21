from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
import pickle
from sklearn.linear_model import LinearRegression
import numpy as np
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.graphics import Rectangle


class SalaryPredictionApp(App):
    def build(self):
        self.avg_salary_label = Label(text="Average Salary: ",bold=True,color=(1,.5,.7,1))
        self.programming_language_label = Label(text="Programming Language: ",bold=True,color='red')
        self.programming_language_spinner = Spinner(text="Select Language", values=["C++","Java","JavaScript","Python"],background_color=(.5,1,1, .7),color=(1, 1, 1, 1))
        self.job_role_label = Label(text="Job Role: ",color="red")
        self.job_role_spinner = Spinner(text="Select Role", values=["Data Scientist","Dev Ops Engineer", "Product Manager", "Software Enigneer"],background_color=(.5,1,1, .7),color=(1, 1, 1, 1))
        self.predict_button = Button(text="Predict", on_press=self.predict_salary,background_color=(.5,1,1, .7),color=(1, 1, 1, 1),bold=True)
        self.prediction_label = Label(text="Predicted Salary: ",color="blue",bold=True)
 
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        layout.add_widget(self.avg_salary_label)
        layout.add_widget(self.programming_language_label)
        layout.add_widget(self.programming_language_spinner)
        layout.add_widget(self.job_role_label)
        layout.add_widget(self.job_role_spinner)
        layout.add_widget(self.predict_button)
        layout.add_widget(self.prediction_label)
        

        # Bind the function to handle size changes
        layout.bind(size=self.update_background)
        
       
    

    

        return layout
    def update_background(self, instance, value):
        # Clear existing canvas instructions
          instance.canvas.before.clear()

        # Redraw the background Rectangle with the updated size
          instance.canvas.before.add(Rectangle(pos=instance.pos, size=instance.size, source='download.jpg'))
  
    def predict_salary(self, instance):
        # Add your salary prediction logic here
        user1=3
        user2=3
        selected_language = self.programming_language_spinner.text
        selected_role = self.job_role_spinner.text
        if selected_language=="C++":
            user1=0
        elif selected_language=="Java":
             user1=1
        elif selected_language=="JavaScript":
             user1=2

        if selected_role=="Data Scientist":
            user2=0
        elif selected_role=="Dev Ops Engineer":
            user2=1
        elif selected_role=="Product Manager":
            user2=2
            
        with open('model.pkl','rb')as file:
            model=pickle.load(file)
            sd=model.predict([[user1,user2]])
        

            df=np.round(sd/12,decimals=0)
            dg=df*1.5

            self.prediction_label.text = f"Predicted Salary for {selected_language} {selected_role}:{df}-{dg}"

if __name__ == '__main__':
    SalaryPredictionApp().run()
