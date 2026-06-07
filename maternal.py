# Backend

# Smart Maternal Care Tracker

# ------ Import module -------

from datetime import timedelta

# ------- Class --------

class SmartMaternalCareTracker:
    
    def __init__(self,last_date, current_date):
        
        self.lmp = last_date
        self.today = current_date
    
# ------- Gestational age chacker --------
    
    def g_age_calc(self):
        
        self.days = (self.today - self.lmp).days
        self.weeks = self.days // 7
        self.remaining_days = self.days % 7
    
        return (                
                self.weeks,
                self.remaining_days    
                )
      
# ------- Trimester --------      
    
    def trimester(self):
        if self.weeks <= 13:
            return "1st Trimester"
        elif self.weeks <= 27:
            return "2nd Trimester"
        elif self.weeks <= 40:
            return "3rd Trimester"
        else:
            return "Post-term pregnancy"
        
# ------- Scan scheduler --------
    
    def scan_scheduler(self):
        if 6 <= self.weeks <= 8:
            return "You may need an ultrasound for confirmation of intrauterine pregnancy."
        elif 18 <= self.weeks <= 22:
            return "You may need a fetal anomaly scan (detailed morphology ultrasound)!"
        elif self.weeks >= 28:
            return "You may need a fetal growth scan!"
        else:
            return "No scheduled scan due currently!"

# ------- Risk prediction --------

    def monitoring_alerts(self):
        
        if self.weeks < 0:
            return "Invalid dates!"
        elif self.weeks > 40:
            return "You have reached/post passed due date. Please visit your healthcare provider for routine check-up and guidance."
        elif self.weeks > 32:
            return "Doctor may assess need for injections to support baby's lung development if early delivery risk exist!"
        elif self.weeks >= 20:
            return "Please confirm tetanus vaccination status."
        else:
            return "Everything seems normal!"
    
# ------- Edd detector --------
    
    def edd_detector(self):
        self.edd = self.lmp + timedelta(days=280)
        return self.edd
    
